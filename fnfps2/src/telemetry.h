#ifndef FNF_TELEMETRY_H
#define FNF_TELEMETRY_H
#include <tamtypes.h>
int telemetry_init(const char *build_id, const char *elf_path);
void telemetry_event(const char *name, int a, int b);
void telemetry_frame(u32 frame, u64 begin, u64 after_draw, u64 after_vsync,
                     unsigned short pressed, int animation, int animation_frame,
                     int asset_frame, u32 textured_quads, int qwords, int state,
                     int transitions, u32 audio_heard, u32 audio_queued,
                     u32 ring_level, u32 underruns);

/* O log eh continuo, nao um despejo no fim. telemetry_finish() so rodava no
   exit, entao um travamento levava o log inteiro com ele -- que eh exatamente
   o caso em que o log eh necessario. telemetry_flush() escreve o que estiver
   pendente e pode ser chamado a qualquer momento, inclusive a cada quadro. */
void telemetry_flush(void);

/* O que a tela mostra no canto: resultado do init, quadros registrados,
   eventos pendentes, descartes e despejos. Se o log nao abriu, isso eh a unica
   pista que existe -- por isso precisa estar visivel o tempo todo, e nao
   enterrada num arquivo que talvez nao tenha sido criado. */
void telemetry_status(int *result, unsigned int *frames, unsigned int *events,
                      unsigned int *drops, unsigned int *flushes);

/* Uma linha por quadro com o estado completo da maquina de estados. Os campos
   sao inteiros de proposito: o log precisa ser comparavel por diff, e ponto
   flutuante no formato de texto introduce ruido de ultima casa. */
void telemetry_state(u32 frame, int ui_state, int target_state, int selection,
                     int story_level, int story_diff, int transition_frame,
                     int transitions, int transport_state, int audio_started,
                     int audio_playing, int menu_audio_suspended,
                     int chart_status, int tutorial_scene_ready,
                     int tutorial_audio_status, int story_assets_ready,
                     int menu_cache_ready, int title_anim_status,
                     int gf_uploaded, int bf_uploaded, int gf16_uploaded,
                     int story_gf_uploaded, int story_bf_uploaded,
                     int aspect_169, int viewport_360,
                     u32 music_clock, u32 audio_submitted, u32 ring_level,
                     u32 underruns, int audio_fd, int title_audio_fd,
                     int note_hits, int note_misses, int note_combo,
                     int note_score, int note_feedback, int event_cursor);

/* Um evento de E/S de arquivo, com o resultado. Eh aqui que se ve um asset que
   nao abriu, um tamanho que nao bateu, ou uma leitura que devolveu menos. */
void telemetry_io(const char *op, const char *path, long result, long detail);

int telemetry_finish(void);
#endif
