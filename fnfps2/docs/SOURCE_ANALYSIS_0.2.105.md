# FNF PS2 — v0.2.105 source analysis (recovered from Drive)

Recovered 2026-10-15 from Google Drive `FNF for ps2 BETA / workspace / fnfps2`.
Byte-perfect copies now live in `fnfps2/`. This document records what the
source actually is, so the port work does not have to re-derive it.

## Build identity (confirmed)

| item | value |
|---|---|
| toolchain | ps2dev ubuntu-latest, gcc 15.2.0, tar sha `c8e5dedccf62084d…` |
| `PS2DEV` | `/var/tmp/ps2dev-root/ps2dev` (set by `compilar.sh`) |
| flags | `-O2 -G0 -Wall -Wextra -Werror=implicit-function-declaration -std=gnu11` |
| version macro | `-DFNF_PS2_VERSION="0.2.105-aceite-exato"` |
| errors/warnings | 0 / 0 |
| ELF | `fnf_ps2_m84.elf`, 5,089,600 B, sha256 `c6e6d580…` |
| display | physical 640×448, logical 1280×720, NTSC, PSMCT32, double buffer |
| audio | audsrv, pcm s16le stereo 48000 Hz |
| assets | `mass:/FNFPS2/…` (USB mass) |
| console | SCPH-90006 |

`Makefile` links: `-ldraw -lgraph -lpacket -ldma -lmath3d -lpad -laudsrv
-lfileXio -lpatches`; map via `-Wl,-Map`.

## Files

```
fnfps2/src/main.c            155,317 B / 1,586 lines (dense: ~98 B/line)
fnfps2/src/audio_ring.c|h    streaming ring: 256 KB, 32 KB reads, sema-guarded
                            producer thread prio 40, switch/reset/loop, stats,
                            cooperative stop (TerminateThread only as last resort)
fnfps2/src/telemetry.c|h     capture system: 18,000 frame records + 2,048 render
                            events -> mass:/FNFPS2/FNF_COLHEITA.txt (FNV-1a footer)
fnfps2/src/tutorial_chart.c|h  FCH3 loader (see below)
fnfps2/src/bs_dados.h        46 characters + 21 stages, official v0.8.6 data
fnfps2/src/official_tables.h tutorial/mainStage derived constants
fnfps2/src/menu_generated.h  g_menu_frame[5][2][3][3] + idle timeline
fnfps2/src/story_generated.h g_story_uv[8][4]
fnfps2/src/engine/io_fila.c|h    sliced single-owner I/O queue (Phase 0 part)
fnfps2/src/engine/vram_cache.c|h VRAM LRU cache (Phase 0 part)
```

Not yet pulled (all are *derived* artifacts, regenerable from ps2sdk):
`iomanX_irx.c`, `fileXio_irx.c`, `usbd_irx.c`, `usbhdfsd_irx.c`,
`audsrv_irx.c` (≈625 KB of IRX-as-C-arrays) and `title_packs.o` /
`story_packs.o` (2.2 MB / 722 KB of packed frames). These are produced from
the `.irx` modules that the ps2sdk build emits, so they are re-generated, not
hand-maintained.

## State machine (`main()`, lines 1143–1582)

Single `ui_state` integer, hand-written transitions:

| state | screen |
|---|---|
| 0 | Title (intro credits → logo → "PRESS ENTER") |
| 1 | (transition/other) |
| 6 | Main Menu — 5 items, parallax bg, FlxFlicker replica |
| 7 | Story Menu — difficulty + track select, VCR text |
| 8 | **Gameplay — Tutorial only** |

`g_viewport_360 = (ui_state==0||6||7||8)`. Scissor band `SCISSOR_TOPO..
SCISSOR_BASE` for 0,1,6,7,8 (640×360 logical centred in 640×448 with 44 px
bars). START alone never exits; SELECT+START exits; START without SELECT
acts as CROSS (matches the original).

## Gameplay core (state 8) — the proven reference to generalise

Entry (main.c ~1275–1308):
1. `tutorial_scene_load(&stagetex,&tex,&gftex)` — stage/bf/gf packs
2. `tutorial_chart_load("mass:/FNFPS2/assets/test.chart", &info)` — FCH3
3. `audio_ring_start(audio_fd)` — music ring; `music_clock` is the sample clock
4. `g_tutorial_audio_status`, `g_tutorial_chart_status` gate everything

Judging (48 kHz sample domain), `tutorial_notes_update`:

| constant | value | meaning |
|---|---|---|
| `TUTORIAL_NOTE_AHEAD` | 76800 | spawn ahead = 1.6 s |
| `TUTORIAL_NOTE_LATE` | 12000 | despawn late = 0.25 s |
| `TUTORIAL_NOTE_JUDGE_WINDOW` | 7200 | hit window = 150 ms |
| `TUTORIAL_MAX_NOTES` | 1024 | matches `CHART_MAX_NOTES` |

Score: `|Δ|≤2400` → 350 pts (SICK); `≤4800` → 200 (GOOD); else 100 (BAD);
miss (late) → feedback 4; ghost (no note in window) → feedback 5.
Note state: 0 unjudged, 1 hit, 2 missed, 3 opponent-sung.
Opponent notes set `g_gf_sing` and mark state 3 exactly when
`sample >= note.sample`; player hits set `g_bf_sing`.
Health/combo exist (`g_tutorial_note_score/hits/misses/combo`).
`tutorial_note_y(delta) = 26.3f + delta*(0.45f/(48*2))*g_tut_scroll`.

Audio mix (`tutorial_audio_mix_submit`): `STEM_READ_CHUNK` 8192 from the ring
→ mix stem+voices to `AUDIO_READ_CHUNK` 4096 → `audio_play_complete`
(lossless audsrv retry, FIX27).

Per-frame song logic already present and source-referenced:
camera follow `TUT_CAM_LERP 0.040042306`, zoom event elasticInOut
(`fnf_elastic_in_out`, TAU 13.962634016), scroll event expoIn
(`fnf_expo_in`), camera bop `TUT_BOP_INTENSITY 1.015` / decay `0.949951` /
every `TUT_BOP_STEPS 16`, `TUT_SAMPLES_PER_STEP 7200`.
Sing durations from `BF_SING[4][2]` / `GF_SING[4][2]` (official track order
LEFT,DOWN,UP,RIGHT) with `TUT_SING_MS 1200`.

## FCH3 container — confirmed byte-compatible with `tools/fnf_to_fch3.py`

`tutorial_chart.c` validates, in order: magic `FCH3`, `u16@4 == 3` (version),
`u16@6 == 12` (note stride), `u16@20 == 16` (bpm stride), `u16@22 == 8`
(section stride), `u16@24 == 16` (event stride), `u16@18 == 0`, `u16@26 == 0`,
`u32@36 == 0`; counts at `u32@8` notes, `u16@12` bpms, `u16@14` sections,
`u16@16` events; FNV-1a at `u32@28`; song end at `u32@32`; file size must
equal header+payload exactly.

Per-record rules the loader enforces (all satisfied by the converter):
- note: `lane ≤ 3`, `must_press ≤ 1`, **`order == index`**, `sample ≤ end`,
  `duration ≤ end-sample`, non-decreasing sample.
- bpm: `samples_per_step > 0`, `bpm > 0`, `start_sample ≤ end`, strictly
  increasing `start_step`/`start_sample`, first record at (0,0).
- section: `must_hit ≤ 1`, `length_steps > 0`, **`order == index`**, strictly
  increasing `start_step`, first at 0.
- event: `type != 0`, `order == index`, `sample ≤ end`, non-decreasing.
- Capacity: 1024 notes / 16 bpm / 512 sections / 512 events; payload ≤ 24,832 B.
  (Butterscotch measured the 28 official charts: largest 2hot = 906 notes /
  12,632 B; spaghetti = 264 events; tutorial = 55 notes.)

The converter's self test now asserts `order == index`, which is what the
loader checks.

## The hard constraint (from the project's own plan, `docs/PLANO_GERAL_PORT_COMPLETO.md`)

`bs.py plano-cena`: 12 of 21 stages fit the current five fixed texture slots,
**9 do not**. Worst case `tankmanBattlefield`: 3 chars + 10 animated props =
13 slots. Lowering resolution does not create a slot — the shortage is live
texture *count*, not size. Measured VRAM budget on this SCPH-90006:

```
VRAM total ............ 4,194,304 B
two framebuffers ..... 2,293,760 B
left for textures .... 1,900,544 B
upload ................ 37 MB/s -> 524,783 B per frame
```

`engine/vram_cache.c` (LRU, key→address, `vc_pedir`) and `engine/io_fila.c`
(sliced, priority-ordered single-owner USB queue) are already written in pure
C with the disk layer behind function pointers, precisely so they can be
exercised on the PC against the 21 real scenes before touching the console.

## Open decision the project's plan puts to the user

Phase 0 in that plan is a **rewrite of `main.c`** onto the new engine; the
approved Tutorial would be rebuilt on it and must come out identical, with an
offline renderer proving it. The alternative offered was to keep extending the
current `main.c`, which is safer short-term but cannot reach the 9 stages.

This repository's plan (`docs/FNF_PS2_PORT_PLAN.md`) takes the middle path:
keep the proven title/menu/story renderer and audio ring untouched, introduce
`vram_cache`/`io_fila` behind the gameplay scene first, and generalise the
gameplay core out of the single hardcoded Tutorial. That is what the P0 work
packages below implement.

## P0 work packages (updated with confirmed facts)

1. **Generalise the chart layer.** `tutorial_chart_*` → `chart_*` (same FCH3,
   same validation). Remove the single hardcoded `"mass:/FNFPS2/assets/test.chart"`
   and the `TUTORIAL_*` naming; the path comes from a song registry entry.
2. **Generalise the scene layer.** `tutorial_scene_load` takes a song
   descriptor (stage id, character ids, difficulties, note style) instead of
   the fixed tutorial packs; `bs_dados.h` already supplies all 46 characters
   and 21 stages, so this is data-driven from the start.
3. **Generalise the play loop.** `tutorial_notes_update/draw` → `play_*`,
   driven by the chart + song descriptor, keeping the exact judging constants
   and the exact `note_y` formula. Add the Conductor on `music_clock`
   (already the sample clock) with BPM from the chart's first record.
4. **Introduce `vram_cache` for the gameplay scene only**, leaving the proven
   title/menu/story paths on their current fixed slots until the cache is
   proven; then migrate.
5. **Route gameplay asset loads through `io_fila`** with `IO_PRIO_AUDIO`, so
   streaming music is not starved by the (large) pack uploads.
6. **Fix the three carried defects** already logged: level-name alpha 0.7,
   runtime `LEVEL SCORE` label, SongRegistry data flow.

## Engine validation on the PC (2026-10-15)

`fnfps2/test/test_engine.c` builds with the host compiler and passes:

```
gcc -O2 -Wall -Wextra -std=gnu11 -Isrc/engine \
    test/test_engine.c src/engine/vram_cache.c src/engine/io_fila.c -o test_engine
```

Proven about `vram_cache`: residency/hit-miss accounting; LRU eviction picks the
least-recently-used and refreshing a key protects it; `vc_fixar` blocks are never
evicted; a request larger than the whole region fails with `-1`; a region made
entirely of pinned blocks cannot be evicted and correctly fails; and **no two
simultaneously-live textures ever share VRAM under continuous eviction
pressure** (24 requests totalling 1,228,800 B into a 1,048,576 B cache).

Proven about `io_fila`: an audio request enqueued *after* a 64 KB background
write is served first (priority works), the write then drains completely, and a
failing disk surfaces a negative result to the caller.

### The budget number the packer needs

Worst scene `tankmanBattlefield` (3 characters + 10 animated props = 13 live
textures) against the measured 1,900,544 B of texture VRAM:

| layout | bytes | % of budget |
|---|---:|---:|
| naive — 3 stage layers (512×256×4) + 3 chars (320×307×2) + 10 props (256×256×4) | 4,783,744 | 252% |
| packed — 1 stage layer + 3 chars + 10 props in 3 atlases of 4 (256×256×4) | **1,900,160** | **100%** |

So the scene fits, but only with the three stage layers reduced to one and the
ten props packed four-per-atlas. That is the packer's contract, and it is now a
test rather than an estimate. (384 B of headroom — the packer must not pad.)

## Progress log

### 2026-10-15 — song registry (P0 package 1)

`fnfps2/src/engine/song_registry.{h,c}` + `test/test_registry.c`, all passing
under `-Werror`. Replaces the single hardcoded Tutorial song with a data-driven
list. Both the level order and the song grouping were read out of the v0.8.6
source rather than assumed:

- level ids/order: `funkin.data.story.level.LevelRegistry.listBaseGameEntryIds()`
  → tutorial, week1…week7, weekend1, sserafim
- song grouping: `funkin/InitState.hx` `startSong()`, lines 519–541

`sr_validate()` checks every character and stage id against the official
tables in `bs_dados.h`, so a wrong id is a test failure rather than a black
screen on the console.

Registered: **27 songs across 10 levels** — the 26 the source confirms
(tutorial; bopeebo/fresh/dadbattle; spookeez/south/monster; pico/philly-nice/
blammed; high/satin-panties/milf; cocoa/eggnog/winter-horrorland; senpai/roses/
thorns; ugh/guns/stress; darnell/lit-up/2hot/blazin) plus one sserafim
placeholder.

Asset path convention now fixed (and tested):
```
<root>/songs/<id>/<difficulty>.chart   FCH3, see tools/fnf_to_fch3.py
<root>/songs/<id>/Inst.pcm             s16le stereo 48 kHz
<root>/songs/<id>/Voices-<bf|dad>.pcm
<root>/chars/<character>.pack
```

### Needs from your assets (funkin.assets @ 9300719)
1. **The three sserafim song ids.** They are not in the source, only in the
   level JSON. Replace `s_sserafim_placeholder` and set `lv_sserafim.song_count`.
2. **Confirm the derived `stage`/`player`/`girlfriend`/`opponent` per song.**
   These came from the game's known layout, not from a file I read. The ids are
   all valid (the test proves that), but e.g. whether `roses` uses `senpai-angry`
   and whether week4's order is `high, satin-panties, milf` (as the source's
   switch lists them) should be checked against the real metadata. If your
   Butterscotch already emits these, send me its output and I will replace the
   table wholesale.
3. **Per-difficulty `scrollSpeed` and which difficulties each chart has.**
   The registry currently assumes easy/normal/hard at 1.0 for every song.

## 6. Song registry: the real data (2026-10-15)

The registry is no longer transcribed by hand. `tools/gen_song_registry.py`
renders `src/engine/song_registry_data.inc` from the JSON the user took out
of their installed copy (`fnfps2/assets-data/`), and `test/run_tests.sh` runs
the generator with `--check` so the committed C can never drift from the
committed JSON. Adding a song is now: drop `<id>-metadata.json` in
`assets-data/songs/`, re-run the generator.

### 6.1 The three questions that were open are answered

| Question | Answer | Source file |
|---|---|---|
| sserafim song ids | one song: `spaghetti` | `levels/sserafim.json` -> `"songs"` |
| stage + characters per song | see the table below | `songs/<id>-metadata.json` -> `playData` |
| scrollSpeed | **not a song field** | `songs/<id>/charts/<difficulty>.json` -> `scrollSpeed` |

`divisions` is also a chart field, not a song field: `Song.hx` has
`DEFAULT_DIVISIONS:Null<Int> = null` and does
`difficulty.divisions = metadata.divisions`. The registry used to carry a
fabricated `divisions = 96` and `scroll_speed = 1.0f`; both are gone.

### 6.2 Authoritative week grouping

`funkin.ui.story.Level.getSongs()` returns `_data.songs.copy()` -- the JSON
array, **in JSON order** -- and `InitState.startLevel()` does
`playlistSongIds.shift()` off the front. So the level JSON is the play order.

The `switch` in `InitState.startSong()` (`case 'high' | 'satin-panties' |
'milf':`) is a **set membership test**, not a sequence. Reading it as an order
is what made me write week4 as high/satin-panties/milf; the JSON says
**satin-panties, high, milf**. Corrected.

| Week | Display name | Background | Songs, in play order |
|---|---|---|---|
| `tutorial` | TEACHING TIME | `#F9CF51` | `tutorial` |
| `week1` | DADDY DEAREST | `#F9CF51` | `bopeebo`, `fresh`, `dadbattle` |
| `week2` | SPOOKY MONTH | `#F9CF51` | `spookeez`, `south`, `monster` |
| `week3` | PICO | `#F9CF51` | `pico`, `philly-nice`, `blammed` |
| `week4` | MOMMY MUST MURDER | `#F9CF51` | `satin-panties`, `high`, `milf` |
| `week5` | RED SNOW | `#F9CF51` | `cocoa`, `eggnog`, `winter-horrorland` |
| `week6` | HATING SIMULATOR FT. MOAWLING | `#F9CF51` | `senpai`, `roses`, `thorns` |
| `week7` | TANKMAN FT. JOHNNYUTAH | `#F9CF51` | `ugh`, `guns`, `stress` |
| `weekend1` | DUE DEBTS | `#413CAE` | `darnell`, `lit-up`, `2hot`, `blazin` |
| `sserafim` | LE SSERAFIM | `#F9CF51` | `spaghetti` (capsule: SP. COLLAB 1) |

### 6.3 Every song, from its own metadata

| Song | Week | Player | Girlfriend | Opponent | Stage | BPM | Notes |
|---|---|---|---|---|---|---|---|
| `tutorial` | tutorial | `bf` | **--** | `gf` | `mainStage` | 100 | **no gf slot** |
| `bopeebo` | week1 | `bf` | `gf` | `dad` | `mainStage` | 100 | var: erect, pico |
| `fresh` | week1 | `bf` | `gf` | `dad` | `mainStage` | 120 | var: erect, pico |
| `dadbattle` | week1 | `bf` | `gf` | `dad` | `mainStage` | 180 | var: erect, pico |
| `spookeez` | week2 | `bf` | `gf` | `spooky` | `spookyMansion` | 150 | var: erect, pico |
| `south` | week2 | `bf` | `gf` | `spooky` | `spookyMansion` | 165 | var: erect, pico |
| `monster` | week2 | `bf` | `gf` | `monster` | `spookyMansion` | 95 | - |
| `pico` | week3 | `bf` | `gf` | `pico` | `phillyTrain` | 150 | var: erect, pico |
| `philly-nice` | week3 | `bf` | `gf` | `pico` | `phillyTrain` | 175 | var: erect, pico |
| `blammed` | week3 | `bf` | `gf` | `pico` | `phillyTrain` | 165 | var: erect, pico |
| `satin-panties` | week4 | `bf-car` | `gf-car` | `mom-car` | `limoRide` | 110 | var: erect |
| `high` | week4 | `bf-car` | `gf-car` | `mom-car` | `limoRide` | 125 | var: erect |
| `milf` | week4 | `bf-car` | `gf-car` | `mom-car` | `limoRide` | 180 | - |
| `cocoa` | week5 | `bf-christmas` | `gf-christmas` | `parents-christmas` | `mallXmas` | 100 | var: erect, pico |
| `eggnog` | week5 | `bf-christmas` | `gf-christmas` | `parents-christmas` | `mallXmas` | 150 | var: erect, pico |
| `winter-horrorland` | week5 | `bf-christmas` | `gf-christmas` | `monster-christmas` | `mallEvil` | 159 | - |
| `senpai` | week6 | `bf-pixel` | `gf-pixel` | `senpai` | `school` | 144 | **pixel notes**; var: erect, pico |
| `roses` | week6 | `bf-pixel` | `gf-pixel` | `senpai-angry` | `school` | 120 | **pixel notes**; var: erect, pico |
| `thorns` | week6 | `bf-pixel` | `gf-pixel` | `spirit` | `schoolEvil` | 190 | **pixel notes**; var: erect |
| `ugh` | week7 | `bf` | `gf-tankmen` | `tankman` | `tankmanBattlefield` | 160 | var: erect, pico |
| `guns` | week7 | `bf` | `gf-tankmen` | `tankman` | `tankmanBattlefield` | 185 | var: pico |
| `stress` | week7 | `bf-holding-gf` | `pico-speaker` | `tankman` | `tankmanBattlefield` | 178 | var: pico |
| `darnell` | weekend1 | `pico-playable` | `nene` | `darnell` | `phillyStreets` | 155 | var: bf, erect |
| `lit-up` | weekend1 | `pico-playable` | `nene` | `darnell` | `phillyStreets` | 176 | var: bf |
| `2hot` | weekend1 | `pico-playable` | `nene` | `darnell` | `phillyStreets` | 182 | - |
| `blazin` | weekend1 | `pico-blazin` | `nene` | `darnell-blazin` | `phillyBlazin` | 180 | - |
| `spaghetti` | sserafim | `sserafim-sakura` | `sserafim-gf` | `sserafim-kazuha` | `sserafim` | 111.5 | - |

### 6.4 What the corrections cost

Entries that were wrong before the JSON arrived, and what they are now:

- **tutorial**: was `bf / gf / dad`. Actually `bf / -- / gf` -- the Tutorial
  has no girlfriend field at all; the girlfriend *is* the opponent. This also
  confirms the note in `main.c` ("no Tutorial a GF e a oponente").
- **week4 order**: was `high, satin-panties, milf`. Actually `satin-panties,
  `high, milf`.
- **week4 sprites**: were plain `bf/gf/mom`. Actually `bf-car / gf-car / mom-car`.
- **week7 player**: was `pico`. Actually `bf` (ugh, guns) and `bf-holding-gf`
  (stress). The girlfriend is `gf-tankmen`, and stress puts `pico-speaker` in
  the girlfriend slot.
- **winter-horrorland**: stage `mallEvil`, opponent `monster-christmas` -- not
  mallXmas.
- **noteStyle**: week6 (senpai/roses/thorns) is `pixel`, everything else
  `funkin`. Two different note atlases.
- **sserafim**: one song, `spaghetti`, cast `sserafim-sakura / sserafim-gf /
  `sserafim-kazuha`, stage `sserafim`, 111.5 BPM -- a fractional bpm, so the
  registry stores it as a float and the test asserts it exactly.

### 6.5 Level metadata the story menu needs

`Level.getTitle()` -> `_data.name`; `getBackgroundColor()` ->
`FlxColor.fromString(_data.background)`; `buildProps()` places prop *i* at
`propData.offsets[0] + FlxG.width * 0.25 * i` (1280 * 0.25 = 320 px apart).
`getDifficulties()` takes the first song's difficulties and keeps only those
present in **every** song of the week. All ten weeks ship easy/normal/hard,
so that reduces to the usual three.

Only `weekend1` differs in background (`#413CAE`); the rest are `#F9CF51`.
Only `sserafim` has a capsule (`SP. COLLAB 1`).

## 7. Real chart conversion, and the two bugs only real data found (2026-10-15)

The converter had only ever been run on charts I wrote myself, which is exactly
why two defects survived in it. Converting `tutorial-chart.json` -- the real
file from the installed game -- broke immediately, and then again, and the
second break was found by the port's own loader rather than by me.

### 7.1 The v2 chart format, as it actually is

```json
{
  "version": "2.0.0",
  "scrollSpeed": {"easy": 1, "normal": 1, "hard": 1},
  "notes": { "easy": [...], "normal": [...], "hard": [...] },
  "events": [ {"t": 9600, "e": "FocusCamera", "v": {"char": 1}}, ... ]
}
```

Three things I had wrong:

- **`notes` is a map keyed by difficulty**, not a flat list. The keys are
  `easy`/`normal`/`hard`.
- **A note is `{t, d, l}`** where `t` is milliseconds, `d` is the strumline
  index and `l` is the sustain. `SongNoteDataRaw` documents `d` as
  `0=left, 1=down, 2=up, 3=right` with
  `floor(d / strumlineSize)` selecting the strumline -- 0 = player,
  1 = opponent. So with a strumline of 4, `d` 0-3 are the player's and 4-7 the
  opponent's. The Tutorial's opponent (the GF) sings `d` 4 and 7.
- **`events` carry a dict of named parameters**, not the legacy positional
  `[name, t, v1, v2]`:
  `{"t":9600,"e":"ZoomCamera","v":{"duration":4,"ease":"elasticInOut","zoom":1.3}}`.

There is no `sections` list and no top-level `bpm`: the bpm comes from the
metadata's `timeChanges`, and sections are derived.

### 7.2 Bug 1 -- the event type ids did not match the loader

The converter's table was:

```python
"FocusCamera": 1, "ChangeCharacter": 2, "PlayAnimation": 3, "AltIdleAnimation": 4
```

But `main.c` switches on:

| id | meaning |
|---|---|
| 1 | FocusCamera -- `g_tut_cam_focus = (value != 0)` |
| 2 | **ZoomCamera** -- `g_tut_zoom_to = (value & 0xFFFF) / 1000` |
| 3 | PlayAnimation |
| 4 | **ScrollSpeed** -- `g_tut_scroll_to = (value & 0xFFFF) / 1000` |

There was no mapping for `ZoomCamera` or `ScrollSpeed` at all, so both became
`EVENT_TYPE_UNKNOWN` and the port silently ignored them: the camera would never
zoom and the scroll speed would never change. `ChangeCharacter` and
`AltIdleAnimation` moved to 5 and 6.

The parameter encoding follows the loader: the fixed-point value in the low 16
bits (zoom/scroll x1000), and the event's `duration` in steps in the high 16.
The loader reads only the low half today, so the high half is free.

`ScrollSpeedEvent` honours `absolute`: when false the target is
`scroll * chart.scrollSpeed[difficulty]`. The Tutorial's event is
`{absolute:false, scroll:1.2}` against a chart scrollSpeed of 1.0, so the target
is 1.2 -- which is what `main.c` hardcodes and what the converted chart now
carries.

### 7.3 Bug 2 -- `order` was written as 0

`build_fch3` serialised every note, section and event with `order = 0`. The
loader enforces `order == index` as a corruption check and returns **-9** for a
bad note, -12 for a bad section, -14 for a bad event. Every chart the converter
produced was therefore rejected by the PS2.

This is the failure mode worth remembering: the converter's own selftest passed,
because it asserted `n[4] == 0` -- it encoded the bug as the expected result.
The real loader, not the converter, was the only thing that could catch it, and
the selftest now asserts `order == i` instead.

### 7.4 The end-to-end test

`test/test_real_chart.c` compiles the port's actual loader on the PC against
`test/ps2sdk-shim/tamtypes.h` (the loader is otherwise pure POSIX C; only the
`u8/u16/u32` typedefs come from ps2sdk). `run_tests.sh` converts the real
Tutorial chart at all three difficulties and loads each one:

```
== real chart -> FCH3 -> real loader ==
  easy:   ALL PASS (0 failures)
  normal: ALL PASS (0 failures)
  hard:   ALL PASS (0 failures)
```

Verified on the real Tutorial chart, hard: 71 notes, 1 bpm change (100 bpm,
7200 samples/step), 27 derived sections, 26 events
(11 FocusCamera, 10 ZoomCamera, 4 PlayAnimation, 1 ScrollSpeed), first note the
opponent's left at sample 460800 (9600 ms at 48 kHz), first zoom target 1.3,
scroll target 1.2.
