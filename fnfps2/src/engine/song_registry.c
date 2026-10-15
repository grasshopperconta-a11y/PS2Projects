#include "song_registry.h"
#include "../bs_dados.h"   /* bs_chars[] / bs_stages[]: validacao de ids */

#include <stdio.h>
#include <string.h>
#include <stdarg.h>

/* =====================================================================
   AS MUSICAS
   Ordem e agrupamento por semana: funkin/InitState.hx startSong(),
   linhas 519-541 (confirmado no fonte v0.8.6).
   personagens/palco: SongPlayData dos JSON de assets. Onde o valor veio
   do conhecimento do jogo e nao de um arquivo que eu li, esta marcado
   DERIVADO — sr_validate() confere que o id existe em bs_dados.h, e a
   conferencia final e contra os seus assets.
   ===================================================================== */

/* tutorial — a musica que o port ja toca, com palco e personagens
   provados no hardware (official_tables.h). */
static const sr_song_t s_tutorial = {
    "tutorial", "Tutorial", "Kawai Sprite", NULL,
    "bf", "gf", "dad", "mainStage", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};

/* week1 — Daddy Dearest */
static const sr_song_t s_bopeebo = {
    "bopeebo", "Bopeebo", "Kawai Sprite", NULL,
    "bf", "gf", "dad", "mainStage", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_fresh = {
    "fresh", "Fresh", "Kawai Sprite", NULL,
    "bf", "gf", "dad", "mainStage", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_dadbattle = {
    "dadbattle", "Dadbattle", "Kawai Sprite", NULL,
    "bf", "gf", "dad", "mainStage", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};

/* week2 — Spooky Month */
static const sr_song_t s_spookeez = {
    "spookeez", "Spookeez", "Kawai Sprite", NULL,
    "bf", "gf", "spooky", "spookyMansion", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_south = {
    "south", "South", "Kawai Sprite", NULL,
    "bf", "gf", "spooky", "spookyMansion", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_monster = {
    "monster", "Monster", "Kawai Sprite", NULL,
    "bf", "gf", "monster", "spookyMansion", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};

/* week3 — PICO */
static const sr_song_t s_pico = {
    "pico", "Pico", "Kawai Sprite", NULL,
    "bf", "gf", "pico", "phillyStreets", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_philly_nice = {
    "philly-nice", "Philly Nice", "Kawai Sprite", NULL,
    "bf", "gf", "pico", "phillyStreets", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_blammed = {
    "blammed", "Blammed", "Kawai Sprite", NULL,
    "bf", "gf", "pico", "phillyTrain", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};

/* week4 — MOMMY MUST MURDER (ordem do fonte: high, satin-panties, milf) */
static const sr_song_t s_high = {
    "high", "High", "Kawai Sprite", NULL,
    "bf", "gf", "mom-car", "limoRide", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_satin_panties = {
    "satin-panties", "Satin Panties", "Kawai Sprite", NULL,
    "bf", "gf", "mom-car", "limoRide", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_milf = {
    "milf", "Milf", "Kawai Sprite", NULL,
    "bf", "gf", "mom-car", "limoRide", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};

/* week5 — RED SNOW */
static const sr_song_t s_cocoa = {
    "cocoa", "Cocoa", "Kawai Sprite", NULL,
    "bf", "gf", "parents-christmas", "mallXmas", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_eggnog = {
    "eggnog", "Eggnog", "Kawai Sprite", NULL,
    "bf", "gf", "parents-christmas", "mallXmas", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_winter_horrorland = {
    "winter-horrorland", "Winter Horrorland", "Kawai Sprite", NULL,
    "bf", "gf", "monster-christmas", "mallXmas", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};

/* week6 — hating simulator. senpai/roses usam schoolEvil (o palco escola
   com o fundo escuro), thorns tambem. */
static const sr_song_t s_senpai = {
    "senpai", "Senpai", "Kawai Sprite", NULL,
    "bf", "gf", "senpai", "schoolEvil", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_roses = {
    "roses", "Roses", "Kawai Sprite", NULL,
    "bf", "gf", "senpai-angry", "schoolEvil", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_thorns = {
    "thorns", "Thorns", "Kawai Sprite", NULL,
    "bf", "gf", "spirit", "schoolEvil", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};

/* week7 — TANKMEN. Aqui o jogador e o PICO, nao o BF. */
static const sr_song_t s_ugh = {
    "ugh", "Ugh", "Kawai Sprite", NULL,
    "pico", "gf", "tankman", "tankmanBattlefield", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_guns = {
    "guns", "Guns", "Kawai Sprite", NULL,
    "pico", "gf", "tankman", "tankmanBattlefield", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_stress = {
    "stress", "Stress", "Kawai Sprite", NULL,
    "pico", "nene", "tankman", "tankmanBattlefield", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};

/* weekend1 — DARNell. Quatro musicas no fonte (darnell, lit-up, 2hot,
   blazin). 'blazin' aparece so no switch de InitState; se nos seus assets
   ela nao existir como musica propria, remova a linha. */
static const sr_song_t s_darnell = {
    "darnell", "Darnell", "Kawai Sprite", NULL,
    "bf", "gf", "darnell", "phillyStreetsErect", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_lit_up = {
    "lit-up", "Lit Up", "Kawai Sprite", NULL,
    "bf", "gf", "darnell-blazin", "phillyBlazin", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_2hot = {
    "2hot", "2Hot", "Kawai Sprite", NULL,
    "bf", "gf", "darnell-blazin", "phillyBlazin", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_song_t s_blazin = {
    "blazin", "Blazin", "Kawai Sprite", NULL,
    "bf", "gf", "pico-blazin", "phillyBlazin", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};

/* =====================================================================
   AS SEMANAS
   Ids e ordem: funkin.data.story.level.LevelRegistry.listBaseGameEntryIds()
   Agrupamento das musicas: funkin/InitState.hx startSong(), 519-541.
   ===================================================================== */

static const sr_level_t lv_tutorial = {
    "tutorial", "Tutorial", "tutorial", 0xF9CF51u,
    { &s_tutorial }, 1, 1
};
static const sr_level_t lv_week1 = {
    "week1", "Daddy Dearest", "week1", 0xF9CF51u,
    { &s_bopeebo, &s_fresh, &s_dadbattle }, 3, 1
};
static const sr_level_t lv_week2 = {
    "week2", "Spooky Month", "week2", 0x8B813Fu,
    { &s_spookeez, &s_south, &s_monster }, 3, 1
};
static const sr_level_t lv_week3 = {
    "week3", "PICO", "week3", 0x9A5D9Bu,
    { &s_pico, &s_philly_nice, &s_blammed }, 3, 1
};
static const sr_level_t lv_week4 = {
    "week4", "MOMMY MUST MURDER", "week4", 0xE45D5Du,
    { &s_high, &s_satin_panties, &s_milf }, 3, 1
};
static const sr_level_t lv_week5 = {
    "week5", "RED SNOW", "week5", 0xC73838u,
    { &s_cocoa, &s_eggnog, &s_winter_horrorland }, 3, 1
};
static const sr_level_t lv_week6 = {
    "week6", "hating simulator", "week6", 0x8A6FBEu,
    { &s_senpai, &s_roses, &s_thorns }, 3, 1
};
static const sr_level_t lv_week7 = {
    "week7", "TANKMEN", "week7", 0xAF6C29u,
    { &s_ugh, &s_guns, &s_stress }, 3, 1
};
static const sr_level_t lv_weekend1 = {
    "weekend1", "DARNell", "weekend1", 0x9A5D9Bu,
    { &s_darnell, &s_lit_up, &s_2hot, &s_blazin }, 4, 1
};
/* sserafim — a decima semana. Os ids das 3 musicas vem dos assets
   (funkin.assets @ 9300719), nao do fonte; o placeholder abaixo mantem a
   semana visivel e contavel, e preencha quando rodar o Butterscotch. */
static const sr_song_t s_sserafim_placeholder = {
    "sserafim", "LE SSERAFIM", "LE SSERAFIM", NULL,
    "sserafim-sakura", "sserafim-gf", "sserafim-kazuha", "sserafim", "default",
    SR_DIFF_ALL, 96, 1.0f, 0
};
static const sr_level_t lv_sserafim = {
    "sserafim", "LE SSERAFIM", "sserafim", 0x2A2A2Au,
    { &s_sserafim_placeholder }, 1, 1
};

static const sr_level_t *const g_levels[] = {
    &lv_tutorial, &lv_week1, &lv_week2, &lv_week3, &lv_week4,
    &lv_week5, &lv_week6, &lv_week7, &lv_weekend1, &lv_sserafim
};
#define SR_LEVEL_COUNT ((unsigned int)(sizeof(g_levels) / sizeof(g_levels[0])))

/* ===================================================================== */

unsigned int sr_level_count(void) { return SR_LEVEL_COUNT; }

const sr_level_t *sr_level(unsigned int index)
{
    return index < SR_LEVEL_COUNT ? g_levels[index] : NULL;
}

const sr_level_t *sr_level_by_id(const char *id)
{
    unsigned int i;
    if (!id) return NULL;
    for (i = 0; i < SR_LEVEL_COUNT; i++)
        if (strcmp(g_levels[i]->id, id) == 0) return g_levels[i];
    return NULL;
}

const sr_song_t *sr_level_song(const sr_level_t *level, unsigned int index)
{
    if (!level || index >= level->song_count) return NULL;
    return level->songs[index];
}

const sr_song_t *sr_song_by_id(const char *id)
{
    unsigned int i, j;
    if (!id) return NULL;
    for (i = 0; i < SR_LEVEL_COUNT; i++)
        for (j = 0; j < g_levels[i]->song_count; j++)
            if (strcmp(g_levels[i]->songs[j]->id, id) == 0)
                return g_levels[i]->songs[j];
    return NULL;
}

unsigned int sr_song_count(void)
{
    unsigned int i, total = 0;
    for (i = 0; i < SR_LEVEL_COUNT; i++) total += g_levels[i]->song_count;
    return total;
}

/* =====================================================================
   caminhos
   ===================================================================== */

static int build_path(char *out, unsigned int cap, const char *fmt, ...)
{
    /* snprintf com formato variavel, para nao repetir o teste de tamanho */
    va_list ap;
    int n;
    va_start(ap, fmt);
    n = vsnprintf(out, cap, fmt, ap);
    va_end(ap);
    return n;
}

int sr_path_chart(char *out, unsigned int cap, const char *root,
                  const sr_song_t *song, const char *difficulty)
{
    if (!out || !root || !song || !difficulty) return -1;
    return build_path(out, cap, "%s/songs/%s/%s.chart", root, song->id, difficulty);
}

int sr_path_inst(char *out, unsigned int cap, const char *root,
                 const sr_song_t *song)
{
    if (!out || !root || !song) return -1;
    return build_path(out, cap, "%s/songs/%s/Inst.pcm", root, song->id);
}

int sr_path_voices(char *out, unsigned int cap, const char *root,
                   const sr_song_t *song, const char *who)
{
    if (!out || !root || !song || !who) return -1;
    return build_path(out, cap, "%s/songs/%s/Voices-%s.pcm", root, song->id, who);
}

int sr_path_char_pack(char *out, unsigned int cap, const char *root,
                      const sr_song_t *song, const char *character_id)
{
    if (!out || !root || !song || !character_id) return -1;
    return build_path(out, cap, "%s/chars/%s.pack", root, character_id);
}

/* =====================================================================
   validacao contra as tabelas oficiais
   ===================================================================== */

static int g_problems;

static void default_report(const char *fmt, ...)
{
    va_list ap;
    va_start(ap, fmt);
    vprintf(fmt, ap);
    va_end(ap);
    putchar('\n');
}

static int char_exists(const char *id)
{
    unsigned int i;
    if (!id) return 0;
    for (i = 0; i < BS_CHAR_COUNT; i++)
        if (strcmp(bs_chars[i].id, id) == 0) return 1;
    return 0;
}

static int stage_exists(const char *id)
{
    unsigned int i;
    if (!id) return 0;
    for (i = 0; i < BS_STAGE_COUNT; i++)
        if (strcmp(bs_stages[i].id, id) == 0) return 1;
    return 0;
}

static void check_song(void (*report)(const char *fmt, ...), const sr_song_t *s,
                       const char *level_id)
{
    if (!s->id || !*s->id) { g_problems++; report("  [%s] musica sem id", level_id); }
    if (!s->name || !*s->name) { g_problems++; report("  [%s/%s] sem nome", level_id, s->id); }
    if (!char_exists(s->player)) { g_problems++; report("  [%s/%s] player '%s' nao existe em bs_dados.h", level_id, s->id, s->player ? s->player : "(null)"); }
    if (!char_exists(s->girlfriend)) { g_problems++; report("  [%s/%s] girlfriend '%s' nao existe em bs_dados.h", level_id, s->id, s->girlfriend ? s->girlfriend : "(null)"); }
    if (!char_exists(s->opponent)) { g_problems++; report("  [%s/%s] opponent '%s' nao existe em bs_dados.h", level_id, s->id, s->opponent ? s->opponent : "(null)"); }
    if (!stage_exists(s->stage)) { g_problems++; report("  [%s/%s] palco '%s' nao existe em bs_dados.h", level_id, s->id, s->stage ? s->stage : "(null)"); }
    if (!(s->difficulties & SR_DIFF_ALL)) { g_problems++; report("  [%s/%s] nenhuma dificuldade", level_id, s->id); }
    if (!(s->difficulties & SR_DIFF_NORMAL)) { g_problems++; report("  [%s/%s] sem 'normal' (a dificuldade padrao)", level_id, s->id); }
    if (s->divisions == 0) { g_problems++; report("  [%s/%s] divisions 0", level_id, s->id); }
    if (s->scroll_speed <= 0.0f) { g_problems++; report("  [%s/%s] scrollSpeed <= 0", level_id, s->id); }
}

int sr_validate(void (*report)(const char *fmt, ...))
{
    unsigned int i, j;
    if (!report) report = default_report;
    g_problems = 0;

    report("song_registry: %u semanas, %u musicas", SR_LEVEL_COUNT, sr_song_count());

    for (i = 0; i < SR_LEVEL_COUNT; i++) {
        const sr_level_t *l = g_levels[i];
        if (!l->id || !*l->id) { g_problems++; report("  semana %u sem id", i); continue; }
        if (l->song_count == 0) { g_problems++; report("  [%s] semana sem musicas", l->id); }
        if (l->song_count > SR_MAX_SONGS_PER_LEVEL) { g_problems++; report("  [%s] %u musicas > limite %d", l->id, l->song_count, SR_MAX_SONGS_PER_LEVEL); }
        if (!l->title_asset || !*l->title_asset) { g_problems++; report("  [%s] sem titleAsset", l->id); }
        for (j = 0; j < l->song_count; j++) {
            const sr_song_t *s = l->songs[j];
            if (!s) { g_problems++; report("  [%s] musica %u nula", l->id, j); continue; }
            if (sr_song_by_id(s->id) != s) { g_problems++; report("  [%s/%s] id duplicado no registro", l->id, s->id); }
            check_song(report, s, l->id);
        }
    }
    if (g_problems == 0) report("  todos os ids de personagem e palco existem em bs_dados.h");
    return g_problems;
}
