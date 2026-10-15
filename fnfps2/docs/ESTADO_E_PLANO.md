# FNF v0.8.6 → PS2 — Estado real e plano de aceleração

Levantado em 2026-10-05 a partir do workspace `workspace-01a10d4f…zip`
(99 297 218 bytes) e do toolchain ps2dev v2.0.0.

---

## 1. Resposta direta: sim, posso acelerar — e aqui está a prova

Não é promessa. Reproduzi o build do zero nesta sessão:

```
toolchain  ps2dev v2.0.0 / ps2dev-ubuntu-latest.tar.gz
           266 096 645 bytes
           sha256 c8e5dedccf62084d476894e88cd0451b57f1ed288e741eb3c1263010aaffc028
           (hash idêntico ao baixado na sessão anterior — ambiente determinístico)
EE  gcc    mips64r5900el-ps2-elf-gcc 15.2.0
saída      fnf_ps2_m47.elf   4 970 488 bytes
           compilado sem um único erro
```

Compila em **3,4 segundos**. Posso iterar o código quantas vezes for
preciso sem depender de você montar nada no PC.

---

## 2. O gargalo real deste projeto

47 versões. O problema não é falta de competência técnica — a
documentação acumulada é boa e as derivações do código oficial estão
corretas. O problema é o **laço de verificação**:

```
alterar código → compilar → zipar → pendrive → console → olhar a TV
→ descrever o que viu → o modelo adivinha a causa → repetir
```

Cada volta custa minutos seus e entrega **uma frase** de informação
("a GF está acelerada", "a tela ficou preta"). É por isso que
`m46 → m47` gastou um ciclo inteiro para descobrir que o Bopper
estava em loop contínuo a 24 fps em vez de tocar uma vez e segurar o
último quadro. Essa é uma pergunta que se responde com **aritmética**,
não com uma viagem ao console.

### Números que sustentam isso

| | |
|---|---|
| `src/main.c` | 89 618 bytes em **611 linhas** → 147 caracteres por linha |
| maior linha | **3 088 caracteres** |
| linhas acima de 2 000 caracteres | 4 |
| funções | 73 |
| pontos de telemetria | 26 |
| superfície de API do PS2SDK usada | **57 funções distintas** |

Os 57 são a notícia boa: a dependência de hardware é pequena e
delimitada. Todo o desenho passa por `draw_rect_textured`,
`draw_rect_filled`, `draw_clear`, `draw_scissor_area` e
`draw_setup_environment`.

---

## 3. A solução: banco de ensaio no PC (BEPC)

Compilar **o mesmo `src/main.c`**, sem fork e sem reescrita, para
x86-64, com uma camada que substitui o hardware:

```
┌───────────────── src/main.c (BYTE A BYTE O MESMO) ─────────────────┐
└────────────────────────────┬───────────────────────────────────────┘
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
   alvo PS2 (real)                        alvo BEPC (x86-64)
   libdraw/libgraph reais                 libdraw REAL compilada
   GS de verdade                          nativamente + interpretador
   audsrv + SPU2                          GIF → rasterizador do
   libpad                                 subconjunto usado
                                          relógio de áudio determinístico
                                          pad roteirizado
                                          saída: PNG por quadro
```

Pontos que tornam isto preciso e não uma aproximação:

1. **`libdraw` é C puro que só escreve quadwords na memória.** Não
   toca MMIO. Compilada nativamente, produz **exatamente** os mesmos
   valores de registrador GIF que o GS receberia. Zero divergência de
   geometria.
2. O que eu implemento é só o consumidor: um interpretador de GIF que
   entende o subconjunto que o jogo usa (`PRIM`, `TEX0`, `UV`, `XYZ2`,
   `RGBAQ`, `SCISSOR`, `ALPHA`, `TEXFLUSH`, PSMCT32) e rasteriza em um
   framebuffer 640×448.
3. **Relógio de áudio determinístico.** O Bopper, o Conductor e o
   chart são todos função de `(bytes_enviados − audsrv_queued())/4`.
   Com um `audsrv` falso que avança amostras por quadro de forma
   exata, o timing vira **reprodutível e testável por asserção**.
   O bug do m46 teria sido pego por um teste de três linhas.
4. **Pad roteirizado**: sequências de botão em arquivo de texto, para
   percorrer Title → Main → Story → Tutorial automaticamente.

### O que isso compra

| hoje | com o BEPC |
|---|---|
| 1 pergunta por viagem ao console | milhares de quadros verificados por segundo |
| "a GF está acelerada" | `quadro 312: esperado gf=14, obtido gf=7` |
| geometria conferida a olho na TV | PNG 640×448 diffável contra referência |
| regressão descoberta na TV | regressão barrada antes de gerar ELF |
| validação de áudio só por ouvido | asserção sobre amostras ouvidas |

Isso **não substitui** o teste em hardware — substitui as 9 em cada 10
viagens ao console que hoje servem só para responder uma pergunta
aritmética.

### Estado da construção

Já iniciado em `host/shim/`: copiados os cabeçalhos reais do PS2SDK
que são declarações puras (`draw.h`, `draw_buffers.h`,
`draw_primitives.h`, `draw_sampling.h`, `draw_tests.h`, `graph.h`,
`graph_vram.h`, `gs_psm.h`, `gs_gp.h`, `gif_tags.h`, `gif_registers.h`,
`packet.h`, `libpad.h`, `audsrv.h`, `dma_tags.h`, `math3d.h`,
`tamtypes.h`). Faltam os substitutos de `kernel.h`, `timer.h`,
`sifrpc.h`, `loadfile.h`, `iopcontrol.h`, `delaythread.h`, `dma.h`
e a implementação do interpretador GIF.

---

## 4. Os assets de runtime: onde estão, e como verificá-los

O `main.c` abre 21 caminhos em `mass:/`. Os assets de runtime que ficam em
`mass:/FNFPS2/assets/` **não vivem no repositório**: são texturas e áudio já
convertidos, cerca de 65 MB, então ficam no Google Drive.

**Resolvido em 2026-10-15.** A pasta pedida no item 6 abaixo está no Drive, e
ela contém duas gerações de `assets/`: a mais nova,
`1XEb6Q9tRfOZU5iGjnXfYyxFzpCicYfD3`, é a que tem todos os 16 arquivos que o
runtime lê, com os nomes que o `main.c` usa hoje. A geração anterior
(`SAIDA_PS2/assets/`) usa nomes antigos — `bf.frames` em vez de
`bf_frames.lz4f`, `mainstage_tutorial.rgba` em vez de
`mainstage_tutorial_parallax.rgba` — e não serve.

| asset | na pasta nova? |
|---|---|
| `bf_frames.lz4f` | sim (1.239.417 B) |
| `gf_frames.lz4f` | sim (1.375.989 B) |
| `mainstage_tutorial_parallax.rgba` | sim (524.288 B) |
| `tutorial_hud_official_320x256_gsalpha.rgba` | sim (327.680 B) |
| `menu_cache.rle` | sim (1.623.445 B) |
| `font.rgba` | sim (294.912 B) |
| `font.widths` | sim (96 B) |
| `freakyMenu_48000.pcm` | sim (21.687.068 B) |
| `menu_sfx.pcm` | sim (281.088 B) |
| `audio_stems.pcm` | sim (25.804.800 B) |
| `test.chart` | sim (1.364 B) |
| `title_alphabet.rgba` | sim (294.912 B) |
| `title_newgrounds.rgba` | sim (126.700 B) |
| `title_prompt_l.rgba` | sim (393.216 B) |
| `title_prompt_r.rgba` | sim (245.760 B) |
| `title_logoBumpin.frames` | sim (4.608.000 B) |
| `title_gfDanceTitle.frames` | sim (7.219.200 B) |

`assets-manifest.json` guarda, para cada arquivo, o id no Drive e o tamanho em
bytes. `./build.sh --check-assets` confere o que está em `assets/` contra esse
manifesto: arquivo ausente é listado com seu id, e arquivo com tamanho errado é
tratado como download interrompido — que é o modo mais comum de uma cópia para
o pendrive dar errado. `--deploy` roda a mesma verificação ao preparar o cartão.

Observação: `assets/title_logoBumpin.lz4f` e
`assets/title_gfDanceTitle.lz4f` estão embutidos no ELF via
`.incbin` (`src/title_packs.S`), mas os `.frames` descomprimidos que o
runtime lê de `mass:/` são outros arquivos.

---

## 5. Plano

| Etapa | Entrega | Depende de |
|---|---|---|
| **E0** | Build reproduzido e hash-verificado | **feito** |
| **E1** | Assets de runtime no workspace | **feito** |
| **E2** | BEPC compila `main.c` nativamente, sem alterar uma linha do fonte | E1 |
| **E3** | Interpretador GIF + rasterizador do subconjunto → PNG 640×448 por quadro | E2 |
| **E4** | Relógio de áudio determinístico + pad roteirizado; suíte de asserções de timing (Bopper, Conductor, chart) | E3 |
| **E5** | Baterias de regressão contra as derivações oficiais já documentadas (73 funções, 26 pontos de telemetria) | E4 |
| **E6** | Atacar o backlog P1/P2 com o laço curto, uma viagem ao console por marco e não por hipótese | E5 |

---

## 6. O que preciso de você

Nada sobre assets: estão todos no Drive, conferidos por
`./build.sh --check-assets`.

O que segue bloqueando é a **validação no console**. O fluxo é:

    ./build.sh                 # suíte offline + build + validação do ELF
    ./build.sh --check-assets  # confere os 16 assets em assets/
    ./build.sh --deploy        # monta build/ps2/FNFPS2/

Aí copie `build/ps2/FNFPS2/` para o cartão como `mass:/FNFPS2/` e me conte o
primeiro erro que aparecer. A parte de compilar é você: este sandbox não
consegue baixar o ps2sdk (ver §10.7 em `SOURCE_ANALYSIS_0.2.105.md`).
