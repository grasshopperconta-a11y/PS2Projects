/* End-to-end check: the converter's output must load in the real loader and
 * must agree with the JSON it came from. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tutorial_chart.h"

static int fails = 0;
static void ck(int c, const char *what)
{
    if (!c) { printf("  FAIL: %s\n", what); fails++; }
    else printf("  ok:   %s\n", what);
}

int main(int argc, char **argv)
{
    tutorial_chart_info_t info;
    int rc;
    if (argc < 3) {
        printf("usage: %s chart.fch3 expected_note_count\n", argv[0]);
        return 2;
    }

    rc = tutorial_chart_load(argv[1], &info);
    if (rc != 0) printf("  loader returned %d\n", rc);
    ck(rc == 0, "the real loader accepts the converted chart");
    printf("  info: %u notes, %u bpms, %u sections, %u events, end=%u, bpm=%u\n",
           info.note_count, info.bpm_count, info.section_count,
           info.event_count, info.song_end_sample, info.initial_bpm);

    /* The expected note count is passed in by run_tests.sh, which reads it
       from the source JSON with a real JSON parser. Parsing JSON in C here
       would be fragile and would test the parser, not the converter. */
    long want = -1;
    if (argc >= 3) want = strtol(argv[2], NULL, 10);
    printf("  source JSON says %ld notes for this difficulty\n", want);
    ck(want > 0 && (long)info.note_count == want,
       "note count matches the source chart JSON");

    ck(info.event_count == 26, "26 events (tutorial-chart.json has 26)");
    ck(info.bpm_count == 1, "1 bpm change");
    ck(info.initial_bpm == 100, "opening bpm is 100");
    ck(info.checksum != 0, "checksum recorded");

    /* the first note is the opponent's left at 9600 ms = 460800 samples */
    tutorial_chart_note_t n;
    ck(tutorial_chart_note(0, &n) == 0, "note 0 readable");
    ck(n.sample == 460800 && n.lane == 0 && n.must_press == 0,
       "note 0 is the opponent's left at 460800 samples");
    ck(n.order == 0, "note 0 order is its index");

    /* every note must be in range, in order, and on a valid lane */
    int ordered = 1, lanes_ok = 1, press_ok = 1;
    u32 prev = 0;
    for (u32 i = 0; i < info.note_count; i++) {
        if (tutorial_chart_note(i, &n) != 0) { ordered = 0; break; }
        if (n.lane > 3) lanes_ok = 0;
        if (n.must_press > 1) press_ok = 0;
        if (n.sample < prev) ordered = 0;
        if (n.sample > info.song_end_sample) ordered = 0;
        prev = n.sample;
    }
    ck(ordered, "notes are sorted and inside the song");
    ck(lanes_ok, "every lane is 0..3");
    ck(press_ok, "must_press is 0 or 1");

    /* the events the port actually acts on */
    int focus = 0, zoom = 0, scroll = 0, unknown = 0, anim = 0;
    for (u32 i = 0; i < info.event_count; i++) {
        const tutorial_chart_event_t *e = tutorial_chart_event(i);
        if (!e) continue;
        if (e->type == 1) focus++;
        else if (e->type == 2) zoom++;
        else if (e->type == 4) scroll++;
        else if (e->type == 3) anim++;
        else if (e->type == 0xFFFF) unknown++;
    }
    printf("  events by type: focus=%d zoom=%d scroll=%d anim=%d unknown=%d\n",
           focus, zoom, scroll, anim, unknown);
    ck(focus + zoom + scroll + anim == (int)info.event_count,
       "every event maps to one of the four loader types");
    /* Counts taken from the source JSON, not assumed:
       {'FocusCamera': 11, 'ZoomCamera': 10, 'PlayAnimation': 4, 'ScrollSpeed': 1} */
    ck(focus == 11, "11 FocusCamera events");
    ck(zoom == 10, "10 ZoomCamera events");
    ck(scroll == 1, "1 ScrollSpeed event");
    ck(unknown == 0, "no UNKNOWN events (every v2 event maps to a loader id)");

    /* the zoom and scroll targets decode the way main.c decodes them */
    float zoom_to = 0.0f, scroll_to = 0.0f;
    for (u32 i = 0; i < info.event_count; i++) {
        const tutorial_chart_event_t *e = tutorial_chart_event(i);
        if (e->type == 2 && zoom_to == 0.0f) zoom_to = (float)(e->value & 0xFFFFu) / 1000.0f;
        if (e->type == 4) scroll_to = (float)(e->value & 0xFFFFu) / 1000.0f;
    }
    ck(zoom_to == 1.3f, "first zoom target is 1.3 (zoom*defaultZoom)");
    ck(scroll_to == 1.2f, "scroll target is 1.2 (scroll 1.2 * chart scrollSpeed 1.0)");

    /* a bad path must fail, not crash */
    ck(tutorial_chart_load("/nonexistent/x.chart", &info) != 0,
       "a missing file fails cleanly");

    printf("\n%s (%d failure%s)\n", fails ? "FAILED" : "ALL PASS",
           fails, fails == 1 ? "" : "s");
    return fails ? 1 : 0;
}
