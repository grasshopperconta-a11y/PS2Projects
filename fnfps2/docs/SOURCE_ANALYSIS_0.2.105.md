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

## 8. All 27 charts converted, and what the events reveal (2026-10-15)

With the real charts in hand, `run_tests.sh` now converts all 81
(27 songs x 3 difficulties) and loads every one through the port's real loader.

```
== real charts -> FCH3 -> real loader ==
  scanned 81 charts (0 unreadable)
  max notes    1035  (limit 1280)  2hot-hard.chart
  max bpm        12  (limit   16)  monster-easy.chart
  max sections  104  (limit  512)  guns-easy.chart
  max events    468  (limit  512)  spaghetti-easy.chart
  all 81 charts load in the real loader
```

### 8.1 The note limit was too small -- 2hot would not load

The comment in `tutorial_chart.c` claimed the biggest real chart was 2hot with
906 notes. That was the **normal** difficulty. `2hot-hard` has **1.035 notes**,
which exceeded `CHART_MAX_NOTES = 1024` and made the loader return -5: the
hardest chart in the game silently failed to load.

Both limits were raised together -- `CHART_MAX_NOTES` in the loader and
`TUTORIAL_MAX_NOTES` in `main.c`, which guards the per-note state array and
would otherwise have skipped the notes past 1024 without a word. The four
limits moved into `tutorial_chart.h` so `test/test_chart_limits.c` can check
them against every chart and name the song that breaches one.

### 8.2 Event inventory across all 27 charts

| Event | Count | Primary parameter |
|---|---|---|
| `FocusCamera` | 664 | `char` (0 = BF, 1 = opponent) |
| `ZoomCamera` | 207 | `zoom` |
| `SetCameraBop` | 105 | `intensity` |
| `PlayAnimation` | 32 | `anim` / `target` |
| `SetHealthIcon` | 15 | `char`, `flipX`, `id` |
| `sserafim*` (10 kinds) | 84 | varies |
| `ScrollSpeed` | 1 | `scroll` |

Three shapes appear for the value field: a **dict** of named parameters (the
documented v2 form), a **bare int** (older charts use `"v": 1` for
`FocusCamera`, meaning the char), and the legacy **positional list**. The
converter now accepts all three and no longer crashes on any of them.

### 8.3 What this says the port still has to implement

This is the honest part. The port currently acts on three event types:

| id | Event | Port behaviour |
|---|---|---|
| 1 | `FocusCamera` | `g_tut_cam_focus = (value != 0)` |
| 2 | `ZoomCamera` | `g_tut_zoom_to = (value & 0xFFFF) / 1000` |
| 4 | `ScrollSpeed` | `g_tut_scroll_to = (value & 0xFFFF) / 1000` |

Everything else converts with an id and is ignored. Specifically:

- **`FocusCamera` carries more than a boolean.** 528 of the 664 also have `x`,
  `y`, `duration`, `ease` and `easeDir` -- a camera that moves to a point over
  time. The port only switches focus between the two characters.
- **`SetCameraBop` (105 events)** overrides the beat bop. The port hardcodes
  `TUT_BOP_INTENSITY 1.015` from the step counter, which is the *default* the
  events replace.
- **`SetHealthIcon` (15 events)** swaps the health icon. The port's HUD has
  icons but nothing drives the swap.
- **The 84 `sserafim*` events** come from that week's `.hxc` scripts. The plan
  already anticipated this ("scripts `.hxc` interpretados"); it needs a small
  interpreter, not a table.
- **`PlayAnimation` (32 events)** is currently redundant: the port derives the
  sing animations from note hits, which happens to agree for the Tutorial but
  is not the same mechanism.

### 8.4 The FCH3 event record cannot carry these faithfully

An event is 16 bytes: `sample | type | value | order`, with `value` a single
u32. That holds one fixed-point parameter plus a duration. It cannot hold
`{intensity, offset, rate}`, `{anim, force, target}` or `{char, flipX, id}`.

So the conversion today is lossy for exactly those events, and pretending
otherwise would be worse than saying so. Carrying them properly means an FCH3
v4 with a wider event record (two value words, or a small parameter block).
That is a format change to a container the port already loads on hardware, so
it is a decision to take deliberately rather than something to slip in -- and
it is the next real piece of work, not a footnote.

## 9. The stage data: 3 errors in the recovered table (2026-10-15)

All 21 stage JSONs came down from the same Drive folder as the songs.
`tools/check_bs_dados.py` parses `bs_stages[]` and compares every field against
them. The result was not clean:

```
bs_dados.h: 21 stages, JSON: 21 stages
mismatches: 3 of 21
```

The three are all `*Erect` variants, and every one of them looks like a copy
of the base stage that was hand-edited and got edited wrongly:

| stage | field | bs_dados.h had | the game has |
|---|---|---|---|
| `schoolEvilErect` | gf position | `[724, 763]` | `[724, 823]` |
| `spookyMansionErect` | cameraZoom | `1.25` | `1.0` |
| `spookyMansionErect` | bf position | `[989.5, 885]` | `[1250, 885]` |
| `tankmanBattlefieldErect` | gf position | `[660.5, 730]` | `[800.5, 775]` |

`schoolEvilErect` had inherited `schoolEvil`'s gf y. `spookyMansionErect` had
`mainStage`'s zoom *and* bf x. `tankmanBattlefieldErect` had inherited
`tankmanBattlefield`'s gf. All four values are now corrected, and the checker
runs in `run_tests.sh` so the table cannot silently drift again.

The other 17 stages agree exactly, including every fractional position
(`989.5`, `751.5`, `800.5`), so the extraction was sound -- it just needed
checking rather than trusting.

### 9.1 What the recovered table does not carry

`bs_stages[]` holds `cameraZoom` and the three character slots. The JSON also
holds **169 stage props** across the 21 stages -- background layers each with
their own position, scale, parallax `scroll` factor and `zIndex`.

`main.c` compresses that into one window and one scroll factor:

```c
#define STAGE_SCROLL (0.9f)
#define STAGE_WIN_X  (88.3500f)
#define STAGE_WIN_Y  (78.9000f)
#define STAGE_WIN_W  (1427.3000f)
#define STAGE_WIN_H  (859.2000f)
```

Measured against `mainStage.json` plus the real PNGs:

| layer | position | scale | scroll | image |
|---|---|---|---|---|
| `stageBack` | `[-600, -200]` | `1.0` | `0.9` | 2560x1400, 1 channel |
| `stageFront` | `[-650, 600]` | `1.1` | `0.9` | 2560x581, 4 channels |
| `stageCurtains` | `[-500, -300]` | `0.9` | **1.3** | 2560x1400, 4 channels |

The union of those three is `(-650, -300)` to `(2166, 1239.1)` -- 2816 x 1539.1
world units -- and it uses **two** scroll factors, not one.

So two things are true and neither is fixed by this pass:

1. `STAGE_SCROLL 0.9` is the back/front factor. The curtains use `1.3`, and
   `STAGE_WIN_W/H` do not equal the props union in either axis (2816/1427.3 is
   not 1539.1/859.2), so the port's window is *some* sub-rectangle of the
   stage, not the whole stage. What rectangle it is, and why, is not recorded
   anywhere I can check, so **`STAGE_WIN_*` is unverified** -- flagged rather
   than guessed at.
2. The port draws one composited 512x256 texture. The real stage is three
   layers of up to 2560x1400, which is why the VRAM budget's "naive" figure
   for `tankmanBattlefield` (4,783,744 B) was so far over the 1,900,544 B
   available -- those are the real image sizes, not estimates.

`tools/dump_stage_geometry.py` prints the union and the scroll factors for
every stage. It can only compute a complete box for `mainStage` right now,
because it needs each prop's pixel size and the other stages' images are not
downloaded yet. It says so instead of inventing sizes.

### 9.2 The character data WAS findable -- it is in assets/data/characters/

First pass on this was wrong, and worth recording as wrong. The character
folders under `assets/shared/images/characters/<id>/` hold spritemaps and
animation data, so I concluded the gameplay numbers had no JSON to diff
against. They do: `assets/data/characters/<id>.json`, all 46 of them, in the
same Drive mirror.

`tools/check_bs_chars.py` parses `bs_chars[]` and diffs `offsets`,
`cameraOffsets` and `singTime` against every JSON, applying the
`CharacterData.hx` defaults where a JSON omits a field:

```c
DEFAULT_OFFSETS  = [0, 0]     // used for both offsets and cameraOffsets
DEFAULT_SINGTIME = 8.0        // in STEPS, not seconds
```

The result:

```
bs_dados.h: 46 characters, JSON: 46 files
checked 46, mismatches: 0
```

Every one of the 46 characters' `offsets`, `cameraOffsets` and `singTime` in
`bs_dados.h` is exactly what the game's own JSON says. So the character table
is **verified**, not merely trusted -- which is the opposite of what the stage
table deserved and got.

### 9.3 What that confirms about the port's own constants

`singTime` is in **steps**, and `bs_dados.h` carries it as a float for that
reason. `main.c` holds `TUT_SING_MS 1200` and
`TUT_SAMPLES_PER_STEP 7200` at 48 kHz:

```
7200 samples / step / 48000 Hz = 0.150 s per step
8 steps x 0.150 s              = 1.200 s   == TUT_SING_MS 1200
```

The tutorial characters use the default `singTime` of 8 steps, and the port's
`TUT_SING_MS 1200` is exactly that. The constant is right, and now it is
*shown* to be right rather than assumed.

Two things still are not covered by this:

- `cameraOffsets` is applied **twice** in the original. `Stage.hx` adds the
  stage's own `stageCharData.cameraOffsets` on top of the character's, and
  `GameOverSubState.hx` uses the character's alone. `bs_dados.h` carries only
  the character's, and the stage table carries none -- the 3 slots in
  `mainStage.json` have `[-100,-100]`, `[150,-100]`, `[0,0]`, which the port
  approximates with `GF_CAMOFF_X`/`GF_CAMOFF_Y`. Those per-stage values are
  now known but not yet wired in.
- `danceEvery` (default 1.0) and `healthIcon` are in the JSONs and are not in
  `bs_dados.h` at all.

## 10. Where the stage images actually are (2026-10-15)

The 21 stage JSONs are in one folder, but their images are not. There is no
`assets/shared/images/stages/` root in the Drive mirror; the images sit in
scattered folders that also hold unrelated assets, and several exist in more
than one copy.

Measured examples:

| image | copies found | sizes |
|---|---|---|
| `weebSchool.png` | 4 | 2956 / 3517 / 2512 / 1888 B |
| `bgLimo.png` | 2 | 731659 / 501453 B |

The `limo` folder does sit under a `stages`-like parent (`.../1c0kvOB.../limo`),
but that parent holds nothing else, and `weeb/` hangs off a different tree that
also contains `pixelNoteSplash.png` and `pixelNoteHoldCover.png`. So the tree is
fragmented by whatever order the upload happened in.

Consequences for the port:

- `tools/dump_stage_geometry.py` can only compute a complete bounding box for
  `mainStage`, because that is the only stage whose three images are known. It
  says so rather than inventing sizes.
- The three shared images are known and measured: `stageback` 2560x1400
  (1 channel), `stagefront` 2560x581 (4 channels), `stagecurtains` 2560x1400
  (4 channels). Those are the Tutorial's stage, so the Tutorial's geometry is
  fully checkable.
- The VRAM budget still has to treat the other 20 stages' images as unknown.
  The worst case in the budget (`tankmanBattlefield`, 18 props) is therefore
  still an estimate, not a measurement.

Downloading all of them reliably means resolving which copy is the game's for
each of the 169 props. That is doable but it is a job of its own, and it is
recorded here as a gap rather than assumed away.

### 10.1 What the stage images actually cost

`tools/vram_budget.py` measures every stage against the SCPH-90006's texture
budget using the real pixel dimensions in `assets-data/stage-image-sizes.json`
(144 of 149 images measured; 5 remain unmeasured and are reported as gaps, not
guessed). The budget is:

* 4,194,304 B of VRAM on the console;
* 2,293,760 B for the two 640x448 framebuffers;
* 1,630,064 B the port already uploads outside the stage -- the BF and GF frame
  buffers, the 320x307 PSMCT16 HUD, the title textures and the 384x192 font
  atlas, all taken from `src/main.c` rather than estimated;
* which leaves **269,480 B for the stage itself**.

Against that, the measured totals are:

| stage | props at native resolution | factor needed to fit |
|---|---|---|
| sserafim | 323,182,592 B | 1/38 |
| mallXmasErect | 204,800,768 B | 1/32 |
| tankmanBattlefield | 171,072,000 B | 1/32 |
| mallXmas | 172,032,000 B | 1/32 |
| phillyStreetsErect | 269,312,768 B | 1/30 |
| limoRideErect | 222,208,000 B | 1/32 |
| phillyStreets | 215,040,000 B | 1/24 |
| spookyMansionErect | 262,144,000 B | 1/19 |
| mainStageErect | 262,912,000 B | 1/20 |
| limoRide | 188,416,000 B | 1/32 |
| mainStage | 147,456,000 B | 1/20 |
| phillyTrain | 212,992,000 B | 1/17 |
| phillyTrainErect | 212,992,000 B | 1/17 |
| spookyMansion | 262,144,000 B | 1/15 |
| school | 225,280,000 B | 1/16 |
| schoolErect | 225,280,000 B | 1/16 |
| mallEvil | 196,608,000 B | 1/13 |
| tankmanBattlefieldErect | 264,192,000 B | 1/10 |
| phillyBlazin | 229,376,000 B | 1/13 |
| schoolEvil | 262,144,000 B | 1/3 |
| **schoolEvilErect** | **262,656 B** | **1/2 -- the only stage that fits** |

Two things follow, and neither is negotiable by the port.

**The stages cannot be uploaded at their native resolution.** The cheapest
stage that does not fit needs 1,224x more texture memory than exists. Even
`schoolEvil`, the smallest stage with images, is 9.7x over. `schoolEvilErect`
is the sole exception, and only because its props are small.

**`src/main.c`'s stage texture is 512x256** -- line 1153 reports
`(512<<16)|256` for `stagetex`. That is 524,288 B, so the port has already been
downscaling; the table above says by how much, per stage, and that the current
fixed 512x256 is wrong for every stage except the two smallest.

This is the one place where "exactly as the original" and "runs on a PS2" cannot
both hold, and the port has to choose the second. What survives the choice is
the composition, the scroll factors, the parallax between layers and the
camera's behaviour; what does not is the pixel detail of the backdrops.

### 10.2 STAGE_WIN_* does not describe mainStage

`src/main.c` lines 68-71 define `STAGE_WIN_X/Y/W/H` as 88.35, 78.9, 1427.3 and
859.2, with `STAGE_SCROLL` 0.9 on line 67. The draw at line 1549 places the
512x256 stage texture at `320 + STAGE_WIN_X - cx*STAGE_SCROLL + 640*STAGE_SCROLL
- 640` by `180 + STAGE_WIN_Y - cy*STAGE_SCROLL + 360*STAGE_SCROLL - 360`, at a
size of `STAGE_WIN_W x STAGE_WIN_H`.

At the camera's origin that is the rectangle (408.35, 258.9) to (1835.65,
1118.1) on a 640x360 logical screen -- so the camera at rest shows roughly the
top-left sixth of the texture, and the rectangle falls far outside the screen.
`STAGE_WIN_*` is therefore a window into a larger stage, not the stage's bounds.

Three aspect ratios disagree, and none of them is derivable from the others:

| quantity | value | aspect |
|---|---|---|
| the stage texture | 512 x 256 | 2.000 |
| `STAGE_WIN_W x STAGE_WIN_H` | 1427.3 x 859.2 | 1.661 |
| mainStage's union bbox, measured | 2816 x 1539.1 | 1.829 |

A 2.000 texture stretched onto a 1.661 rectangle is a non-uniform scale: the
stage is drawn about 12% wider than it is tall, relative to the image. That is
either a real defect or `STAGE_WIN_*` was fitted to something other than the
measured union. **The values stay unverified. Nothing in the JSON or the
recovered source derives them, so they are not corrected here** -- the port
needs to recompute them from the union bbox once the stage texture is per-stage
rather than a fixed 512x256.

### 10.3 Where the images live

The stage images are not in one folder. They sit in per-week `images/`
directories mixed with unrelated assets, and `assets/shared/images/stages/` does
not exist. The table in `assets-data/stage-image-sizes.json` keys each image by
the stage JSON's `assetPath`, which is the only reliable identifier: several
files exist in multiple copies with different dimensions, and the stage JSON is
what says which one the game reads.

Two copies are worth naming because they differ:

* `limo/bgLimo.png` -- 4096x2048 in `limo/images/`, and 4096x2048 in
  `limo/images/erect/`; the same size, so `limoRide` and `limoRideErect` cannot
  be told apart by size alone.
* `limo/limoDrive.png` -- **2048x2048** in `limo/images/` but **4096x4096** in
  `limo/images/erect/`. `limoRideErect` references `limo/erect/limoDrive`, so it
  is the 4096x4096 copy. Picking the wrong one would quadruple that layer.

The 169 props across the 21 stages resolve to 144 distinct images.

### 10.4 The display scale, taken from the original itself

The user asked how the original behaves when the window is resized, so that the
PS2's scale could be computed the same way. v0.8.6 answers this directly:
`source/Main.hx` line 196 sets `FlxG.scaleMode = new FullScreenScaleMode()`, and
`source/funkin/ui/FullScreenScaleMode.hx` contains the arithmetic.
`tools/ps2_display.py` reimplements it.

The two functions that matter are `updateGameSize()` and `updateScaleOffset()`:

    gameRatio   = FlxG.width / FlxG.height          // 1280 / 720 = 1.7778
    screenRatio = Width / Height                    // the window
    ratioAxis   = screenRatio < gameRatio ? Y : X    // letterbox or pillarbox

    if ratioAxis == Y:                              // window narrower than the game
        gameSize.x   = Width                        // use the window's full width
        logicalSize.y = ceil(gameSize.x / gameRatio)
        gameSize.y   = logicalSize.y
    else:                                           // window wider than the game
        gameSize.y   = Height                       // use the window's full height
        logicalSize.x = ceil(gameSize.y * gameRatio)
        gameSize.x   = logicalSize.x

    scale.x = deviceSize.x / FlxG.width
    scale.y = deviceSize.y / FlxG.height
    scale.x = scale.y = min(scale.x, scale.y)       // uniform, never distorts

    offset.x = ceil((deviceSize.x - gameSize.x) * 0.5)   // centred
    offset.y = ceil((deviceSize.y - gameSize.y) * 0.5)

So the game always scales uniformly to fit the window, is centred, and whatever
is left over becomes a black bar. The game's own proportions, and the position
of everything inside it, never change. That is the behaviour to reproduce.

Applied to the console (`src/main.c` draws 640x448 PSMCT32, double buffered):

* `screenRatio` 640/448 = **1.4286**, `gameRatio` 1280/720 = **1.7778**;
* 1.4286 < 1.7778, so `ratioAxis = Y` -- the console is narrower than the game
  and must be letterboxed;
* `gameSize.x = 640`, `logicalSize.y = ceil(640 / 1.7778) = 360`;
* `scale = min(640/1280, 448/720) = 0.5` exactly;
* `offset.y = ceil((448 - 360) * 0.5) = 44`, and 44 px remain at the bottom.

**The game area is 640x360 at a uniform 0.5x, with 44 px black bars top and
bottom.** `src/main.c` already draws exactly this, so the port's display
geometry is correct and needed no change. The scale being a clean 0.5 means
every texture only has to be **half** its original resolution to appear at
precisely the size the original shows it -- same aspect, same position, same
proportions.

### 10.5 Half resolution is the display target, not yet the VRAM answer

`tools/ps2_display.py` also totals each stage at that half resolution, against
the texture budget that is left once the two framebuffers and the textures
`src/main.c` already uploads are taken out:

| stage | native | at 0.5x | against 269,480 B |
|---|---|---|---|
| mallXmasErect | 171,281,364 | 42,826,900 | 159x over |
| sserafim | 161,773,828 | 40,462,188 | 150x over |
| tankmanBattlefield | 155,894,732 | 38,981,800 | 145x over |
| mallXmas | 155,786,080 | 38,950,220 | 145x over |
| limoRideErect | 135,290,240 | 33,824,128 | 126x over |
| phillyStreetsErect | 88,293,592 | 22,086,548 | 82x over |
| limoRide | 81,131,200 | 20,284,768 | 75x over |
| phillyStreets | 73,081,624 | 18,286,160 | 68x over |
| mainStageErect | 61,607,200 | 15,403,952 | 57x over |
| spookyMansionErect | 52,777,216 | 13,194,304 | 49x over |
| school | 44,635,388 | 11,162,820 | 41x over |
| schoolErect | 44,635,388 | 11,162,820 | 41x over |
| phillyTrain | 41,026,576 | 10,262,824 | 38x over |
| phillyTrainErect | 41,026,576 | 10,262,824 | 38x over |
| spookyMansion | 35,410,176 | 8,852,544 | 33x over |
| mainStage | 34,621,440 | 8,657,920 | 32x over |
| mallEvil | 22,815,044 | 5,709,108 | 21x over |
| phillyBlazin | 17,329,044 | 4,339,708 | 16x over |
| tankmanBattlefieldErect | 14,031,824 | 3,509,288 | 13x over |
| schoolEvil | 1,324,128 | 332,428 | 1.2x over |
| **schoolEvilErect** | **1,009,068** | **253,712** | **fits** |

Two conclusions, and they are different in kind.

**0.5x is the right target and the port already has it.** Resizing every
texture to half its original resolution reproduces the original's appearance
exactly at the console's resolution, and the display geometry that does it is
already in `src/main.c`. This part is settled.

**0.5x still does not fit in VRAM, and the gap is 13x to 159x.** The console has
1,900,544 B of texture memory in total. No arrangement of half-resolution
textures fits a stage larger than `schoolEvil`. So the backdrops must be reduced
*further* than their display size, and will be softer on screen than the
original at the same window size. That is the hardware's limit and not a choice
the port gets to make -- but it is a separate, smaller compromise than the one
in 10.1, because 0.5x is now known to be exactly right rather than merely
plausible.

One further saving is available and has not been counted above: the title
textures `src/main.c` uploads -- `(320*240 + 256*235 + 320*192) * 4` =
1,069,888 B -- are only needed on the title screen. Releasing them during
gameplay raises the stage budget from 269,480 B to 1,339,368 B, which brings
`schoolEvil` and `schoolEvilErect` comfortably inside and narrows every other
stage's gap. `vram_cache` and `io_fila` already exist to do this, which is
presumably what the port's own Phase 0 intended: stream the visible part of the
backdrop and let the LRU evict what the camera has left behind.
