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
