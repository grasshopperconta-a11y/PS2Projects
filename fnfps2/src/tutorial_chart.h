#ifndef TUTORIAL_CHART_H
#define TUTORIAL_CHART_H

#include <tamtypes.h>

typedef struct {
    u32 note_count;
    u32 bpm_count;
    u32 section_count;
    u32 event_count;
    u32 song_end_sample;
    u32 checksum;
    u32 initial_bpm;
} tutorial_chart_info_t;

typedef struct {
    u32 sample;
    u32 type;
    u32 value;
    u32 order;
} tutorial_chart_event_t;

/* Capacity of the loader's static arrays. These are a contract, not an
 * implementation detail: a chart that exceeds any of them is rejected with
 * -5, which is what happened to 2hot-hard (1.035 notes) until 0.2.105 raised
 * the note limit from 1.024 to 1.280. test/test_chart_limits.c asserts these
 * against every converted chart, so lowering one fails loudly instead of
 * silently dropping a song. Keep TUTORIAL_MAX_NOTES in main.c in step with
 * CHART_MAX_NOTES. */
#define CHART_MAX_NOTES 1280u
#define CHART_MAX_BPMS 16u
#define CHART_MAX_SECTIONS 512u
#define CHART_MAX_EVENTS 512u

typedef struct {
    u32 sample;
    u32 duration;
    u8 lane;
    u8 must_press;
    u16 order;
} tutorial_chart_note_t;

int tutorial_chart_load(const char *path, tutorial_chart_info_t *info);
int tutorial_chart_note(u32 index, tutorial_chart_note_t *out);
const tutorial_chart_event_t *tutorial_chart_event(u32 index);
u32 tutorial_chart_step_at(u32 sample);

#endif
