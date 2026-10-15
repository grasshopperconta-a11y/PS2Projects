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
