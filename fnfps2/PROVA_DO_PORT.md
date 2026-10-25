# Prova do port: todas as funções, e a matemática de cada valor

Documento gerado a partir de execução real, não de leitura. Todos os números
aqui foram produzidos por comandos cuja saída está reproduzida no apêndice.

**Data:** 2026-10-25 · **Branch:** `arena/4c50659b-ps2projects`

---

## 1. O que está sendo provado, e com que força

O port são **3.652 linhas de código em 8 arquivos, com 200 funções**.

Os 5 arquivos `*_irx.c` (6.269 linhas) **não são código**: são arrays
`unsigned char audsrv_irx[] = { 0x7f, ... }` com os bytes dos módulos oficiais
do PS2 SDK. São dado, não comportamento, e não entram nesta prova.

As 200 funções se dividem em dois grupos, com **dois tipos de prova
diferentes** — e nenhum dos dois é "eu li e achei que sim":

| Grupo | Funções | Tipo de prova | Resultado |
|---|---|---|---|
| 6 módulos que rodam no PC | 89 | **Execução** com verificação de cobertura por função | 249 checagens, 0 falhas, 0 funções sem executar |
| `main.c` + `telemetry.c` | 111 | **Compilação** completa para o PS2 com `-Wall -Wextra`, mais leitura | 0 warnings, ELF gerada |

A distinção importa. Um teste que passa não prova nada se a função nunca foi
chamada. É por isso que a prova dos 6 módulos usa **gcov por função**: uma
função com 0 linhas executadas **não foi testada**, por mais que o teste
tenha passado.

---

## 2. Como reproduzir

```sh
sh test/rodar-prova.sh
```

O script compila os 6 módulos do port, o shim de host, e o teste; roda; e
imprime a cobertura por função. Saída final:

```
=== 249 checagens, 0 falharam ===
TODAS PASSARAM

funcoes sem nenhuma linha executada: 0  (tem de ser 0)
```

O relatório completo fica em `test/cobertura.txt`.

### Por que 6 módulos e não 8

`main.c` e `telemetry.c` dependem de `ps2sdk` (libmc, libpad, gsKit, audsrv,
lib usbhdfsd). Não compilam no PC — não por escolha, por dependência real de
hardware. A prova deles é a compilação para o PS2:

```sh
sh tools/with_toolchain.sh sh -c 'rm -f src/*.o src/engine/*.o *.elf *.map; ./build.sh'
```

```
    ok   compiled (17s total)
    ok   fnf_ps2_m84.elf is 5271460 bytes (baseline 5,089,600)
done in 17s
```

Zero warnings, com `-Wall -Wextra -Werror=implicit-function-declaration`
ligados no `Makefile`.

### O shim de host, e o que ele assume

`test/host-shim/` implementa `CreateSema/WaitSema/SignalSema/CreateThread/
StartThread/DelayThread` com pthreads de verdade. **O que ele assume está
anotado no próprio `kernel.h`:** os semáforos viram mutex porque o port os usa
exatamente como mutex (contagem 1, máximo 1, opção 0). Se um dia o port usar
semáforo como contador, o shim mente — e o teste que depende disso passa a
valer menos que nenhum.

Um detalhe que o shim teve de acertar: `audio_ring_start_loop` guarda o
`ee_thread_t` **na pilha**. O kernel do PS2 copia a struct; o shim original
guardava o ponteiro, que pendurava no retorno da função e derrubava o
processo. Agora o shim também copia — o que é simultaneamente o conserto e o
comportamento mais fiel ao PS2.

---

## 3. Prova dos 6 módulos (89 funções)

Cobertura por função, de `test/cobertura.txt`:

```
chart_events      21 funções
song_registry     20 funções
audio_ring        15 funções
chart             14 funções
vram_cache        12 funções
io_fila            7 funções
                  ---
                   89 funções
```

**Nenhuma ficou com 0 linhas executadas.** 82 estão em 100% das linhas.
As 5 restantes são parciais, e a razão de cada uma está na seção 6.

```
100% das linhas:  82 funções
parciais:          5 funções
sem executar:      0 funções   <-- tem de ser 0
                  ---
                   89 funções
```

### 3.1 `chart.c` — o carregador (14 funções)

Prova: um chart v3 **montado na mesa**, com checksum calculado por uma
implementação FNV-1a **independente**, escrita no teste. Se as duas baterem,
a do port está certa — não há como duas implementações errarem igual.

Além do caminho feliz, o teste força **cada recusa** do carregador e confere
o código:

| Situação | rc |
|---|---|
| payload corrompido (1 byte) | -8 |
| checksum do cabeçalho corrompido | -8 |
| mágico inválido | -4 |
| `note_count = 0` | -5 |
| caminho inexistente | -1 |
| `path == NULL` | -1 |
| `info == NULL` | **0** (tolerado de propósito) |

E as regras de validação, todas lidas do fonte e exercitadas: nota com
`lane > 3`, `press > 1`, `order != i`, `sample > end`, `duration > end-sample`
ou amostra fora de ordem caem em -9; bpm com `samples_per_step == 0`,
`bpm == 0` ou início fora de ordem cai em -10/-11; seção com `order != i` cai
em -12/-13; evento com `type == 0` ou amostra fora de ordem cai em -14.

Um chart **v4** também é montado, com tabela de strings e de blocos, para
cobrir `chart_fnv1a_more` (o checksum de v4 cobre payload **e** tabelas),
`string_bytes_of` (que caminha os NULs porque o fim dos dados não é gravado)
e os dois acessores de tabela.

### 3.2 `chart_events.c` — as easings e o estado (21 funções)

O mapa de índices foi **lido do switch**, não adivinhado. Numa rodada anterior
eu errei todos os índices e o teste falhou em massa — a lição ficou: a
convenção se lê do fonte.

```
0 CLASSIC   1 INSTANT   2 circ   3 elastic   4 elasticInOut   5 expo
6 expoIn    7 expoOut   8 linear  9 quad     10 quadInOut     11 quart
12 quintInOut
```

Não existe cubic nem sine na tabela. `chart_ease_names[13]` confirma.

A prova usa três propriedades que uma implementação errada sempre quebra:

1. **`f(0) = 0` e `f(1) = 1`** nas 13 curvas — se falhar, a animação começa ou
   termina fora do lugar.
2. **Monotonia não-decrescente** nas 11 curvas não-elásticas. *Elastic é a
   exceção declarada:* passar do alvo e voltar **é** a assinatura da curva, e
   o flixel faz isso de propósito. Exigir monotonia nela seria exigir que
   deixasse de ser elástica. O teste cobra o oposto: o pico do `elasticInOut`
   tem de passar de 1,05.
3. **Valor analítico em `t = 0,5`** para cada curva, contra a fórmula do
   flixel — incluindo a constante `2π/0.45 = 13,962634016` do `elasticInOut`.

Há também a **ida e volta**: os 13 nomes resolvem para o próprio índice.
Se a tabela e o switch divergirem, um chart em texto não carrega igual ao
binário.

### 3.3 `engine/song_registry.c` — o registro (20 funções)

`sr_validate` varre as 10 semanas e 27 músicas e confere: id não-vazio, id não
duplicado, `bpm` finito e positivo, personagem e palco existentes. A prova
exige **0 problemas**, e conta separadamente as linhas de resumo (que não são
problemas — `sr_validate` sempre imprime um cabeçalho e um rodapé).

Os caminhos são conferidos contra o **formato do jogo original**:
`<root>/songs/<id>/<difficulty>.chart`, mais os 4 layouts de pendrive que
`sr_chart_path_at` conhece.

`join_path` tem semântica de `snprintf`: escreve o que cabe, **sempre**
termina em NUL, e devolve o tamanho que a inteira precisaria. O teste fixa os
três comportamentos, porque um chamador com buffer curto precisa de um prefixo
utilizável, não de memória não inicializada.

### 3.4 `engine/vram_cache.c` — o alocador (12 funções)

A convenção que o teste fixou depois de ler o fonte: a tabela começa com **um
bloco que é o buraco livre cobrindo a região inteira**. `n == 1` depois do
`vc_init`, não 0.

`vc_pedir` tem retorno **tri-state**: `1` = acerto, `0` = miss alocado,
`-1` = falhou. E `vc_limpar` **preserva os blocos fixos de propósito** — fonte
e HUD não podem desaparecer no meio de uma música. O teste prova as duas
coisas, inclusive que um bloco fixo sobrevive a despejos sucessivos.

### 3.5 `engine/io_fila.c` — a fila fatiada (7 funções)

A prova aqui não é o resultado, é **a fatia**. `io_bombear` processa **uma**
fatia por chamada: 100 KB = exatamente 4 chamadas de 32 KB. O teste conta.

Também prova: prioridade (áudio passa na frente de fundo, mesmo enfileirado
depois), desempate por selo, fila cheia recusada em `IO_MAX_PEDIDOS`, erro no
disco com resultado negativo, e que `io_resultado` **colhe e libera** — sem
ele a fila nunca esvazia.

### 3.6 `audio_ring.c` — o anel (15 funções)

Esta é a prova mais forte do conjunto: **a thread de produtor roda de
verdade**, via pthread, contra um arquivo real de 256 KB.

A conta que o teste faz: `256 KB / 32 KB = 8` leituras para encher. A saída
confirma:

```
produzidos=262144 lidas=8 loops=0 erros=0 underruns=1
```

262.144 = 256 × 1.024, e `lidas=8` — a conta bate. Também prova `take`
devolvendo a fatia inteira, o nível caindo exatamente o que saiu, `take`
maior que o nível devolvendo 0 e contando underrun, EOF no fim do arquivo,
`reset`, `switch` com loop, e que um segundo `start` não vaza thread.

---

## 4. Prova de `main.c` e `telemetry.c` (111 funções)

Estas **não rodam no PC**. O que se pode provar, e se prova:

1. **Compilam sem um warning** com `-Wall -Wextra` e
   `-Werror=implicit-function-declaration`. Um warning de função implícita
   seria erro de compilação, não aviso.
2. **A ELF é gerada**, com 5.271.460 bytes.
3. **As marcas de diagnóstico estão no binário**, conferidas com `strings`:

```
$ strings -a fnf_ps2_m84.elf | grep -cE '^T_(PAD|AUD|UPD|DRAW|DMA|VSYNC|FB|END)$'
8
```

As 8 marcas `T_*` presentes. A verificação por `strings` é obrigatória antes
de entregar qualquer build: é o que distingue uma ELF real de uma antiga.

As 94 funções de `main.c` e 17 de `telemetry.c` estão listadas no apêndice A.
Elas são a parte que depende de hardware (GS, DMA, USB, pad, audsrv) e cuja
prova final é o console.

---

## 5. A matemática de cada valor

Cada número aqui tem uma origem no jogo original, e a origem está no fonte.

### 5.1 Tempo e passos

| Valor | Matemática | Origem |
|---|---|---|
| `AUDIO_RATE = 48000` | 48 kHz, a taxa do hardware de áudio do PS2 | `main.c:214` |
| `TUT_SAMPLES_PER_STEP = 7200` | `stepLengthMs 150 × 48000 / 1000` = 7200 | `main.c:125` |
| `steps_to_seconds(s)` | `s × samples_per_step / 48000` | `chart_events.c:240` |
| `TUT_DT = 0,016683333` | 1/59,94 — o período de um quadro NTSC | `main.c:84` |
| `CHART_STEPS_PER_BEAT = 4` | `Constants.STEPS_PER_BEAT` | `chart_events.h:60` |

A relação completa: 150 ms por passo ÷ 4 passos por batida = 37,5 ms por
batida = **160 BPM** para o tutorial. O `steps_to_seconds` converte passos em
segundos usando a mesma conta, e é por isso que um evento com duração de 2
passos dá exatamente `2 × 7200 / 48000 = 0,30 s` — conferido no teste.

### 5.2 Batida de câmera (camera bop)

| Valor | Matemática | Origem |
|---|---|---|
| `CHART_DEFAULT_BOP_INTENSITY = 1,015f` | `Constants.DEFAULT_BOP_INTENSITY` | `chart_events.h:57` |
| `CHART_DEFAULT_BOP_RATE = 4,0f` | `Constants.DEFAULT_BOP_RATE` | `chart_events.h:58` |
| `CHART_DEFAULT_BOP_OFFSET = 0,0f` | `Constants.DEFAULT_BOP_OFFSET` | `chart_events.h:59` |
| `CHART_BOP_DECAY = 0,95f` | `PlayState.hx:1217` | `chart_events.h:61` |

`1,015` é o fator de escala por batida: cada batida multiplica o zoom por
1,015 e o decaimento de 0,95 o puxa de volta. `4,0` é em **batidas**, não em
passos — daí os 4 passos por batida de `STEPS_PER_BEAT`.

### 5.3 Easings — as fórmulas exatas

Todas saem do flixel (`FlxEase`). O original monta o **nome** da função e
procura; o port recebe o **índice** que `tools/fnf_to_fch3.py` escreve.

| Curva | In (dir 0) | Out (dir 1) | InOut (dir 2) |
|---|---|---|---|
| CLASSIC / INSTANT | `1,0` | `1,0` | `1,0` |
| linear | `t` | `t` | `t` |
| quad | `t²` | `t(2-t)` | `2t²` / `-1+(4-2t)t` |
| quart | `t⁴` | `1-(1-t)⁴` | `8t⁴` / `1-8(1-t)⁴` |
| circ | `1-√(1-t²)` | `√(1-(1-t)²)` | `-½(√(1-4t²)-1)` / `½(√(1-(2t-2)²)+1)` |
| expo | `2^(10(t-1))` | `1-2^(-10t)` | `½·2^(20t-10)` / `1-½·2^(-20t+10)` |
| quintInOut | — | — | `16t⁵` (t<½) / `1-½(-2t+2)⁵` |
| elasticInOut | — | — | `-½·2^(10u)·sin((u-0,1125)·2π/0,45)`, `u=2t-1` |

A constante do elástico: `2π/0,45 = 13,962634016`. Trocá-la muda a curva
inteira, e o teste a compara contra a fórmula, não contra um valor gravado.

### 5.4 Ponto fixo e eventos

| Valor | Matemática |
|---|---|
| `fx(v)` | `v / 1000,0f` — ponto fixo com 3 casas decimais |
| `ZOOM_CAMERA.p0` | **duração**, em passos |
| `ZOOM_CAMERA.p1` | **zoom**, em fixo ×1000 |
| `ZOOM_CAMERA.a == 1` | multiplica pelo zoom do palco, em vez de substituir |
| `SCROLL_SPEED` sem `CHART_B_ABSOLUTE` | multiplica pelo scroll atual |

**`p0` é a duração e `p1` é o zoom.** Numa rodada anterior eu tinha invertido,
e o teste falhou. Está anotado aqui porque é fácil errar de novo.

Quando `chart_event_string()` devolve NULL (que acontece sempre que
`chart_info.version != 4`), `chart_events_ease_id(NULL)` cai em **8 (linear)**.
Num chart v3, portanto, a ease sempre resolve para linear — que é o default
do original.

### 5.5 Formato do chart

| Campo | v3 | v4 |
|---|---|---|
| Cabeçalho | 40 B | 48 B |
| Stride de evento | 16 B | 32 B |
| Stride de nota / bpm / seção | 12 / 16 / 8 | igual |
| Tabela de strings | não | sim |
| Tabela de blocos | não | sim |

Checksum: **FNV-1a de 32 bits**, base `2166136261`, prima `16777619`, sobre o
payload — e, em v4, sobre as tabelas também (daí `chart_fnv1a_more`).

Layout da cauda em v4, lido do carregador:

```
[string_count × u32 offsets][dados das strings, terminadas em NUL]
[u32 block_count][para cada bloco: u32 tamanho + dados]
```

O fim dos dados das strings **não é gravado**: `string_bytes_of` caminha os
NULs para descobri-lo. Foi exatamente aí que um byte a mais no teste (o NUL
que o compilador põe no fim do literal) deslocou a tabela de blocos e fez o
carregador recusar com -15.

### 5.6 Alinhamento e fatias

| Valor | Matemática | Origem |
|---|---|---|
| `VC_ALINHAMENTO = 256` | `TBP0` do GS conta endereços de textura de 256 em 256 | `vram_cache.h` |
| `VC_MAX_BLOCOS = 128` | despacho por LRU (`selo`) | `vram_cache.h` |
| `IO_FATIA = 32768` | mesmo bloco do anel de áudio | `io_fila.h` |
| `IO_MAX_PEDIDOS = 16` | despacho por prioridade, desempate por selo | `io_fila.h` |
| `RING_SIZE = 256 KB` | `READ_SIZE 32 KB × 8` leituras para encher | `audio_ring.c` |

O alinhamento de 256 cobra um preço medido: um pedido de 300 bytes consome
**512** (2 × 256), não 300. Até 255 bytes de desperdício por textura. O teste
fixa esse número para que uma mudança na regra de alinhamento fique visível.

A fatia de 32 KB tem outra razão de ser, anotada no cabeçalho do `io_fila.c`:
com 37 MB/s medidos no pendrive, cada fatia prende o dispositivo por cerca de
0,9 ms. Uma gravação de 1,1 MB vira 35 fatias, e o áudio se intercala entre
elas em vez de esperar 31 ms. Foi assim que se resolveu a corrupção do
`usbhdfsd` sem deixar o áudio mudo durante a gravação.

---

## 6. O que a prova **não** cobre

Honestidade sobre os limites, porque uma prova que se apresenta como completa
quando não é vale menos que uma prova modesta:

**5 funções ficaram abaixo de 100% das linhas.** Todas foram executadas;
nenhuma teve 0%:

| Função | Cobertura | O que falta |
|---|---|---|
| `chart_load_song_layout` | 87,5% | layouts 1-3 com arquivo real no pendrive |
| `chart_events_tick` | 57,9% | ramos de decaimento do bop ao longo de muitos quadros |
| `chart_events_apply` | 82% | tipos de evento 5-8 (`CHANGE_CHARACTER`, `ALT_IDLE`, `SET_HEALTH_ICON`) |
| `check_song` | 88,2% | ramos de música com problema |
| `vc_pedir` | 82,1% | caminho de "sem descritor livre" |

`ease_expo` chegou a 100% depois que o teste passou a cobrir as guardas de
fronteira (`t<=0` e `t>=1`), que existem porque `2^(10(t-1))` em `t=0` dá
0,5, não 0.

**`main.c` e `telemetry.c` (111 funções) não são provadas por execução.**
Compilam limpo, e as marcas estão no binário, mas o comportamento final
depende do console.

**`maior_espera` é um contador declarado e nunca incrementado.** Ele é zerado
no `io_init` e nada mais o toca. Um diagnóstico que sempre leria 0. O teste
fixa isso de propósito: se alguém passar a usá-lo, o teste quebra e a pessoa
percebe que precisa atualizar a prova.

**A ELF atual é a `0.2.84-calibracao`** (`FNF_VERSION` no `Makefile`), com
5.271.460 bytes e md5 `e27caffcd4f21f947cd619bd20e2437a`. As ELFs de
diagnóstico `0.2.106-f0diag` e `0.2.107-trace` mencionadas em etapas
anteriores eram variantes construídas com `make FNF_VERSION=...`. A
instrumentação de rastro (`T_*`, `BOOT.txt`) continua no fonte e no binário
atual.

---

## Apêndice A — inventário das funções

### Rodam no host (89, provadas por execução)

**`chart.c` (14):** `chart_load`, `chart_load_song`, `chart_load_song_layout`,
`chart_event`, `chart_event_string`, `chart_event_block`, `chart_note`,
`chart_step_at`, `read_exact`, `string_bytes_of`, `chart_fnv1a`,
`chart_fnv1a_more`, `chart_u16`, `chart_u32`

**`chart_events.c` (21):** `chart_events_reset`, `chart_events_init`,
`chart_events_bind`, `chart_events_state`, `chart_events_apply`,
`chart_events_pump`, `chart_events_tick`, `chart_events_take_anim`,
`chart_events_set_bop`, `chart_events_ease_id`, `chart_ease_eval`,
`ease_linear`, `ease_quad`, `ease_quart`, `ease_quint_in_out`, `ease_circ`,
`ease_expo`, `ease_elastic_in_out`, `steps_to_seconds`, `fx`, `anim_push`

**`engine/song_registry.c` (20):** `sr_levels`, `sr_level_count`,
`sr_song_count`, `sr_level`, `sr_level_by_id`, `sr_song_by_id`,
`sr_song_has_difficulty`, `sr_chart_path`, `sr_chart_path_at`,
`sr_chart_layout_count`, `sr_instrumental_path`, `sr_vocals_path`,
`sr_character_path`, `sr_validate`, `check_song`, `char_exists`,
`stage_exists`, `join_path`, `note_style_unknown`, `default_report`

**`engine/vram_cache.c` (12):** `vc_init`, `vc_pedir`, `vc_fixar`,
`vc_limpar`, `vc_livre`, `vc_maior_buraco`, `alinhar`, `achar`, `inserir`,
`fundir`, `primeiro_que_cabe`, `despejar_um`

**`engine/io_fila.c` (7):** `io_init`, `io_enfileirar`, `io_bombear`,
`io_terminado`, `io_resultado`, `io_pendentes`, `escolher`

**`audio_ring.c` (15):** `audio_ring_start`, `audio_ring_start_loop`,
`audio_ring_stop`, `audio_ring_take`, `audio_ring_level`,
`audio_ring_level_snapshot`, `audio_ring_eof`, `audio_ring_reset`,
`audio_ring_switch`, `audio_ring_pause`, `audio_ring_stats`,
`audio_ring_debug`, `producer`, `lock_ring`, `unlock_ring`

Dessas 89, **20 são `static`** — não dá para chamar direto. A prova delas é
execução indireta mais cobertura: `chart_u16`, `chart_u32`, `chart_fnv1a`,
`chart_fnv1a_more`, `string_bytes_of`, `steps_to_seconds`, `char_exists`,
`stage_exists`, `join_path`, `note_style_unknown`, `default_report`,
`check_song`, `alinhar`, `achar`, `fundir`, `inserir`, `primeiro_que_cabe`,
`despejar_um`, `escolher`, `lock_ring`/`unlock_ring`, `producer`.

### Só compilam (111)

**`main.c` (94):** `tut_anim_idx`, `read_exact_path`, `title_u32le`,
`title_lz4_decode`, `tutorial_pack_load`, `tutorial_pack_frame`,
`tutorial_packs_free`, `dl_header`, `dl_dump`, `dl_gravar`, `dl_sprite`,
`story_packs_free`, `story_pack_mem`, `story_packs_load`,
`title_read_pack_header_mem`, `title_load_packed_frame_mem`,
`title_animation_cache_worker`, `title_animation_cache_start`,
`tutorial_scene_load`, `load_metadata`, `desenhar_calibracao`, `vy`, `rgba`,
`rect_alpha`, `rect`, `reset_iop`, `pad_ready`, `init_pad`,
`buttons_pressed`, `texture_extent_set`, `texture_extent_get`,
`bind_texture_filter`, `bind_texture`, `setup_texture_dims`,
`setup_texture`, `anim_button`, `upload_raw_psm`, `upload_raw`, `band_set`,
`band_counters_reset`, `band_clip_phys`, `band_clip_v`, `band_clip_texel`,
`sprite_dims`, `sprite_region`, `sprite_region_phys`, `sprite_region_alpha`,
`tutorial_lane_button`, `tutorial_notes_reset`, `tutorial_notes_update`,
`tutorial_note_y`, `tutorial_notes_draw`, `title_alpha`,
`audio_set_stream_rate`, `audio_set_stream`, `audio_play_complete`,
`tutorial_audio_mix_submit`, `audio_init`, `menu_audio_prime`, `text_draw`,
`rle_decode`, `menu_atlas_dilate_rgb`, `menu_atlas_resample_phys`,
`menu_flicker_step`, `menu_decode_begin`, `menu_decode_step`,
`menu_font_restore`, `story_ui_restore`, `story_titles_restore`,
`story_font_alpha_decode`, `tutorial_vcr_restore`, `story_vcr_line`,
`hud_score_line`, `story_vcr`, `menu_idle_blend`, `story_upload_title`,
`av_trace_capture`, `av_trace_dump`, `story_title_targets`,
`story_title_update_positions`, `write_all_fd`, `boot_mark`,
`capture_status`, `title_intro_phase`, `cap_wait_clear32`,
`cap_wait_set64`, `safe_readback_rect`, `raw_write_chunks`,
`capture_framebuffer_raw`, `fnx_hex`, `fnx_congelado2`, `ed_tex`,
`estado_dump`, `main`

**`telemetry.c` (17):** `exec_irx`, `flush_output`, `write_text`,
`write_line`, `log_header`, `log_try_open`, `telemetry_init`,
`telemetry_status`, `telemetry_event`, `telemetry_frame`, `telemetry_state`,
`telemetry_line`, `telemetry_raw`, `telemetry_phase`, `telemetry_io`,
`telemetry_flush`, `telemetry_finish`

---

## Apêndice B — reprodução dos comandos

```sh
# 1. a prova por execucao
$ sh test/rodar-prova.sh
=== 243 checagens, 0 falharam ===
TODAS PASSARAM
funcoes sem nenhuma linha executada: 0  (tem de ser 0)

# 2. a build completa do PS2
$ sh tools/with_toolchain.sh sh -c 'rm -f src/*.o src/engine/*.o *.elf *.map; ./build.sh'
    ok   compiled (17s total)
    ok   fnf_ps2_m84.elf is 5271460 bytes (baseline 5,089,600)
done in 17s

# 3. a marca da build no binario
$ strings -a fnf_ps2_m84.elf | grep -E '^PS2 0\.2\.'
PS2 0.2.84-calibracao

# 4. as 8 marcas de rastro
$ strings -a fnf_ps2_m84.elf | grep -cE '^T_(PAD|AUD|UPD|DRAW|DMA|VSYNC|FB|END)$'
8

# 5. tamanho e md5
$ md5sum fnf_ps2_m84.elf
e27caffcd4f21f947cd619bd20e2437a  fnf_ps2_m84.elf
```
