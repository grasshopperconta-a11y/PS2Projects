# FCH4 — the chart container, revised

Status: **implemented 2026-10-15**. The converter emits v4 by default, the
loader reads both, and `tools/test_fch4.py` proves the round trip is lossless
on all 27 real charts. This document is the decision the code follows.

## Why v3 is not enough

FCH3's event record is 16 bytes:

```
u32 sample | u32 type | u32 value | u32 order
```

One `u32` of value. The converter packs a primary parameter in the low 16 bits
and a duration in the high 16, which is enough for the three events the port
currently acts on. It is not enough for what the charts actually contain.

`tools/survey_events.py` enumerates all 1,110 events in the 27 real charts:

| event | count | parameters |
|---|---|---|
| `FocusCamera` | 664 | `char`, `duration`, `ease`, `easeDir`, `x`, `y` |
| `ZoomCamera` | 207 | `duration`, `ease`, `easeDir`, `mode`, `zoom` |
| `SetCameraBop` | 105 | `intensity`, `offset`, `rate` |
| `PlayAnimation` | 32 | `anim`, `force`, `target` |
| `SetHealthIcon` | 15 | `char`, `flipX`, `id` |
| `ScrollSpeed` | 1 | `absolute`, `duration`, `ease`, `scroll`, `strumline` |
| `sserafim*` (11 kinds) | 84 | see below |

So 445 events carry parameters that v3 silently drops, and the port plays them
as if they were not there. `SetCameraBop` (105) replaces the beat bop that the
port hardcodes; `SetHealthIcon` (15) swaps the icon; `PlayAnimation` (32)
forces an animation. Converting them lossily and saying nothing would be worse
than not converting them.

## What v4 has to carry

Every parameter in the table above, with its real type:

- **Numerics** — `duration`, `x`, `y`, `zoom`, `intensity`, `offset`, `rate`,
  `scroll`, `amount`. All are floats or ints; `x`/`y`/`zoom`/`intensity` are
  fractional.
- **Small integers** — `char` (0/1/2), `mode` (`direct`/`stage`), `target`
  (`bf`/`boyfriend`/`dad`/`gf`), `strumline` (`both`), `easeDir`
  (`In`/`InOut`/`Out`), `rate` (1/2/4), `offset` (0/1).
- **Booleans** — `force`, `flipX`, `absolute`, `enabled`, `visible`, `final`,
  `beautiful`.
- **Strings** — `ease` (13 distinct names), `anim` (`cheer`/`hey`), `id`
  (7 names), plus the four above. 425 of the 1,110 events carry at least one.
- **Variable-length lists** — `sserafimPulseLights` carries `colors` (up to 4
  hex colours), `durations` and `intensities` (up to 4 floats each).
  `sserafimSing` and `sserafimShow` carry boolean lists of 6 and 5.

The 13 `ease` names, measured, not guessed:
`CLASSIC`, `INSTANT`, `circ`, `elastic`, `elasticInOut`, `expo`, `expoIn`,
`expoOut`, `linear`, `quad`, `quadInOut`, `quart`, `quintInOut`.

## Design

Three changes, and no others. Notes, BPM changes and sections keep their v3
layout exactly — they were already lossless.

### 1. The event record grows to 32 bytes (8 × u32)

```
 0  u32  sample        48 kHz position, as in v3
 4  u32  type          event id, same ids as v3
 8  u32  p0            numeric parameter 0, fixed-point x1000
12  u32  p1            numeric parameter 1, fixed-point x1000
16  u32  p2            numeric parameter 2, fixed-point x1000
20  u32  a             primary small-integer parameter
24  u32  b             secondary small-integer parameter + booleans
28  u32  ref           index into the string table or the block table
```

No `order` field: v3 required `order == index` for every record, so it carried
no information. v4 relies on the array position and drops it.

`a` holds the one small integer that names the event's subject:

| event | `a` |
|---|---|
| `FocusCamera` | `char` (0 = BF, 1 = opponent, 2 = GF) |
| `ZoomCamera` | `mode` (0 = `direct`, 1 = `stage`) |
| `PlayAnimation` | `target` (0 = bf, 1 = boyfriend, 2 = dad, 3 = gf) |
| `ScrollSpeed` | `strumline` (0 = both, 1 = opponent, 2 = player) |
| `SetHealthIcon` | `char` |

`b` packs the rest:

```
bits  0-15   ease index into EASE_NAMES
bits 16-17   easeDir (0 = In, 1 = Out, 2 = InOut)
bit  18      force      (PlayAnimation)
bit  19      flipX      (SetHealthIcon)
bit  20      absolute   (ScrollSpeed)
bit  21      ref_is_string
bit  22      ref_is_block
bits 23-31   spare, must be 0
```

`ref` is an index into the string table when `ref_is_string`, into the block
table when `ref_is_block`, and unused (0xFFFFFFFF) otherwise. The two bits are
mutually exclusive by construction.

### 2. A string table

```
u32  string_count
u32  string_bytes
then string_count x u32 offsets, then the NUL-terminated strings
```

Strings are stored once per file and referenced by index. The 13 ease names,
`cheer`, `hey`, and the 7 health-icon ids are the whole content today, so the
table is a few dozen bytes per chart. It exists so that adding a new anim name
or a new character does not mean another format revision.

### 3. A block table, for the one genuinely variable-length event

`sserafimPulseLights` is the only event whose parameters are lists of
different lengths, so it is the only one that cannot fit the fixed record.
Its parameters go in a block:

```
block:
  u32  param_count
  param_count x {
    u32  name_ref     index into the string table
    u32  elem_count
    elem_count x { u32 kind, u32 value }
  }
```

`kind`: `0` = float (value is the f32 bit pattern), `1` = int, `2` = RGB
(`0x00RRGGBB`), `3` = bool.

The block is self-describing — the parameter names travel with it — so the
port does not have to know the script's signature to read it, and a future
`.hxc` script event needs no format change either.

`sserafimSing` (6 booleans) and `sserafimShow` (5 booleans) do **not** need a
block: their lists are boolean masks that fit in `a`. So of the 84 scripted
events, only the 24 `sserafimPulseLights` use the block table.

### Header

v4's header is 48 bytes, v3's is 40. The first 28 bytes are identical in
meaning so a reader can dispatch on the magic and then read the right strides:

```
 0  4    magic "FCH4"
 4  u16   version = 4
 6  u16   note_stride = 12
 8  u32   note_count
12  u16   bpm_count
14  u16   section_count
16  u16   event_count
18  u16   flags  (bit 0 = has string table, bit 1 = has block table)
20  u16   bpm_stride = 16
22  u16   section_stride = 8
24  u16   event_stride = 32
26  u16   reserved = 0
28  u32   fnv1a(payload)
32  u32   song_end_sample
36  u32   string_count
40  u32   string_bytes
44  u32   block_count
```

## 3. What wiring it into main.c found

`src/chart_events.c` is the module that reads these records, and
`test/test_chart_events.c` proves it against the real charts. Building it caught
four things that the round-trip test could not, because the round trip only
checks that a value survives -- it does not check that the port *uses* it the way
the original does.

**The ease is a string-table index, not a fixed-list index.** The converter
writes `b`'s ease field as an index into the file's own string table
(`tools/fnf_to_fch3.py:452` says so in as many words). The first version of
`chart_events.c` read it as an index into the 13-name list, which is the exact
bug the round trip had already caught once -- an ease name the port has never
heard of would silently point at the wrong curve. `chart_events_ease_id()` now
resolves the name through `chart_event_string()`. The tutorial's ZoomCamera
carries `elasticInOut` at string index 0, so index 0 has to mean a curve, not
"absent".

**`elastic` + `InOut` and `elasticInOut` are one curve.** The original builds
`'$ease$easeDir'` and looks the result up in `FlxEase`, so both spellings find
the same function. The charts use both: `elasticInOut` 11 times and `elastic`
with `easeDir InOut` 5 times. `elasticIn` and `elasticOut` are never used by any
of the 27 charts, so rather than invent them both fall back to the InOut curve
and say so.

**`boyfriend` and `bf` are the same target id.** `tools/fnf_to_fch3.py` maps
both to 0. The header documented them as 0 and 1, which would have sent every
`PlayAnimation` aimed at `boyfriend` at a target that does not exist.

**Two PlayAnimation events can land on the same sample, and both must fire.**
The tutorial fires `hey` on boyfriend and `cheer` on dad together at 18,600 ms,
and philly-nice does the same. A single pending slot silently dropped the first.
The module now keeps a small queue; measured across all 27 charts the most that
ever pile up on one sample is 2, so a queue of 4 is generous. This is the one
place where an event is an *action* rather than a *state*: `SetHealthIcon` and
`SetCameraBop` are last-wins, because the original simply applies them in order
and the icon and the bop have one current value each.

The three events that had no port-side state now have one:

* **SetCameraBop** (105 events) sets the bop's intensity, rate and offset,
  replacing the hardcoded `1.015` and every-16-steps. milf's first is
  `{intensity: 2.5, rate: 1}`, which the original turns into an intensity of
  `(1.015 - 1) * 2.5 + 1 = 1.0375` firing every 4 steps instead of every 16.
  Its second, `{intensity: 1, rate: 4}`, is the documented reset and lands back
  on the defaults.
* **SetHealthIcon** (15 events, all in spaghetti) sets the icon's character,
  flip flag and id. Fourteen target the opponent and name an SSERAFIM member;
  the fifteenth, sharing a sample with one of them, is `{char: 0, flipX: true,
  id: 'bf'}`.
* **PlayAnimation** (32 events) is queued and reported. The tutorial's packs
  have no `hey` or `cheer` frame to show, so the port emits a telemetry event
  rather than dropping it silently -- the place it becomes visible is a song
  whose packs actually carry those animations.

`main.c` keeps its own event loop and its telemetry, and calls
`chart_events_apply()` per event, so the diff is one call site rather than a
rewritten pump. The tween advance and the bop decay moved out of the draw block
into `chart_events_tick()`, and the duplicate `fnf_elastic_in_out` /
`fnf_expo_in` copies in main.c were deleted -- two implementations of the same
curve is how the wrong values got in before.

`test/test_chart_events.c` also reproduces main.c's exact call shapes with the
same variable types, against the real headers, because main.c itself cannot be
compiled here. If a signature drifts, that is where it is caught before the
user's build breaks.

## Per-event mapping

Every parameter in the survey, and where it goes. Nothing is dropped.

| event | p0 | p1 | p2 | a | b | ref |
|---|---|---|---|---|---|---|
| `FocusCamera` | duration | x | y | char | ease, easeDir | — |
| `ZoomCamera` | duration | zoom | — | mode | ease, easeDir | — |
| `SetCameraBop` | intensity | offset | rate | — | — | — |
| `PlayAnimation` | — | — | — | target | force | anim |
| `SetHealthIcon` | — | — | — | char | flipX | id |
| `ScrollSpeed` | duration | scroll | — | strumline | ease, absolute | — |
| `ChangeCharacter` | — | — | — | char | — | — |
| `AltIdleAnimation` | — | — | — | — | — | anim |
| `sserafimDark` | amount | duration | — | — | — | — |
| `sserafimLights` | amount | duration | — | — | — | — |
| `sserafimGuitarVibration` | duration | — | — | — | — | — |
| `sserafimFlash` | duration | — | — | — | — | — |
| `sserafimCover` | visible | — | — | — | — | — |
| `sserafimKick` | final | — | — | — | — | — |
| `sserafimBeautiful` | beautiful | — | — | — | — | — |
| `sserafimSing` | — | — | — | 6-bit mask | — | — |
| `sserafimShow` | — | — | — | 5-bit mask | — | — |
| `sserafimPulseLights` | enabled | — | — | — | — | block |
| `sserafimEnd` | — | — | — | — | — | — |

Integral parameters (`char`, `mode`, `target`, `strumline`, `offset`, `rate`,
`force`, `flipX`, `absolute`, masks) are stored raw. Fractional ones
(`duration`, `x`, `y`, `zoom`, `intensity`, `scroll`, `amount`, and every
block element) are stored as fixed-point x1000, matching v3.

`ease` is an index, not a string, because the port has to *evaluate* it. The
name travels in the string table for the record and for anything that has to
display it.

## Compatibility

The loader reads both. Magic `FCH3` → v3 strides, magic `FCH4` → v4 strides.
The converter emits v4 by default and v3 with `--v3`. This matters because the
port already loads FCH3 on the SCPH-90006 and that path stays proven while v4
is brought up beside it.

## Cost

| | v3 | v4 |
|---|---|---|
| event record | 16 B | 32 B |
| worst chart (`spaghetti-easy`, 468 events) | 7,488 B | 14,976 B |
| extra static RAM | — | 7,488 B |
| string + block tables | — | a few hundred B |

7,488 B of static RAM on a port that already budgets ~27 KB of chart payload
is affordable, and it buys a lossless chart. The alternative — a side table of
lookup data keyed by event index — costs the same RAM and cannot be validated
by the loader.

## What this does not solve

The 84 `sserafim*` events are still *dispatched by a script*. v4 carries their
arguments faithfully; it does not implement what they do. That is the `.hxc`
interpreter, which is separate work and is now the only thing standing between
the sserafim week and fidelity. Everything else in the game — 1,026 of the
1,110 events — is fully representable as of this change.

## What the implementation found

`tools/test_fch4.py` round-trips all 27 charts x 3 difficulties:

```
charts converted:      27 x 3 difficulties
events checked:        3330
strings interned:      126 (across all files)
parameter blocks:      72
unrepresentable:       0
ease names seen:       13 of the 13 expected
```

Three things were wrong in the first cut and only the round-trip test caught
them:

1. **The ease index pointed at a fixed list, not the file's string table.** An
   ease name the port had never seen would have been unrepresentable without
   rebuilding the port. It is a string-table index now.
2. **Negative camera offsets wrapped.** `FocusCamera`'s `x` is `-120` in real
   charts; stored as a u32 fixed-point it reads back as `4294847.296` unless
   sign-extended.
3. **408 events used the bare-int form.** `FocusCameraSongEvent.handleEvent`
   reads `data.getInt('char')` and falls back to `cast data.value`, so
   `{"e":"FocusCamera","v":1}` *is* `{char: 1}`. That is a third of all
   `FocusCamera` events in the game and it was being encoded as zeroes.
