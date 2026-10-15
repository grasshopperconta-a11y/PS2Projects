/* Unit test for song_registry: the data-driven song/level list.
 *
 * Build: gcc -O2 -Wall -Wextra -std=gnu11 -Isrc/engine \
 *            test/test_registry.c src/engine/song_registry.c -o test_registry
 *
 * The point of this test is that every character and stage id the registry
 * references must exist in the official tables (bs_dados.h), and that the
 * week grouping matches funkin/InitState.hx exactly.
 */
#include <stdio.h>
#include <string.h>
#include "song_registry.h"

static int failures = 0;
static void check(int cond, const char *what)
{
    if (!cond) { printf("  FAIL: %s\n", what); failures++; }
    else printf("  ok:   %s\n", what);
}

int main(void)
{
    printf("song_registry: structure\n");
    check(sr_level_count() == 10, "ten story levels (LevelRegistry.listBaseGameEntryIds)");

    /* The week order is hard-coded in the original and MUST be preserved. */
    static const char *order[] = {
        "tutorial", "week1", "week2", "week3", "week4",
        "week5", "week6", "week7", "weekend1", "sserafim"
    };
    int order_ok = 1;
    for (unsigned int i = 0; i < 10; i++)
        if (strcmp(sr_level(i)->id, order[i]) != 0) order_ok = 0;
    check(order_ok, "level order matches LevelRegistry.listBaseGameEntryIds()");

    /* Song grouping comes from InitState.hx startSong() lines 519-541. */
    struct { const char *level; const char *songs[5]; int n; } expect[] = {
        { "tutorial",  {"tutorial"}, 1 },
        { "week1",     {"bopeebo", "fresh", "dadbattle"}, 3 },
        { "week2",     {"spookeez", "south", "monster"}, 3 },
        { "week3",     {"pico", "philly-nice", "blammed"}, 3 },
        { "week4",     {"high", "satin-panties", "milf"}, 3 },
        { "week5",     {"cocoa", "eggnog", "winter-horrorland"}, 3 },
        { "week6",     {"senpai", "roses", "thorns"}, 3 },
        { "week7",     {"ugh", "guns", "stress"}, 3 },
        { "weekend1",  {"darnell", "lit-up", "2hot", "blazin"}, 4 },
    };
    int group_ok = 1;
    for (unsigned int i = 0; i < sizeof(expect) / sizeof(expect[0]); i++) {
        const sr_level_t *l = sr_level_by_id(expect[i].level);
        if (!l || (int)l->song_count != expect[i].n) { group_ok = 0; continue; }
        for (int j = 0; j < expect[i].n; j++)
            if (strcmp(l->songs[j]->id, expect[i].songs[j]) != 0) group_ok = 0;
    }
    check(group_ok, "song grouping matches InitState.hx startSong()");

    printf("song_registry: lookups\n");
    const sr_song_t *tut = sr_song_by_id("tutorial");
    check(tut != NULL, "tutorial is findable by id");
    check(tut && strcmp(tut->stage, "mainStage") == 0, "tutorial uses mainStage (proven on hardware)");
    check(tut && strcmp(tut->player, "bf") == 0 && strcmp(tut->opponent, "dad") == 0,
          "tutorial is bf vs dad with gf in the middle");
    const sr_song_t *ugh = sr_song_by_id("ugh");
    check(ugh && strcmp(ugh->player, "pico") == 0, "week7 switches the player to pico");
    check(ugh && strcmp(ugh->stage, "tankmanBattlefield") == 0, "week7 uses tankmanBattlefield");
    check(sr_song_by_id("does-not-exist") == NULL, "unknown id returns NULL");
    check(sr_level_by_id("week9") == NULL, "unknown level returns NULL");
    check(sr_level_song(NULL, 0) == NULL, "NULL level is handled");
    check(sr_song_count() >= 26, "at least the 26 source-confirmed songs are registered");

    printf("song_registry: paths\n");
    char path[256];
    int n = sr_path_chart(path, sizeof(path), "mass:/FNFPS2", tut, "hard");
    check(n > 0 && n < (int)sizeof(path), "chart path fits");
    check(strcmp(path, "mass:/FNFPS2/songs/tutorial/hard.chart") == 0,
          "chart path convention");
    check(sr_path_chart(path, 8, "mass:/FNFPS2", tut, "hard") >= 8,
          "truncated path reports the needed length");
    n = sr_path_inst(path, sizeof(path), "mass:/FNFPS2", tut);
    check(n > 0 && strcmp(path, "mass:/FNFPS2/songs/tutorial/Inst.pcm") == 0,
          "instrumental path convention");
    n = sr_path_voices(path, sizeof(path), "mass:/FNFPS2", tut, "bf");
    check(n > 0 && strcmp(path, "mass:/FNFPS2/songs/tutorial/Voices-bf.pcm") == 0,
          "vocals path convention");
    n = sr_path_char_pack(path, sizeof(path), "mass:/FNFPS2", tut, "bf");
    check(n > 0 && strcmp(path, "mass:/FNFPS2/chars/bf.pack") == 0,
          "character pack path convention");
    check(sr_path_chart(NULL, 10, "x", tut, "hard") < 0, "NULL out is rejected");

    printf("song_registry: validation against the official tables\n");
    int problems = sr_validate(NULL);
    check(problems == 0, "every character and stage id exists in bs_dados.h");

    printf("\n%s (%d failure%s)\n", failures ? "FAILED" : "ALL PASS",
           failures, failures == 1 ? "" : "s");
    return failures ? 1 : 0;
}
