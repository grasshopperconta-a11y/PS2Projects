#!/usr/bin/env python3
"""
fnf_to_fch3.py - Friday Night Funkin' v0.8.6 chart -> PS2 FCH3 converter.

Part of the FNF v0.8.6 -> PS2 port data pipeline (plan section 4.4).
Converts the original game's song/chart JSON into the port's proven binary
chart container "FCH3" (recovered from the v0.1.99-fix27 implementation).

FCH3 container layout (little-endian, FNV-1a validated):
  header  40 B: b"FCH3" | u16 version=3 | u16 note_stride=12 | u32 note_count
               | u16 bpm_count | u16 section_count | u16 event_count | u16 rsv
               | u16 bpm_stride=16 | u16 section_stride=8 | u16 event_stride=16
               | u16 rsv | u32 fnv1a(payload) | u32 song_end_sample | u32 rsv
  note    12 B: u32 sample | u32 duration | u8 lane(0..3) | u8 must_press | u16 order
  bpm     16 B: u32 start_step | u32 start_sample | u32 samples_per_step | u32 bpm
  section  8 B: u32 start_step | u8 must_hit | u8 length_steps | u16 order
  event   16 B: u32 sample | u32 type | u32 value | u32 order
             value packs up to two numeric event values: value1 in the low
             16 bits, value2 in the high 16 bits (FocusCamera carries char).

Input formats supported (both produced by FNF v0.8.6):
  * legacy : {"song": {"bpm":..,"speed":..,"notes":[{mustHitSection,sectionNotes:
              [[t,d,len],..]}], "events":[[name,t,v1,v2],..]}}
  * v2     : metadata.json (SongMetadata) + charts/<difficulty>.json (SongChartData)

Semantics taken from the original source:
  * Note times are milliseconds (SongMetadata.timeFormat = 'ms').
  * SongTimeChange.timeStamp is a timestamp in the song's timeFormat, i.e.
    MILLISECONDS (not steps) - funkin.data.song.SongTimeChange.
  * Legacy BPM changes are applied at the first note's timestamp of the section
    that carries changeBPM (FNFLegacyImporter.rebuildTimeChanges).
  * Legacy note data: 0..3 player strumline (left,down,up,right), 4..7 opponent
    (floor(data/4) = strumline index). Legacy charts flip 0..3 <-> 4..7 when
    mustHitSection is false. data < 0 are Psych event notes (skipped).
  * Legacy sections carry mustHitSection and lengthInSteps (default 16).

Usage:
  python3 fnf_to_fch3.py --legacy song.json --difficulty hard -o hard.chart
  python3 fnf_to_fch3.py --metadata metadata.json --chart chart.json -o chart.bin
  python3 fnf_to_fch3.py --selftest
"""
import argparse
import json
import struct
import sys

SAMPLE_RATE = 48000
STRUMLINE_SIZE = 4          # lanes per strumline
STEPS_PER_BEAT = 4
DEFAULT_BPM = 100.0         # funkin.data.song.SongTimeChange.DEFAULT
SECTION_STEPS = 16          # FNF chart editor section length
DEFAULT_DIFFICULTY = "normal"

# FNF song event -> port FCH3 event type id.
# Integration decision (plan 4.4): the port's event registry assigns these ids;
# FocusCamera is the only event the legacy importer synthesises automatically.
EVENT_TYPES = {
    "FocusCamera": 1,
    "ChangeCharacter": 2,
    "PlayAnimation": 3,
    "AltIdleAnimation": 4,
}
EVENT_TYPE_UNKNOWN = 0xFFFF

MAGIC = b"FCH3"
VERSION = 3
NOTE_STRIDE = 12
BPM_STRIDE = 16
SECTION_STRIDE = 8
EVENT_STRIDE = 16


def fnv1a(data: bytes) -> int:
    h = 2166136261
    for b in data:
        h ^= b
        h = (h * 16777619) & 0xFFFFFFFF
    return h


# ----------------------------------------------------------------------------
# time model (timestamps in milliseconds, per SongTimeChange.timeStamp)
# ----------------------------------------------------------------------------
class Timeline:
    """ms/step/sample conversion driven by BPM time changes."""

    def __init__(self, time_changes):
        ch = sorted(((float(t), float(b)) for t, b in time_changes), key=lambda c: c[0])
        if not ch or ch[0][0] != 0.0:
            ch.insert(0, (0.0, DEFAULT_BPM))
        self.changes = ch

    @staticmethod
    def _ms_per_beat(bpm):
        return 60000.0 / bpm

    def sample_at_ms(self, ms):
        return int(round(float(ms) * SAMPLE_RATE / 1000.0))

    def step_at_ms(self, ms):
        """Steps elapsed at the given millisecond timestamp."""
        step = 0.0
        for i, (t, bpm) in enumerate(self.changes):
            end_t = self.changes[i + 1][0] if i + 1 < len(self.changes) else None
            if ms <= t:
                break
            seg_end = end_t if (end_t is not None and ms > end_t) else ms
            span = seg_end - t
            if span > 0:
                step += span / self._ms_per_beat(bpm) * STEPS_PER_BEAT
            if end_t is None or ms <= end_t:
                break
        return step

    def ms_at_step(self, step):
        """Millisecond timestamp of the given step position."""
        ms = 0.0
        cur = 0.0
        for i, (t, bpm) in enumerate(self.changes):
            end_t = self.changes[i + 1][0] if i + 1 < len(self.changes) else None
            mpb = self._ms_per_beat(bpm)
            if end_t is None:
                seg = step - cur
                if seg > 0:
                    ms += seg * mpb / STEPS_PER_BEAT
                cur = step
                break
            seg_steps = (end_t - t) / mpb * STEPS_PER_BEAT
            if cur + seg_steps >= step:
                ms += (step - cur) * mpb / STEPS_PER_BEAT
                cur = step
                break
            ms += seg_steps * mpb / STEPS_PER_BEAT
            cur += seg_steps
        return ms

    def samples_per_step(self, bpm):
        return int(round(self._ms_per_beat(bpm) / STEPS_PER_BEAT * SAMPLE_RATE / 1000.0))


# ----------------------------------------------------------------------------
# chart extraction
# ----------------------------------------------------------------------------
def _legacy_notes(song):
    """Yield (time_ms, data, sustain_ms) from a legacy FNF chart."""
    for section in song.get("notes", []):
        must_hit = bool(section.get("mustHitSection", False))
        for entry in section.get("sectionNotes", []):
            if len(entry) < 2:
                continue
            t = float(entry[0])
            data = int(entry[1])
            length = float(entry[2]) if len(entry) > 2 and entry[2] is not None else 0.0
            if data < 0:
                continue  # Psych event note
            if data > STRUMLINE_SIZE * 2:
                data = data % (2 * STRUMLINE_SIZE)
            if not must_hit:  # flip: player notes are 4..7 in non-must-hit sections
                data = data - STRUMLINE_SIZE if data >= STRUMLINE_SIZE else data + STRUMLINE_SIZE
            yield t, data, length


def _legacy_time_changes(song):
    """(time_ms, bpm) pairs; changes land on the first note of their section."""
    out = [(0.0, float(song.get("bpm", DEFAULT_BPM)))]
    for section in song.get("notes", []):
        if section.get("changeBPM", False) and section.get("sectionNotes"):
            t = float(section["sectionNotes"][0][0])
            out.append((t, float(section.get("bpm", DEFAULT_BPM))))
    return out


def _legacy_sections(song):
    """(start_step, must_hit, length_steps) straight from the chart sections."""
    return [(float(s.get("sectionNotes", [[0]])[0][0]),
             1 if s.get("mustHitSection", False) else 0,
             int(s.get("lengthInSteps", SECTION_STEPS) or SECTION_STEPS))
            for s in song.get("notes", [])]


def _legacy_events(song):
    """Legacy event rows are [name, strumTime, value1, value2]."""
    out = []
    for e in song.get("events", []) or []:
        if len(e) < 2:
            continue
        out.append((float(e[1]), str(e[0]), list(e[2:])))
    return out


def _v2_notes(chart, difficulty):
    notes = []
    per_diff = chart.get("notes", {}) or {}
    arr = per_diff.get(difficulty)
    if arr is None:
        if not per_diff:
            return notes
        arr = next(iter(per_diff.values()))  # fall back to first difficulty
    for n in arr:
        t = float(n.get("t", n.get("time", 0.0)))
        data = int(n.get("d", n.get("data", 0)))
        length = float(n.get("l", n.get("length", 0.0)) or 0.0)
        notes.append((t, data, length))
    return notes


def _v2_time_changes(metadata):
    changes = []
    for tc in metadata.get("timeChanges", []) or []:
        changes.append((float(tc.get("t", tc.get("time", 0.0))),
                        float(tc.get("bpm", tc.get("value", DEFAULT_BPM)))))
    return changes or [(0.0, DEFAULT_BPM)]


def _v2_events(chart):
    out = []
    for e in chart.get("events", []) or []:
        t = float(e.get("t", e.get("time", 0.0)))
        name = e.get("e", e.get("event", ""))
        values = e.get("v", e.get("values", [])) or []
        out.append((t, name, values))
    return out


def _sections_derived(notes, timeline):
    """Derive 16-step sections for v2 charts (which carry no section list)."""
    if not notes:
        return [(0, 1, SECTION_STEPS)]
    last_sample = max(s for s, _, _, _ in notes)
    last_step = int(timeline.step_at_ms(last_sample * 1000.0 / SAMPLE_RATE) // SECTION_STEPS)
    out = []
    for idx in range(last_step + 1):
        lo = timeline.sample_at_ms(timeline.ms_at_step(idx * SECTION_STEPS))
        hi = timeline.sample_at_ms(timeline.ms_at_step((idx + 1) * SECTION_STEPS))
        has_player = any(mp == 1 and lo <= s < hi for _, s, _, mp in notes)
        out.append((idx * SECTION_STEPS, 1 if has_player else 0, SECTION_STEPS))
    return out


# ----------------------------------------------------------------------------
# conversion
# ----------------------------------------------------------------------------
def build_fch3(notes_ms, time_changes, events, sections_ms=None,
               song_end_ms=None):
    """notes_ms: [(time_ms, data, sustain_ms)]; sections_ms: [(time_ms, must_hit,
    length_steps)] or None to derive. Returns (bytes, info dict)."""
    timeline = Timeline(time_changes)

    # ---- notes -------------------------------------------------------------
    notes = []
    for t, data, length in notes_ms:
        notes.append((timeline.sample_at_ms(t),
                      timeline.sample_at_ms(length) if length > 0 else 0,
                      data % STRUMLINE_SIZE,
                      1 if data < STRUMLINE_SIZE else 0))
    notes.sort(key=lambda n: (n[0], n[2]))
    for s, d, _, _ in notes:
        assert 0 <= s <= 0xFFFFFFFF and 0 <= d <= 0xFFFFFFFF

    # ---- bpm changes -------------------------------------------------------
    bpms = []
    for t_ms, bpm in timeline.changes:
        bpms.append((int(round(timeline.step_at_ms(t_ms))),
                     timeline.sample_at_ms(t_ms),
                     timeline.samples_per_step(bpm),
                     int(round(bpm))))
    dedup = []
    for b in bpms:
        if dedup and dedup[-1][0] == b[0]:
            dedup[-1] = b
        else:
            dedup.append(b)
    bpms = dedup

    # ---- sections ----------------------------------------------------------
    if sections_ms:
        sections = [(int(round(timeline.step_at_ms(t))), mh, ln)
                    for t, mh, ln in sections_ms]
        # merge duplicates / keep strictly increasing start_step
        merged = []
        for s in sorted(sections):
            if merged and merged[-1][0] == s[0]:
                merged[-1] = s
            else:
                merged.append(s)
        sections = merged
    else:
        sections = _sections_derived(notes, timeline)

    # ---- events ------------------------------------------------------------
    evs = []
    for t, name, values in events:
        etype = EVENT_TYPES.get(name, EVENT_TYPE_UNKNOWN)
        value = 0
        for i, v in enumerate(values[:2]):
            try:
                value |= (int(v) & 0xFFFF) << (16 * i)
            except (TypeError, ValueError):
                pass
        evs.append((timeline.sample_at_ms(t), etype, value))
    evs.sort(key=lambda e: e[0])

    # ---- song end ----------------------------------------------------------
    end_sample = 0
    for s, d, _, _ in notes:
        end_sample = max(end_sample, s + d)
    for s, _, _ in evs:
        end_sample = max(end_sample, s)
    if song_end_ms is not None:
        end_sample = max(end_sample, timeline.sample_at_ms(song_end_ms))
    if end_sample == 0:
        end_sample = SAMPLE_RATE  # 1 s floor keeps the loader's invariant

    # ---- serialise ---------------------------------------------------------
    payload = bytearray()
    for s, d, lane, mp in notes:
        payload += struct.pack("<IIBBH", s, d, lane, mp, 0)
    for st, ss, sps, bpm in bpms:
        payload += struct.pack("<IIII", st, ss, sps, bpm)
    for st, mh, ln in sections:
        payload += struct.pack("<IBBH", st, mh, ln, 0)
    for i, (s, etype, value) in enumerate(evs):
        payload += struct.pack("<IIII", s, etype, value, i)

    header = MAGIC + struct.pack(
        "<HHIHHHHHHHHIII",
        VERSION, NOTE_STRIDE, len(notes),
        len(bpms), len(sections), len(evs), 0,
        BPM_STRIDE, SECTION_STRIDE, EVENT_STRIDE, 0,
        fnv1a(bytes(payload)), end_sample, 0)
    assert len(header) == 40, len(header)
    return bytes(header) + bytes(payload), {
        "notes": len(notes), "bpms": len(bpms), "sections": len(sections),
        "events": len(evs), "song_end_sample": end_sample,
    }


def convert_legacy(path, difficulty):
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    song = doc.get("song", doc)
    return build_fch3(
        list(_legacy_notes(song)),
        _legacy_time_changes(song),
        _legacy_events(song),
        sections_ms=_legacy_sections(song))


def convert_v2(metadata_path, chart_path, difficulty):
    with open(metadata_path, encoding="utf-8") as f:
        meta = json.load(f)
    with open(chart_path, encoding="utf-8") as f:
        chart = json.load(f)
    return build_fch3(
        _v2_notes(chart, difficulty),
        _v2_time_changes(meta),
        _v2_events(chart))


# ----------------------------------------------------------------------------
# independent parser (mirrors the port loader's validation invariants)
# ----------------------------------------------------------------------------
def _parse_fch3(data):
    assert data[:4] == MAGIC, "bad magic"
    (ver, stride, count, bc, sc, ec, _r,
     bs, ss, es, _r2, checksum, end_sample, _r3) = struct.unpack_from("<HHIHHHHHHHHIII", data, 4)
    assert ver == VERSION and stride == NOTE_STRIDE
    assert bs == BPM_STRIDE and ss == SECTION_STRIDE and es == EVENT_STRIDE
    payload = data[40:]
    assert fnv1a(payload) == checksum, "checksum mismatch"
    notes = [struct.unpack_from("<IIBBH", payload, i * 12) for i in range(count)]
    off = count * 12
    bpms = [struct.unpack_from("<IIII", payload, off + i * 16) for i in range(bc)]
    off += bc * 16
    secs = [struct.unpack_from("<IBBH", payload, off + i * 8) for i in range(sc)]
    off += sc * 8
    evs = [struct.unpack_from("<IIII", payload, off + i * 16) for i in range(ec)]
    return notes, bpms, secs, evs, end_sample


def selftest():
    # 120 BPM: 1 step = 60000/120/4 = 125 ms = 6000 samples
    legacy = {
        "song": {
            "bpm": 120,
            "speed": 2.0,
            "notes": [
                {"mustHitSection": False, "lengthInSteps": 16,
                 "sectionNotes": [[0, 0, 0], [125, 1, 0], [2000, 4, 500]]},
                {"mustHitSection": True, "lengthInSteps": 16, "changeBPM": True, "bpm": 240,
                 "sectionNotes": [[4000, 0, 0], [4125, 5, 250]]},
            ],
            "events": [["FocusCamera", 0, 0, 1]],
        }
    }
    data, info = build_fch3(
        list(_legacy_notes(legacy["song"])),
        _legacy_time_changes(legacy["song"]),
        _legacy_events(legacy["song"]),
        sections_ms=_legacy_sections(legacy["song"]))
    notes, bpms, secs, evs, end = _parse_fch3(data)

    # container invariants from the port loader
    assert len(notes) == 5, info
    for i, n in enumerate(notes):
        assert n[2] <= 3 and n[3] <= 1
        assert n[4] == 0
        if i:
            assert n[0] >= notes[i - 1][0]      # sorted by sample
        assert n[0] <= end and n[0] + n[1] <= end
    assert bpms[0][0] == 0 and bpms[0][1] == 0 and bpms[0][3] == 120
    assert bpms[0][2] == 6000                   # samples per step at 120 BPM
    # BPM change at 4000 ms: step 4000/125 = 32, sample 4000*48 = 192000,
    # samples per step at 240 BPM = 60000/240/4 ms = 62.5 ms = 3000
    assert bpms[1][0] == 32 and bpms[1][1] == 192000, bpms[1]
    assert bpms[1][2] == 3000 and bpms[1][3] == 240, bpms[1]
    assert secs[0][0] == 0 and secs[0][1] == 0 and secs[0][2] == 16   # mustHit False
    assert secs[1][0] == 32 and secs[1][1] == 1                        # mustHit True
    assert evs[0][0] == 0 and evs[0][1] == 1      # FocusCamera -> type 1
    assert end >= max(n[0] + n[1] for n in notes)

    # must-hit flip: section 0 is mustHitSection=False so data 0,1 -> opponent
    # (4,5) and data 4 -> player (0); section 1 is mustHitSection=True so data
    # 0 -> player and data 5 -> opponent. Notes are sorted by sample, so the
    # first three come from section 0 and the last two from section 1.
    lanes = [(n[2], n[3]) for n in notes]
    assert lanes == [(0, 0), (1, 0), (0, 1), (0, 1), (1, 0)], lanes

    # time math: note at 125 ms -> 6000 samples; sustain 500 ms -> 24000
    assert notes[1][0] == 6000, notes[1]
    assert notes[2][0] == 2000 * 48 and notes[2][1] == 500 * 48, notes[2]

    # v2 path: sections derived from player-note presence
    v2chart = {"scrollSpeed": {"hard": 2.4}, "events": [], "notes": {"hard": [
        {"t": 0, "d": 0, "l": 0}, {"t": 1000, "d": 4, "l": 0}]}}
    v2meta = {"timeChanges": [{"t": 0, "bpm": 150}]}
    d2, i2 = build_fch3(_v2_notes(v2chart, "hard"), _v2_time_changes(v2meta),
                        _v2_events(v2chart))
    n2, b2, s2, e2, end2 = _parse_fch3(d2)
    assert b2[0][3] == 150 and b2[0][2] == 4800      # 150 BPM -> 4800 samples/step
    assert any(sec[1] == 1 for sec in s2), s2        # section with the player note
    print("selftest OK:", info, "| v2:", i2)
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--legacy", help="legacy FNF chart JSON (contains {\"song\": ...})")
    p.add_argument("--metadata", help="v2 SongMetadata JSON")
    p.add_argument("--chart", help="v2 SongChartData JSON")
    p.add_argument("--difficulty", default=DEFAULT_DIFFICULTY)
    p.add_argument("-o", "--output", help="output .chart path")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args(argv)

    if a.selftest:
        return selftest()
    if a.legacy:
        data, info = convert_legacy(a.legacy, a.difficulty)
    elif a.metadata and a.chart:
        data, info = convert_v2(a.metadata, a.chart, a.difficulty)
    else:
        p.error("provide --legacy, or --metadata with --chart, or --selftest")
    if a.output:
        with open(a.output, "wb") as f:
            f.write(data)
        print("wrote", a.output, len(data), "bytes:", info)
    else:
        sys.stdout.buffer.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
