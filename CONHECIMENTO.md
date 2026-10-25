# CONHECIMENTO ACUMULADO — FNF PS2

Tudo que foi medido, descoberto e decidido neste projeto, com fonte. **Nada aqui
é estimativa**: cada número tem origem (linha de log, medição sobre arquivo real,
arquivo de código, ou fato documentado do ps2sdk).

Se você for continuar este projeto, **leia este arquivo antes de escrever uma
linha de código**. Ele contém meses de medição que não estão em nenhum outro
lugar.

---

## 1. Identidade do projeto

- **O que é:** porte do Friday Night Funkin' (versão web/Lime/OpenFL) para
  PlayStation 2, em C, usando o ps2sdk.
- **Repositório:** `grasshopperconta-a11y/PS2Projects`
- **Branch de trabalho:** `arena/4c50659b-ps2projectes` (fixa, não renomear)
- **Commit atual:** `7037d61`
- **Build atual:** `0.2.111-log-reabre`
- **Regras do projeto:** `REGRAS.md` — **leia e siga**. A regra 1 é: nada,
  nunca, jamais é inventado.

---

## 2. Links (Google Drive)

- **Pasta de entregas:** `1bhBZGS67lWeSzlDxK7TeNdJSc7_Z2VC1`
- **Pasta de assets (43 arquivos):** `1XEb6Q9tRfOZU5iGjnXfYyxFzpCicYfD3`
- **Pendrive 0.2.112 (ZIP completo, 47.488.753 B, 400 arquivos):**
  `1-b_MGBqR0ZNntX6nYIRN90J20ufMQEIf` — descompacte **direto na raiz** do
  pendrive. Traz `FNF_PS2.ELF` + `FNFPS2/assets/` com os 16 assets e os 81
  charts nos 4 layouts + `LEIA-ME.txt`.
- **Cliente do canal remoto (ZIP, 7.049 B, 3 arquivos):**
  `1R8YMDecPuhro9QqJGksChGPv0vfeyIQH` — ver §13. Não precisa de senha nem de
  instalação. (A versão anterior, `1jfFk4SJt6Uffdaytd2jRala8xATNiTRu`, usava
  um servidor exposto em URL pública que o proxy do e2b não serve — está
  superada, não use.)
- **`menu_cache.rle` corrigido (1.587.561 B):**
  `1G6hpFcI8u2i7Ig0-z2cQMgb8QOezU91E` — ver §11.
- **ELF 0.2.112 (entregue, o atual):** `1tWGK7DhGWpbWTXlo3N4fhPQKyVDBXsQp`
  5.264.808 B, md5 `78bf7f6d4591ae9b73b9bb81516d5486`,
  sha256 `095a5e0b68a2e34a591ddf57ffcc3415b56f689840e3e2068f3c2301bdf74faa`.
  **Rebuild byte-idêntico confirmado** (duas compilações limpas, mesmo md5).
- **ELF 0.2.111 (entregue, superado):** `1MZ4wEki3gQB5Hj9y7HSWE6x56HsnRmB1`
  5.264.820 B, md5 `facadf7338ad14a6d2dc7f8a713be918`. Diferença de 12 B para a
  0.2.112 é só a string de versão (`0.2.84-calibracao` vs `0.2.112`); a 0.2.111
  foi compilada com a versão default do Makefile.
- **ELF 0.2.110:** `1k0WbjQBOlvPGBRcsssmvh4huwlMEuRXN`
- **ELF 0.2.109:** `158ACsUScHVnOela2AWYOA3uRg5I3mxfZ`
- **ELF 0.2.108:** `1tajPzIX2RSX-rBQIKFpIQnWjS5H7qbny`
- **Pendrive 0.2.109 (com LEIA-ME):** `1rxXQob8hVocx3x-3bmoHlam1NFi7C6-u`
- **Toolchain (43.841.008 B, tar.xz):** `1Va-8_k4GTxXpJaX4uMApV8OOpE9_QzJc`
  ⚠️ **Atenção ao ler este id:** o caractere antes do `Jc` é **J**, não Z.
  Um erro de digitação aqui custou tempo de trabalho.

Formato de link de download:
`https://drive.google.com/uc?export=download&id=<id>`

Todos os arquivos de entrega já estão `anyoneWithLink`, role `writer`.

---

## 3. Como compilar

```sh
# 1. extrair o toolchain (faz tudo: extrai, exporta PS2DEV, limpa no exit)
sh tools/with_toolchain.sh make -j4 FNF_VERSION=0.2.112-minha-versao \
    EE_BIN=build/FNF_PS2.ELF
```

`tools/with_toolchain.sh` procura `PS2DEV_EE_MIN_FNF.tar.xz` em
`/home/user/PS2Projects/google_drive/` e extrai para
`fnfps2/build/toolchain`. Se o arquivo não estiver lá, falha com
`nao achei PS2DEV_EE_MIN_FNF.tar.xz`.

**Build tem de sair sem nenhum warning.** O projeto compila com
`-Wall -Wextra -Werror=implicit-function-declaration`.

---

## 4. Como testar

```sh
sh test/run_tests.sh          # suite inteira (unitários + harness + negativos)
sh tools/run_harness.sh 1400  # só o harness, 1400 quadros
python3 tools/analisa_log.py  # analisa o log gerado
```

O que o harness cobre: 1401 quadros, jogo inteiro (título → menu → story →
tutorial, 5 ciclos), estouro de pacote, DMA acima de QWC_MAX, asset que não
abriu, escrita na zona de guarda, ASan+UBSan.

### ⚠️ O QUE O HARNESS NÃO COBRE — ISTO JÁ CUSTOU TRÊS BUILDS

`test/ps2harness/ps2h.c` **finge** a E/S do PS2:

| Função | No harness | No PS2 real |
|---|---|---|
| `open("mass:/...")` | interceptado, vira caminho local | RPC fileXio para o IOP |
| `write()` | `syscall` direto — **instantâneo** | RPC + escrita de bloco USB — **milissegundos** |
| `fsync()` | idem, instantâneo | **flush do USB, dezenas a centenas de ms** |
| `reset_iop()`, `SifExecModuleBuffer()`, `fileXioInit()`, `sbv_patch_*` | no-op | real |

**Consequência:** qualquer correção sobre I/O, tempo, sincronização ou hardware
**não pode ser verificada pelo harness**. Se você afirmar "verificado" depois de
rodar `run_tests.sh` sobre uma correção de E/S, você está inventando.

---

## 5. Estado atual — o que funciona e o que não

### Funcionando no console (build 0.2.106, última confirmada pelo usuário)

- Faixa visível 4:3 correta: **112 linhas pretas, conteúdo apenas nas linhas
  56..391** de 640×448. Antes desta correção a mesma auditoria media 2.567
  violações.
- Jogo abre, menu funciona, story funciona, tutorial toca música.

### NÃO resolvido (o usuário testou e confirmou em hardware)

1. **Linha estranha abaixo dos botões animados do menu principal.** Sintoma
   recorrente. **Descoberta do log:** o menu desenha **cada item 2× por quadro**
   (duas passagens completas, ordem 1,2,3,4 / 1,2,3,4). No FNF original cada
   item é desenhado uma vez. Isso dobra o alpha e dobra as chamadas de desenho.
   **Ainda não corrigido.**
2. **Itens do menu quebrados ao voltar do modo história.** Sintoma recorrente.
3. **Fundo do menu esticando em vez de rolar.** ✅ **CORRIGIDO** — ver §7.
4. **Travamento ao entrar no modo história.** Não reproduzido no harness.
5. **Tutorial:** câmera travada no BF, sem notas, sem barra de acerto,
   personagens não animando, música toca. Código escrito, não confirmado.
6. **O log vinha com 0 bytes.** ✅ **CORRIGIDO** — ver §8.

### ⚠️ "O jogo não abriu" — três builds quebradas, e o que se aprendeu

As builds **0.2.108, 0.2.109 e 0.2.110 não abriram no console**. Três causas
diferentes foram afirmadas com convicção e **nenhuma era a real na hora em que
foi dita**. A sequência real:

| Build | Causa real | Status |
|---|---|---|
| 0.2.108 | `telemetry_raw()` por sprite = ~20 escritas bloqueantes no pendrive **dentro** do laço de render | corrigido em 0.2.109 |
| 0.2.109 | `telemetry_flush()` com `fsync()` **em todo quadro** = 60 sincronizações de USB por segundo | corrigido em 0.2.110 |
| 0.2.110 | `telemetry_init()` desistia após 5 s, mas o USB leva **mais** de 5 s para re-enumerar depois de `reset_iop()` | corrigido em 0.2.111 |

**A lição que virou regra:** o sintoma "não abriu" tem seis significados
possíveis. Sem dado que os distinga, a build seguinte serve para **coletar**
dado, nunca para tentar um conserto.

---

## 6. O log — formato e como lê-lo

**Caminho no console:** `mass:/FNFPS2/FNF_COLHEITA.txt`
**Caminho no harness:** `fnfps2/build/harness_assets/FNFPS2/FNF_COLHEITA.txt`

O log é **acumulativo** (O_APPEND, sem truncar). Para colheita limpa, apague o
arquivo antes de testar.

### Tipos de linha

| Prefixo | Conteúdo |
|---|---|
| `#` | comentário/cabeçalho, inclui a legenda das colunas |
| `P,fase,linha,cod` | marco de fase (boot, troca de estado). **Escrito e sincronizado na hora.** |
| `S,` | estado completo da máquina de estados, um por quadro |
| `F,` | tempo de quadro (begin/draw/vsync, qwords, fps) |
| `D,` | **um sprite por linha** — a geometria que foi ao GS |
| `E,` | evento nomeado |
| `IO,` | operação de arquivo com resultado |

### Linha `D,` (a mais valiosa)

```
D,quadro,i,estado,x,y,w,h,u,v,uw,vh,alfa,vy0,vy1,vy_span,gsx0,gsy0,gsx1,gsy1
```

Índices (0-based, `p = linha.split(',')`):
`p[1]`=quadro `p[2]`=i `p[3]`=estado `p[4]`=x `p[5]`=y `p[6]`=w `p[7]`=h
`p[8]`=u `p[9]`=v `p[10]`=uw `p[11]`=vh `p[12]`=alfa `p[13]`=vy0 `p[14]`=vy1
`p[15]`=vy_span `p[16]`=gsx0 `p[17]`=gsy0 `p[18]`=gsx1 `p[19]`=gsy1

`x,y,w,h,u,v,uw,vh` são os valores **depois** do recorte da faixa.
`vy0/vy1` são os vértices que foram ao GS.

**Como detectar os defeitos só com o log:**

- **Sprite esticado:** `h/vh` (escala tela/textura) diferente da escala do
  sprite inteiro. A referência do projeto é **1.5894** (= 406.893/256). O fundo
  do menu aparecia com `h=335.00, vh=205.56` → escala **1.6297**, ou seja
  **+2.54% de esticamento**, todo quadro.
- **Sprite fora da faixa:** `vy0` ou `vy1` fora de 56..391.
- **Item deslocado:** comparar o `(y,h)` dos itens entre a primeira visita ao
  menu e as seguintes.
- **Travamento:** onde o log para. O último `P,` com `_BEGIN` sem `_DONE`
  correspondente depois dele.

### ⚠️ Uma rodada por arquivo — e o mapa da linha `S,`

**Desde a 0.2.112 o log trunca.** `telemetry.c:186` abre com
`O_WRONLY|O_CREAT|O_TRUNC`. Os três despejos de `main.c` (`av_trace_dump`,
`fnx_congelado2`, `estado_dump`) continuam com `O_APPEND`, porque entram no
**mesmo** arquivo desta rodada. A regra: **quem abre primeiro trunca, quem entra
depois acrescenta.**

Antes disso era `O_APPEND` em tudo, e cada boot acumulava no arquivo do
pendrive. Um log com várias rodadas **não pode ser lido de uma vez** — foi assim
que nasceram duas conclusões falsas (ver §12). Sempre confira:
`grep -c "^P,SHUTDOWN" FNF_COLHEITA.txt` — se der mais de 1, separe antes de
analisar. `tools/analisa_log.py` faz isso sozinho desde a 0.2.112.

**Mapa da linha `S,` (41 campos, `src/telemetry.c:353`):**

```
S, 1 quadro, 2 ui_state, 3 target_state, 4 selection, 5 story_level,
  6 story_diff, 7 transition_frame, 8 transitions, 9 transport_state,
  10 audio_started, 11 audio_playing, 12 menu_audio_suspended, 13 chart_status,
  14 tutorial_scene_ready, 15 tutorial_audio_status, 16 story_assets_ready,
  17 menu_cache_ready, 18 title_anim_status, 19 gf_uploaded, 20 bf_uploaded,
  21 gf16_uploaded, 22 story_gf_uploaded, 23 story_bf_uploaded, 24 aspect_169,
  25 viewport_360, 26 music_clock, 27 audio_submitted, 28 ring_level,
  29 underruns, 30 audio_fd, 31 title_audio_fd, 32 note_hits, 33 note_misses,
  34 note_combo, 35 note_score, 36 note_feedback, 37 event_cursor,
  38 band_clip_rects, 39 band_clip_lines, 40 band_cull_rects
```

**O que NÃO está na linha `S,`:** o estado do piscar do menu
(`g_fl_item_vis`, `g_fl_item_toggles`, `menu_exit_frames`). Ele só sai no
despejo sob demanda de `dl_sprite()` (`main.c:1095-1107`), na linha
`phys1:1 ... flick_item_vis=%d toggles=%d flick_mag_vis=%d toggles=%d exit=%d`.
Consequência: **o log não explica, por si, por que um quadro do estado 6 tem 3
itens em vez de 4.** Quem lê precisa saber que é o piscar do confirmar
(16 piscadas, `g_fl_item_left=16`). Está anotado aqui e no analisador.

### `BOOT.txt` — o marcador que sobrevive

`mass:/FNFPS2/BOOT.txt` (ou `mass:/BOOT.txt` se a pasta não existir). Uma linha,
reescrita com `fsync` a cada passo: `passo N: <FASE> code=<código>`.

Existe porque **log nenhum explica um boot que não acontece**: se o pendrive
nunca montou, não há log. Este arquivo diz o último passo completado. Para de
escrever após o boot, e marca **quadro a quadro nos primeiros 300 quadros**.

---

## 7. O bug do fundo esticado — corrigido e provado

**Causa:** aritmética de `band_clip_phys()` em `src/main.c`. A fração de baixo
era medida a partir do `y0` **já cortado** pelo primeiro `if`. Quando o sprite
cruza a faixa dos dois lados — o fundo do menu tem 406,893 linhas físicas contra
uma faixa de 335 — a fração sai pequena demais, o trecho de textura vem estreito
e o sprite estica.

**Prova, pelo log, mesma linha antes e depois:**

```
antes : h=335.00  v=6.33  vh=205.56  ->  escala 1.6297  (+2.54%)
depois: h=335.00  v=6.33  vh=210.77  ->  escala 1.5894  ( 0.00%)
```

**Correção:** as duas frações passaram a ser medidas a partir do `y0` original.

---

## 8. O log com 0 bytes — causa raiz e correção

**Causa raiz (descoberta pelos dados do console, não por hipótese):**

`reset_iop()` **desmonta o pendrive que o lançador montou**. Depois de
recarregar `usbd`/`usbhdfsd`, a re-enumeracao do USB levou **mais de 5
segundos**. O `telemetry_init()` esperava 5 s, desistia, e o log nunca era
aberto — todas as escritas seguintes viravam no-op silencioso.

**A prova de que o `mass:` aparece depois:** o `boot_mark()` abre o **próprio**
arquivo, não depende da máquina de telemetry, e escreveu o passo 1 normalmente —
porque quando ele rodou já tinham se passado os 6,5 s de espera do init e o
pendrive tinha montado. **O dispositivo aparece; o init é que desistia cedo
demais.**

**Correção (0.2.111):** a abertura do log virou função própria,
`log_try_open()`, e ganhou uma **segunda chance tardia**, chamada de
`telemetry_phase()` e de `telemetry_state()` — uma vez por quadro, no máximo 40
vezes. Se o pendrive montar depois do boot, o log começa a sair a partir do
quadro em que isso acontecer.

**Outras causas históricas do log vazio (já corrigidas, não reintroduzir):**

- `main.c` reabria o log com `O_TRUNC` logo depois do `telemetry_init()`,
  apagando o cabeçalho — e criava um segundo escritor no mesmo arquivo.
- `capture_status()` abria/escrevia/`fsync`/fechava o arquivo a cada chamada,
  enquanto a telemetria segurava outro descritor com buffer. Dois escritores.
- `dl_sprite()` era gated por `g_dl_gravando`, então nenhuma linha de sprite era
  registrada por padrão.

---

## 9. Fatos de hardware e ps2sdk (medidos, não presumidos)

### Vídeo

- Tela física **640×448** (NTSC), framebuffer PSMCT32, double buffer.
- `vy(y) = VY_OFFSET + y * VY_FATOR`, com
  `VY_FATOR = g_aspect_169 ? 448/360 : 14/15` e
  `VY_OFFSET = g_aspect_169 ? 0 : 56`.
- Faixa publicada em 4:3: `SCISSOR_TOPO/BASE = 56/391`. Em 16:9: `0/447`.
- O log do console confirma **4:3**.
- `draw_setup_environment` emite um GIF tag packed de 15 qwords, SCISSOR para o
  framebuffer inteiro, XYOFFSET (2048,2048), `PRMODECONT = PRIM_OVERRIDE_DISABLE`.
- `draw_rect_textured` escreve seu próprio GIF tag e PRIM, então o contexto do
  PRIM sempre casa com o argumento `context` do helper (o projeto passa 0).
- **O scissor do GS corta de verdade — medido em hardware.** O vértice que sai
  para o GS passa da faixa por uma fração de linha (ex.: o fundo do menu em
  `gsy 55.5625..391.5625`, contra a faixa 56..391). Nas 6 capturas RGBA32 da
  0.2.106 (1.146.880 B cada, 640×448), o conteúdo começa **exatamente** na linha
  56 e acaba **exatamente** na 391 — 336 linhas, sem sangramento para a 55 nem
  para a 392. Portanto a fração de linha dos vértices não é defeito, e a
  checagem disso no `analisa_log.py` é informativa, não um problema.
  (Observado à parte: 5 das 6 capturas tinham 3 pixels escuros e isolados na
  **linha 6**, x=256..258 — fora da faixa, no topo. Não sei a causa e não
  concluo nada a partir daí.)

### `texrect_t` — layout autoritativo (`ee/draw/include/draw2d.h`)

```
{ vertex_t v0; texel_t t0; vertex_t v1; texel_t t1; color_t color; }
```
Offsets em floats: `v0.x`=0 `v0.y`=1 `v0.z`=2, `t0.s`=4 `t0.t`=5,
`v1.x`=6 **`v1.y`=7** `v1.z`=8, `t1.s`=10 `t1.t`=11, `color`=12.
`vertex_t` = 12 B (z é `unsigned int`); `texel_t`/`color_t` = 8 B.
⚠️ Ler `v1.y` no offset 3 silenciosamente devolve `t0.s`.

### A "linha abaixo dos botões" — o que já se descartou, com medição

O usuário descreve: *"uma linha que pisca de forma repetida, como se seguisse
os sprites da animação, em alguns botões (quase todos), em estados específicos:
câmera se movendo, câmera estática, não selecionado, selecionado"*.

**Descartado, cada um com sua medição:**

1. **Não é geometria.** Em 545 itens do menu no log do harness: escala `h/vh`
   = **1,0** em todos; `x`, `y` e `vy0` com fração **0,0** em todos (nenhum
   subpixel); `vy_span == h` em todos. O blit é 1:1 exato.
2. **Não é o "1 pixel a mais" do quad do GS.** Todo sprite sai 1 px maior que a
   região de textura (`gsx1-gsx0 = w+1`). Isso é **oficial do ps2sdk**, não
   defeito do porto: `ee/draw/src/draw2d.c` define
   `START_OFFSET 2047.5625f` (= 2048 − 0,4375 + 1) para v0 e
   `END_OFFSET 2048.5625f` (= 2048 + 0,5625 + 1) para v1 — diferença de
   exatamente 1,0, em `draw_rect_textured`. `dl_sprite()` replica essa mesma
   conversão.
3. **Não é o atlas.** `tools/inspecionar_atlas.py` decodifica o
   `menu_cache.rle` REAL e replica os três passos do jogo (RLE, `dilate_rgb`,
   `resample_phys`). Medido nos 30 quadros originais e nos 30 reamostrados: o
   maior desvio local de alfa é **12,1 de 128 (9%)**, e as bordas são fades
   suaves (STORY MODE se=0, últimas 5 linhas: 83.3, 61.2, 32.0, 12.6, 3.8).
   Não há linha de 1 px na textura.
4. **Não é duplicação de sprite** e **não é o menu voltar diferente** — ver §12.

**O que continua sem explicação.** A causa não é conhecida. Os suspeitos que
restam são a rasterização do GS com filtro LINEAR (`bind_texture_filter(...,1)`)
e a interação do `END_OFFSET` do ps2sdk com o mapeamento UV — mas **isso é
hipótese, não medição**, e não vou agir sem dado. O dado que decide é um log do
console com a linha aparecendo, porque o log tem o quadro, o item e o estado.

### Geometria do menu principal

- Fundo: `bg_y = -37.978227f - (menu_cam_y - 360.0f) * 0.085f`, altura
  **435.956454**, x = **-64**, largura **768**.
- Itens: `camoff = (menu_cam_y - 360.0f) * 0.4f`,
  `cy = (40.0f + 160.0f * mi - camoff) * .5f`.
- Slots de `mi` medidos no log: y = 94, 181, 255, 332 (mi=0..3), com alturas
  81, 57, 58, 52 e larguras 384, 242, 193, 244.

### Assets

- `menu_cache.rle`: 1.623.445 B (o script avisa que esperava 1.587.561 — o
  bloco 4 de story titles foi acrescentado). Blocos: menu [0,1288182) →
  2.961.848; font [1288182,1326524) → 294.912; story ui [1326524,1398926) →
  524.288; story titles [1398926,1587561) → 306.180.
- **Formato do token RLE:** `c<128` → copia `(c+1)*4` bytes; `c>128` → repete o
  pixel de 4 bytes seguinte `257-c` vezes (**5 bytes consumidos**); `c==128` →
  erro.
- **Fonte VCR do story:** blob em `menu_sfx.pcm` offset **264.576**, 7.672 B →
  160×120 px, grade 16×6 de células 10×20, glifo n = ch−32; RGB forçado branco,
  alpha reescalado `(a*128+127)/255`; avanço **9.375**.
- **Atlas da fonte principal:** 384×192 RGBA32, grade 16×6, célula 24×32, glifo
  n = ch−32 para ASCII 32..127; avanço `g_font_widths[n] * 0.5`.
- **Atlas dos títulos do story** (`g_story_title[9][3]`, RGBA32, 306.180 B),
  offsets (x,y,w,h): (0,222,41) (36408,180,44) (68088,180,44) (99768,179,44)
  (131272,177,44) (162424,182,46) (195912,180,46) (229032,182,50)
  (265432,167,61).

### Formato da captura de tela

`mass:/FNFPS2/FNF_SCREEN_%04u.rgba.txt` = **RGBA32 puro**, 640×448,
**1.146.880 B** por arquivo, sem cabeçalho. Ler com
`d[(y*640+x)*4 .. +3]`. Fundo bege = RGB(253,231,113); letterbox = RGB(0,0,0).
Acionada por **SELECT+R3** simultâneos.

### Áudio

audsrv, pcm s16le estéreo 48000 Hz.

---

## 10. Ferramentas do repositório

| Arquivo | O que faz |
|---|---|
| `tools/with_toolchain.sh` | **a forma correta de compilar.** Extrai o toolchain, exporta PS2DEV, limpa no exit |
| `tools/run_harness.sh` | compila e roda o harness (jogo real + draw real do ps2sdk) |
| `test/run_tests.sh` | suite inteira |
| `tools/analisa_log.py` | **lê um log e responde sozinho** os quatro defeitos do console |
| `tools/build_pendrive.sh` | monta a pasta do pendrive + `LEIA-ME.txt` na raiz |
| `tools/fix_menu_cache_block4.py` | corrige o bloco 4 do `menu_cache.rle` |
| `tools/gen_harness_assets.py` | gera os assets sintéticos do harness |
| `tools/check_assets.py`, `check_real_assets.py`, `check_harness_assets.py` | validam assets |
| `tools/vram_budget.py`, `dump_stage_geometry.py` | orçamento de VRAM e geometria |

### `analisa_log.py` — use sempre

```sh
python3 tools/analisa_log.py [caminho/do/FNF_COLHEITA.txt]
```

Sem argumento, procura em `build/harness_assets/FNFPS2/FNF_COLHEITA.txt`.
Responde, sem ninguém descrever sintoma: (1) sprite que não passa pela faixa e
sprite que não é fundo nem item; (2) escala vertical de cada sprite contra a
referência 1.5894; (3) a cara do menu na primeira visita vs. as seguintes;
(4) onde o log parou e fase que começou sem fechar. Mais: falhas declaradas
(`_FAIL`) e sprites inteiramente fora da faixa.

Foi validado num log sintético com três defeitos injetados: pegou o
esticamento de 2,54%, o menu com cara diferente e o sprite fora da faixa.

---

### ⚠️ O `menu_cache.rle` do Drive estava VELHO — e o sintoma era a fonte errada

**Descoberta em 0.2.112, ao montar o pendrive.** O `build_pendrive.sh` avisa
quando o `menu_cache.rle` não tem 1.587.561 bytes. A cópia do Drive tinha
**1.623.445**. A causa, medida por `tools/fix_menu_cache_block4.py`:

| bloco | offset | comprimido | decodificado | estado |
|---|---|---|---|---|
| menu | 0 | 1.288.182 B | 2.961.848 B | OK, preservado |
| fonte | 1.288.182 | 38.342 B | 294.912 B | OK, preservado |
| story ui | 1.326.524 | 72.402 B | 524.288 B | OK, preservado |
| **story títulos** | 1.398.926 | **224.519 B → 379.264 B** | | **VELHO** |
| story títulos (certo) | 1.398.926 | **188.635 B → 306.180 B** | | regerado |

Os três primeiros blocos decodificam perfeito; só o quarto — o que desenha os
**9 nomes das semanas do modo história** — era de outra versão. É exatamente o
sintoma que o usuário reportou como *"os botões do modo história usam uma fonte
diferente"*, que estava marcado como "corrigido no asset". **A correção existia
na ferramenta, mas nunca tinha sido aplicada ao arquivo do Drive** — o
comentário do `build_pendrive.sh` afirmava que "a cópia do Drive já é a
corrigida", e essa afirmação era **falsa**. O tamanho do arquivo prova.

**O número que decide:** o jogo lê exatamente
`PRELOAD_RLE_BYTES = MENU_RLE_BYTES + FONT_RLE_BYTES + STORY_RLE_BYTES +
STORY_TITLES_RLE_BYTES = 1.288.182 + 38.342 + 72.402 + 188.635 =
**1.587.561 bytes**`. Um arquivo maior não falha na leitura — falha depois,
dentro de `story_titles_restore()`. Por isso o sintoma aparecia só no modo
história, e só na tela dos nomes das semanas.

**Corrigido, e à prova de recorrência:**
- `tools/build_pendrive.sh` agora **regenera e verifica** o bloco 4 em todo
  build, e ainda decodifica o bloco 4 para confirmar que fecha em
  188.635 → 306.180. Um arquivo velho não passa mais silenciosamente.
- O Drive foi trocado: id novo **`1G6hpFcI8u2i7Ig0-z2cQMgb8QOezU91E`**
  (1.587.561 B, sha256 `cd27d719…d351`), o velho
  (`1p4gBOaOrUytU85MVt0VPwOEqip69OzWt`) foi para a lixeira. Upload verificado
  byte a byte por re-download.
- `assets-manifest.json` aponta para o novo id e carrega o aviso.

**A lição:** um AVISO num script não é uma correção. Eu ignorei esse aviso por
várias sessões e entreguei pendrive com o bug. Verificação que não **impede** o
build não é verificação.

## 13. Canal de comando remoto (`canal/` + `tools/remote/`)

Canal para eu executar comandos no PC do usuário e receber a saída. Nasceu de
um pedido dele: *"você mesmo pode criar um programa que faça isto e eu deixo
aberto aqui no meu pc"*.

### A primeira tentativa FALHOU, e por quê

Montei um servidor HTTP aqui, exposto em `https://8791-<sandbox>.e2b.app`, com
senha nos dois sentidos. Testei tudo em `127.0.0.1` (20 verificações, todas
passando) e entreguei.

**O usuário abriu a URL e recebeu `502 Bad Gateway — Sandbox not found`.**

Diagnóstico, em ordem:
- O ID do sandbox estava **correto** (`E2B_SANDBOX_ID`), e o servidor estava
  **no ar**, escutando em `0.0.0.0:8791` — confirmei os dois na hora.
- De dentro do sandbox eu **não alcanço** a URL do proxy (`HTTP 000`): o
  allowlist de saída daqui é exatamente os 6 hosts declarados, e `e2b.app`
  não está entre eles. Então *nunca pude verificar a URL pública do meu lado* —
  e não deixei isso claro o suficiente para o usuário testar antes de confiar.
- O proxy do e2b diz que o sandbox **não existe**. Não é porta errada, não é
  cache: é o sandbox inteiro. A troca de porta não resolveria.

**A lição:** um servidor que eu só consigo testar por `localhost` não é um
servidor que eu posso entregar. E "não consegui verificar" precisa virar
"peça para o usuário testar antes de qualquer coisa", não uma nota de rodapé.

### A arquitetura que funciona: arquivo público no GitHub

O allowlist de saída me dá `api.github.com`, `github.com` e
`codeload.github.com`. O repositório `grasshopperconta-a11y/PS2Projects` é
**público** e eu tenho permissão de escrita. Daí:

| sentido | como | precisa de senha? |
|---|---|---|
| eu → PC do usuário | eu faço `git push` de `canal/comandos.txt`; o cliente lê de `raw.githubusercontent.com` | **não** |
| PC do usuário → eu | o cliente salva `resultados/resultado-<id>.txt`; o usuário arrasta a pasta para o Google Drive, que eu já leio pelo conector | **não** |

**Por que isso é seguro, e é seguro de um jeito diferente do anterior:** o
canal é um arquivo **público**. Qualquer pessoa pode *lê-lo* — inclusive um
curioso. Só eu posso *escrever*. O pior caso possível é alguém ler a lista de
comandos que eu mandei. Não existe injeção de comando por fora, porque não
existe endpoint público de escrita. Não há senha para vazar, não há token no
PC do usuário, não há servidor meu exposto.

Isso custa um passo manual por lote (arrastar a pasta `resultados` para o
Drive), e é a troca certa: a versão automática exigiria um token do GitHub no
PC dele, e um canal de escrita pública seria exatamente a coisa perigosa que
eu tinha alertado que não faria.

### O cliente

`tools/remote/fnf-remote-client.ps1` — PowerShell puro, zero dependência,
zero instalação. Lê o canal a cada 5 s, executa só as linhas com id maior que
o último que rodou (guardado em `estado.txt`), e por isso **nunca repete** um
comando depois de fechar e reabrir.

Formato do canal, uma linha por comando: `<id>|<comando>`. Prefixo `CMD:` manda
para o Prompt de Comando; o resto vai para o PowerShell.

O `?cb=<timestamp>` no fetch não é enfeite: o GitHub põe um CDN na frente do
`raw.githubusercontent.com`, e sem furar o cache o PC do usuário poderia ficar
lendo a cópia velha por minutos depois de eu publicar um comando.

### A trava de System32

Fica **no cliente**, antes de qualquer execução, e é recusa dura: o comando
não roda, devolve código 99 e salva o resultado explicando. A normalização é
`minúsculo -> sem espaços -> barra arrumada`, então `"C:\Windows\System 32"`,
`c:/windows/SYSTEM32` e `WiNdOwS\SyStEm32` caem no mesmo filtro.

**O buraco que existiu:** eu tinha escrito `winssxs`, mas a pasta real é
`WinSxS`, cujo minúsculo é `winsxs` — **um `s` a menos**. Comando em WinSxS
passava direto. Só foi pego porque o teste cobre esse caso.

**E o bug de id que o teste pegou:** a comparação é `id <= já rodou`, e o
estado inicial é 0. Um comando com id `0` **nunca executaria** — eu ia achar
que o comando tinha sumido. Agora o parser rejeita `id < 1` explicitamente.

### O bug do `.cmd` que quebraria todo uso

O template comparava `%FNF_PONTE%` com `@@PONTE@@`. Depois de o gerador
substituir o endereço real, a comparação virou *"endereco == endereco"* —
**sempre verdadeira**, então o programa dava erro e saía em 100% dos usos.
Peguei reliando o `.cmd` gerado em vez de confiar no template. A validação
agora é `findstr /b /c:"http"`, que continua significativa depois da
substituição.

### Teste

`test/test_remote.sh`, chamado por `test/run_tests.sh`. 10 verificações:
trava (14 bloqueios + 12 liberações), parser (16 casos), gerador, ausência de
qualquer referência a servidor/porta/senha, e o canal commitado bem formado.

### Layout do pendrive (o jogo exige)

```
mass:/FNFPS2/assets/...          -> assets na raiz do pendrive
mass:/FNFPS2/assets/songs/<id>/<d>.chart
mass:/FNFPS2/FNF_COLHEITA.txt    (criado pelo jogo)
mass:/FNFPS2/BOOT.txt            (criado pelo jogo)
```

A pasta `FNFPS2` **tem de estar na raiz**. Se ficar
`mass:/FNFPS2/FNFPS2/...` o jogo não acha asset nenhum, chama `SleepThread()` e
dorme para sempre — tela preta, e o log cai na raiz em vez de dentro de
`FNFPS2/`. O ZIP de entrega traz `LEIA-ME.txt` na raiz explicando isso.

---

## 12. Erros que não se devem repetir

- **`git commit -F -` com heredoc falha silenciosamente.** Escreva a mensagem
  num arquivo com python e passe `-F /tmp/msg.txt`.
- **O connector do Google Drive usa parâmetros planos**, não um objeto `input`
  aninhado.
- **O id do toolchain tem um `J`, não um `Z`.** `1Va-8_k4GTxXpJaX4uMApV8OOpE9_QzJc`.
- **O ambiente de trabalho é resetado periodicamente.** `google_drive/` e
  `fnfps2/build/` desaparecem, e o histórico local do git volta ao commit
  inicial. **Sempre recupere com `git fetch` + `git reset --hard` no tip do
  remote, e salve arquivos em `/tmp` antes de resetar.**
- **`git reset --hard origin/<branch>` pode falhar** com "could not detach HEAD"
  por causa de arquivos untracked. Apague os arquivos conflituosos antes, ou use
  o SHA: `git reset --hard <sha>`.
- **Não confie em `git log origin/<branch>` depois de um reset** — o ref pode
  estar velho. Use `git ls-remote origin <branch>` para saber o tip real.
- **`rm -rf` num diretório de staging apaga documentos que você acabou de
  escrever nele.** Escreva os documentos no repositório, não em `/tmp`.
- **LI UM LOG COM QUATRO EXECUÇÕES E TIREI DUAS CONCLUSÕES FALSAS.** O
  `FNF_COLHEITA.txt` era aberto com `O_APPEND`, então um único
  `test/run_tests.sh` deixava 4 linhas `P,SHUTDOWN` no mesmo arquivo. Li o
  quadro 364 duas vezes e afirmei que "o menu desenha cada item duas vezes", e
  que "o menu volta com cara diferente depois do roteiro". As duas são falsas.
  Um quadro do estado 6 tem 5 sprites (1 fundo + 4 itens), e as 2 visitas ao
  menu têm exatamente as mesmas 4 posições.
  **Regra que sai daí: antes de comparar qualquer coisa num log, conte quantas
  rodadas ele tem (`grep -c SHUTDOWN`). Se for mais de uma, separe.** Corrigido
  em 0.2.112 (`d2eed51`), e `test/run_tests.sh` agora tem teste que falha se o
  analisador voltar a errar.
- **A contagem de sprites por quadro não é medida de nada.** Ela varia de
  propósito: ao confirmar um item, `menu_flicker_step()` (main.c:856) pisca o
  item selecionado 16 vezes e some em metade dos quadros. Um quadro com 3 itens
  em vez de 4 é animação, não bug.
- **Commitei 25 arquivos gerados (~50 MB) por engano**, porque o `git rm
  --cached` não cobriu `analisa_duas.txt`. Um arquivo já rastreado **não** é
  afetado pelo `.gitignore` — `git check-ignore` não o reporta. Confira sempre
  `git show --name-only HEAD | grep build/` antes de dar push.
