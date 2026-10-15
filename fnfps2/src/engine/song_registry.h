/* song_registry - the data-driven song/level list for the port
 *
 * POR QUE ISTO EXISTE
 * O port atual tem UMA musica: o Tutorial. O caminho do chart esta
 * digitado no meio de main.c ("mass:/FNFPS2/assets/test.chart"), os
 * personagens e o palco sao fixos, e a dificuldade nao existe. Para
 * chegar as 28 musicas e as 10 semanas do jogo original, a lista tem
 * de ser dado, nao codigo.
 *
 * Este modulo e C puro, sem nada de PS2: roda no PC dentro de um teste
 * e valida cada id de personagem e de palco contra as tabelas oficiais
 * de bs_dados.h antes de qualquer coisa pisar no console.
 *
 * FONTE DOS DADOS
 *   funkin.data.story.level.LevelRegistry.listBaseGameEntryIds() da as
 *   dez semanas, na ordem: tutorial, week1..week7, weekend1, sserafim.
 *   funkin.data.song.SongData.SongMetadata/SongPlayData/SongCharacterData
 *   dao os campos de cada musica. Os 25 ids de musica confirmados foram
 *   extraidos do fonte v0.8.6 por grep; a semana sserafim traz 3 musicas
 *   cujos ids vem dos assets (funkin.assets @ 9300719), nao do fonte.
 *
 * O que e DERIVADO e precisa de conferencia contra os seus assets esta
 * marcado no comentario de cada entrada em song_registry.c.
 */
#ifndef SONG_REGISTRY_H
#define SONG_REGISTRY_H

#ifdef __cplusplus
extern "C" {
#endif

/* Dificuldades, na ordem de funkin.util.Constants.DEFAULT_DIFFICULTY_LIST_FULL
 * (easy, normal, hard). O port guarda um bitmask. */
#define SR_DIFF_EASY   0x01u
#define SR_DIFF_NORMAL 0x02u
#define SR_DIFF_HARD   0x04u
#define SR_DIFF_ALL    0x07u

#define SR_MAX_SONGS_PER_LEVEL 8
#define SR_MAX_LEVELS 16
#define SR_ID_MAX 32

typedef struct {
    const char *id;            /* "bopeebo" - tambem o nome da pasta em songs/ */
    const char *name;          /* "Bopeebo" - SongMetadata.songName */
    const char *artist;        /* SongMetadata.artist */
    const char *charter;       /* SongMetadata.charter, ou NULL */
    const char *player;        /* SongCharacterData.player  -> "bf" */
    const char *girlfriend;    /* SongCharacterData.girlfriend -> "gf" */
    const char *opponent;      /* SongCharacterData.opponent -> "dad" */
    const char *stage;         /* SongPlayData.stage -> "mainStage" */
    const char *note_style;    /* SongPlayData.noteStyle */
    unsigned char difficulties;/* bitmask SR_DIFF_* */
    unsigned short divisions;  /* SongMetadata.divisions, 96 no ChartEditor */
    float scroll_speed;        /* SongChartData.scrollSpeed[difficulty] */
    unsigned char looped;      /* SongMetadata.looped */
} sr_song_t;

typedef struct {
    const char *id;            /* "week1" */
    const char *name;          /* LevelData.name */
    const char *title_asset;   /* LevelData.titleAsset */
    unsigned long background;  /* LevelData.background, 0xRRGGBB */
    const sr_song_t *songs[SR_MAX_SONGS_PER_LEVEL];
    unsigned char song_count;
    unsigned char visible;     /* LevelData.visible */
} sr_level_t;

/* ---------------------------------------------------------------- */
/* acesso */

unsigned int sr_level_count(void);
const sr_level_t *sr_level(unsigned int index);
const sr_level_t *sr_level_by_id(const char *id);
const sr_song_t *sr_song_by_id(const char *id);
const sr_song_t *sr_level_song(const sr_level_t *level, unsigned int index);
unsigned int sr_song_count(void);

/* ---------------------------------------------------------------- */
/* caminhos. O port grava o que o Butterscotch converte; a convencao e
 *   <root>/songs/<id>/<difficulty>.chart    (FCH3, ver tools/fnf_to_fch3.py)
 *   <root>/songs/<id>/Inst.pcm              (s16le estéreo 48 kHz)
 *   <root>/songs/<id>/Voices-<player|opponent>.pcm
 *   <root>/songs/<id>/<player|gf|opponent>.pack  (pacote de quadros)
 * Escreve sempre com terminacao NULA. Devolve o numero de caracteres
 * que seriam escritos (como snprintf), ou -1 se nao couber. */
int sr_path_chart(char *out, unsigned int cap, const char *root,
                  const sr_song_t *song, const char *difficulty);
int sr_path_inst(char *out, unsigned int cap, const char *root,
                 const sr_song_t *song);
int sr_path_voices(char *out, unsigned int cap, const char *root,
                   const sr_song_t *song, const char *who);
int sr_path_char_pack(char *out, unsigned int cap, const char *root,
                      const sr_song_t *song, const char *character_id);

/* ---------------------------------------------------------------- */
/* validacao. Devolve 0 se tudo certo, ou o numero de problemas
 * encontrados. Se 'report' nao for NULL, cada problema e impresso la
 * com uma linha. Usa as tabelas oficiais de bs_dados.h. */
int sr_validate(void (*report)(const char *fmt, ...));

#ifdef __cplusplus
}
#endif
#endif
