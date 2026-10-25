# Análise geral: o que existe, o que falta, e o plano para o jogo inteiro

Documento de **medição**, não de intenção. Todo número aqui saiu de um comando
rodado no workspace em 2026-10-25. Nada é estimativa sem estar marcado como tal.

**Branch:** `arena/4c50659b-ps2projects` · **Commit:** `b4f2f55`

---

## 1. O que existe hoje, medido

### 1.1 Código

| | |
|---|---|
| Linhas de código real | **3.652** em 8 arquivos |
| Funções | **200** |
| Os 5 `*_irx.c` | 6.269 linhas de **dado** (bytes dos módulos do SDK), não comportamento |

### 1.2 Estados do jogo

`ui_state` tem 4 valores alcançáveis, e `target_state` só recebe 4 valores:

```
target_state = 0   título
target_state = 6   menu principal
target_state = 7   story menu
target_state = 8   tutorial      <-- o único estado jogável
```

**Só o tutorial é jogável.** Não existe estado de gameplay para as 27 músicas.
Escolher uma semana no story menu não leva a uma música.

### 1.3 Conteúdo do jogo original, já no repositório

| | Quantidade | Estado |
|---|---|---|
| Músicas | **27** (com metadata completa em `assets-data/songs/`) | no registro |
| Charts convertidos | **81** (27 músicas × 3 dificuldades) | **prontos e validados** |
| Notas no total | **34.325** (maior chart: 1.035, `2hot-hard`) | cabem de sobra |
| Personagens | **46** | no registro, **sem pack** |
| Stages | **21** | no registro, **sem pack** |

Os 81 charts ocupam **672 KB** e somam 34.325 notas. O carregador deles
(`chart.c`, formato v3 e v4) está **provado por execução** — 249 checagens,
0 falhas, cobertura por função com 0 funções sem executar.

**Conclusão importante: chart não é gargalo.** O dado de jogo mais volumoso já
está convertido, validado e cabe folgado.

### 1.4 Sistemas de gameplay presentes

Contagem de menções no `main.c`:

| Sistema | Menções | Situação |
|---|---|---|
| score | 9 | só HUD |
| health | 2 | só ícone |
| miss | 5 | mínimo |
| combo | 5 | mínimo |
| **accuracy** | **0** | **não existe** |
| **judgement** | **0** | **não existe** |
| **rating** | **0** | **não existe** |
| **results** | **0** | **não existe** |
| freeplay | 3 | menção apenas |

O gameplay é `tutorial_notes_update/draw/reset` — específico do tutorial.
Personagens e stage vêm de `g_official_mainstage_chars`, uma tabela
**hardcoded** do tutorial (linha 874 de `main.c`).

### 1.5 A restrição que define o projeto: VRAM

O GS do PS2 tem **4 MB de VRAM**. A configuração atual aloca:

| Buffer | Tamanho | Bytes |
|---|---|---|
| `fb[0]` | 640×448 PSM32 | 1.146.880 |
| `fb[1]` | 640×448 PSM32 | 1.146.880 |
| `tex` | 320×256 PSM32 | 327.680 |
| `tex2` | 320×256 PSM32 | 327.680 |
| `gftex` | 256×256 PSM32 | 262.144 |
| `g_gftex16` | 320×64 PSM16 | 40.960 |
| `stagetex` | 512×256 PSM32 | 524.288 |
| `fonttex` | 384×256 PSM32 | 393.216 |
| **TOTAL** | | **4.169.728** |

Isso é **99,4% dos 4 MB**, com o código do próprio jogo comentando
*"VRAM livre apos o fonttex: 163.840 B"*. A diferença entre os meus 24.576 B de
soma bruta e os 163.840 B do alocador real é o alinhamento de bloco/página —
o número do código é o autoritativo, o meu é a confirmação da ordem de
grandeza.

**Sobra 160 KB de VRAM.** Não cabem 46 personagens animados, 21 stages e os
note skins. É aqui que "resolução menor" deixa de ser preferência e passa a ser
pré-requisito.

---

## 2. O que "portar todo o jogo" exige

Em ordem de dependência, não de preferência:

| # | Item | Situação | Risco |
|---|---|---|---|
| 1 | **Orçamento de VRAM** | 160 KB livres | **bloqueia tudo** |
| 2 | Carregador genérico de packs de personagem | não existe (tutorial é hardcoded) | alto |
| 3 | Carregador genérico de stage | não existe | alto |
| 4 | Estado de gameplay genérico | não existe (só o 8) | alto |
| 5 | Song select (semana → música → dificuldade) | não existe | médio |
| 6 | Sistemas: scoring, health, miss, combo, **accuracy**, **judgement**, **rating**, **results** | parciais ou ausentes | médio |
| 7 | Áudio das 27 músicas em PCM | só o tutorial | médio |
| 8 | Geração dos packs (46 personagens, 21 stages) | ferramenta não está em `tools/` | médio |
| 9 | Menu de pausa, tela de resultados, transições | não existem | baixo |

O item 1 vem primeiro porque **nenhum dos outros cabe sem ele**.

---

## 3. A decisão de resolução, quantificada

Rodei as contas. O que cada opção compra de VRAM livre:

| Configuração | VRAM usada | Livre | Ganho |
|---|---|---|---|
| **ATUAL** 640×448 PSM32 | 99,4% | **163.840 B** | — |
| 640×448, framebuffers PSM16 | 72,1% | 1.171.456 B | **7,1×** |
| 512×384 PSM32 | 82,2% | 745.472 B | 4,5× |
| **512×384, fb PSM16** | **63,5%** | **1.531.904 B** | **9,3×** |
| 480×448, fb PSM16 | 65,2% | 1.458.176 B | 8,9× |

A alavanca mais barata é **PSM16 nos framebuffers**: metade dos bytes, sem
perder um pixel de resolução. 640×448 PSM16 sozinho já multiplica o VRAM livre
por 7.

Combinando com 512×384, chega-se a **1,5 MB livre** — suficiente para os
personagens e stages de uma música de cada vez, com troca por streaming.

**Recomendação: 512×384 com framebuffers PSM16**, por três razões medidas:

1. É a maior sobra de VRAM (1,53 MB, 9,3× a atual).
2. 512×384 é modo nativo do GS — sem escalonamento por hardware, sem carta de
   bandeira.
3. PSM16 (RGBA1555 ou RGB565) é o que o próprio código já usa em
   `g_gftex16`, então o caminho de upload já existe e está testado.

O custo é qualidade de cor em gradientes. Dá para mitigar com dithering, que o
GS faz por hardware.

---

## 4. Plano, em fases

Cada fase tem um **portão de saída medido**. Se o portão não passar, a fase
não acabou — não se passa para a próxima com algo em aberto.

### Fase 0 — Travamento no console (pendência atual)

O jogo abre, mostra o primeiro texto e congela. O harness passa 1401 quadros
sem travar, então **não é lógica de jogo** — é algo de hardware que o harness
não emula (audsrv, USB, VSYNC).

- Portão: `BOOT.txt` dizendo em que marco parou, além do `passo 66: FRAME`.

### Fase 1 — VRAM (destrava tudo)

Mudar `SCREEN_W/H` e o PSM dos framebuffers, com o harness medindo antes e
depois.

- Portão: harness passando com a nova resolução, e o telemetry mostrando o
  endereço final dos buffers dentro dos 4 MB.
- Risco: todos os `upload_raw` e `setup_texture_dims` assumem PSM32 em vários
  lugares. É varredura mecânica, e o harness pega erro na hora.

### Fase 2 — Pack genérico de personagem e stage

Generalizar o que o tutorial faz. O formato `CFZ4` (mágico + versão + contagem
+ bytes por quadro, quadros LZ4) já existe e já é validado; falta o carregador
deixar de ser específico.

- Portão: carregar um personagem e um stage que **não** sejam os do tutorial,
  com os bytes conferidos por `tools/check_real_assets.py`.

### Fase 3 — Estado de gameplay genérico (estado 9)

Um estado que carrega qualquer chart dos 81 já convertidos.

- Portão: jogar `bopeebo-hard` do início ao fim no harness, com as notas
  chegando na ordem certa.

### Fase 4 — Sistemas de jogo

Scoring, health, miss, combo, accuracy, judgement, rating, results.

- Portão: um chart conhecido, com entrada scriptada, produzindo pontuação e
  rating conferíveis contra o cálculo feito no PC.

### Fase 5 — Song select e o resto

Semana → música → dificuldade, pausa, resultados, transições.

- Portão: atravessar título → menu → semana → música → results no harness.

---

## 5. Sobre "garantia total de inexistência de erro"

Você pediu garantia total. Não posso dar, e dizer que sim seria mentira — eu
já errei três vezes prometendo certeza sem medição.

O que posso dar, e é melhor que promessa:

1. **Cada afirmação medida.** O documento que você está lendo não tem número
   estimativo. Onde não medi, está escrito que não medi.
2. **Portão por fase.** Nada avança com algo em aberto. Se a Fase 1 quebrar o
   harness, ela não acabou.
3. **O harness como rede.** Ele compila o jogo real contra o `draw` real do
   ps2sdk e pega estouro de pacote, DMA acima de `QWC_MAX, escrita em zona de
   guarda e asset que não abriu — no PC, antes do console. É o que impede
   corromper a memória do PS2 em silêncio.
4. **ASan + UBSan** sobre o jogo inteiro (`tools/run_harness_asan.sh`).

O risco que **nenhuma** dessas camadas cobre é o de hardware puro: audsrv,
USB, VSYNC, timing do IOP. É justamente onde o jogo trava hoje. Para isso, a
prova é o console, e a preparação é o `BOOT.txt` com marcos suficientes para
dizer exatamente onde parou.

---

## 6. O que eu preciso de você

Antes de executar a Fase 1, duas decisões que são suas, não minhas:

1. **A resolução.** Recomendo 512×384 com fb PSM16, mas se você preferir
   640×448 PSM16 (mantém a resolução, aceita 1,17 MB em vez de 1,53 MB), dá
   para fazer. A diferença é qualidade de cor contra espaço.

2. **A ordem.** A Fase 0 (travamento no console) é o que está te bloqueando
   para testar. A Fase 1 (VRAM) é o que bloqueia o jogo inteiro. Se o objetivo
   é o jogo completo, a Fase 1 primeiro evita retrabalho; se é fazer o que
   existe hoje funcionar no console, a Fase 0 primeiro.

---

## 7. O modelo de carregar/descarregar (adendo)

Você perguntou se não íamos carregar o jogo inteiro de uma vez, mas ir
carregando e descarregando ao entrar nas fases. **A resposta é sim — e a
medição mostra exatamente onde o port quebra esse modelo hoje.**

### 7.1 Onde o port já faz certo

`tutorial_packs_free()` dá `free()` de verdade nos packs do tutorial, que são
`malloc`'ados do pendrive ao entrar e liberados ao sair. O áudio usa o anel de
256 KB com leituras de 32 KB, streamado. Ou seja, **o caminho de streaming já
existe e funciona**.

### 7.2 Onde o port quebra o modelo — dois pontos medidos

**Ponto 1: a VRAM é alocada uma vez e nunca liberada.**

As 6 chamadas de `graph_vram_allocate` estão **todas** na inicialização
(linhas 1346-1352 de `main.c`), e **não existe `graph_vram_free` em lugar
nenhum** do código:

```
1346: fb[0] ... graph_vram_allocate(SCREEN_W,SCREEN_H,GS_PSM_32,GRAPH_ALIGN_PAGE)
1348: tex   ... graph_vram_allocate(320,256,GS_PSM_32,GRAPH_ALIGN_BLOCK)
1349: tex2  ... graph_vram_allocate(320,256,GS_PSM_32,GRAPH_ALIGN_BLOCK)
1350: gftex ... graph_vram_allocate(256,256,GS_PSM_32,GRAPH_ALIGN_BLOCK)
1351: stagetex ... graph_vram_allocate(512,256,GS_PSM_32,GRAPH_ALIGN_BLOCK)
1352: fonttex  ... graph_vram_allocate(384,256,GS_PSM_32,GRAPH_ALIGN_BLOCK)
```

Nada disso sai. Os 8 buffers somam 4.169.728 dos 4.194.304 B do GS — 99,4% — e
o próprio código comenta *"VRAM livre apos o fonttex: 163.840 B"*. Sobram
160 KB, e não há mecanismo para devolver espaço.

**Ponto 2: 2,93 MB de packs linkados dentro da ELF.**

`src/title_packs.S` e `src/story_packs.S` usam `.incbin`, que copia os arquivos
para `.rodata`:

| Pack | Bytes | Usado em |
|---|---|---|
| `title_gfDanceTitle.lz4f` | 1.549.455 | só no título |
| `title_logoBumpin.lz4f` | 658.996 | só no título |
| `story_gf_idle.lz4f` | 483.303 | só no story |
| `story_bf_idle.lz4f` | 238.038 | só no story |
| **TOTAL** | **2.929.792** | 2 dos 4 estados |

Esses 2,93 MB ficam na RAM **o tempo todo**, esteja você no título, no menu, no
story ou no tutorial. É o único lugar onde o "carregar tudo" acontece de fato, e
é a primeira coisa a consertar.

### 7.3 O orçamento, medido

| Categoria | Bytes | % da RDRAM (32 MB) |
|---|---|---|
| Permanente (`menu_cache.rle`, sfx, cache do menu, packs na ELF) | 7.760.289 | 23,1% |
| Scratch (buffers de decode, sempre alocados) | 13.652.092 | 40,7% |
| Streaming (áudio + packs, por estado) | 5.841.006 | 17,4% |
| **Se tudo carregado** | **27.253.387** | **81,2%** |
| Piso permanente + scratch | 21.412.381 | sobra **11,58 MB** |

**A conclusão que inverte a prioridade da seção 3:** a RDRAM **não** é o
gargalo. Mesmo carregando tudo, são 81% de 32 MB, e o piso fixo deixa 11,58 MB
livres. O gargalo é a **VRAM**, com 160 KB.

Isso quer dizer que a resolução menor **não é exigência do carregamento** — é
exigência do que precisa estar desenhável ao mesmo tempo (personagem, stage,
notas, HUD). E que a primeira medida de arquitetura não é mexer em resolução:
é **parar de linkar 2,93 MB na ELF** e passar a carregá-los do pendrive por
estado, que é o que você propôs.

### 7.4 A arquitetura que segue daí

```
boot:      aloca os buffers de VRAM UMA vez (framebuffers, tex, tex2, gftex,
           stagetex, fonttex) -- esses são os "slots" fixos
por estado: carrega do pendrive os packs daquele estado para a RAM,
           faz upload nos slots de VRAM que o estado precisa,
           e ao sair dá free() na RAM e marca o slot como livre
```

Três consequências práticas:

1. **Um gerenciador de slots de VRAM** — quais dos 6 slots estão em uso, por
   quem, e quando podem ser reutilizados. Hoje isso é implícito e
   hardcoded por estado.
2. **Fim do `.incbin`** para os 4 packs de título/story: passam a vir do
   pendrive, como já acontece com os do tutorial.
3. **Um pack por vez na VRAM** — personagem, stage e notas dividem os slots,
   com upload sob demanda. É o que permite 46 personagens e 21 stages sem
   estourar 4 MB.

### 7.5 Plano revisto

| Fase | Item | Portão de saída |
|---|---|---|
| 0 | Travamento no console | `BOOT.txt` dizendo onde parou, além de `passo 66: FRAME` |
| 1 | **Tirar os 4 packs do `.incbin`**, carregar do pendrive por estado | harness passa; ELF encolhe ~2,93 MB; `check_real_assets.py` valida |
| 2 | **Gerenciador de slots de VRAM** (alocar/ocupar/liberar) | teste de unidade no host: alocar todos os slots, liberar, realocar |
| 3 | Pack genérico de personagem e stage | carregar personagem e stage que **não** sejam os do tutorial |
| 4 | Estado de gameplay genérico (estado 9) | jogar `bopeebo-hard` do início ao fim no harness |
| 5 | Sistemas: scoring, health, miss, combo, accuracy, judgement, rating, results | chart conhecido + entrada scriptada = pontuação conferível no PC |
| 6 | Song select, pausa, resultados, transições | atravessar título → semana → música → results no harness |

A Fase 1 vem antes da resolução porque é a que implementa o modelo que você
descreveu, é medida (2,93 MB), e não tem risco de regressão visual — os packs
continuam os mesmos, só mudam de onde vêm.

### 7.6 Ressalva importante sobre o workspace

Entre turnos, o workspace foi restaurado e **perdeu dois diretórios
gitignored**: `google_drive/` (com o tarball do toolchain, 42 MB) e os assets
de runtime. Consequência medida agora:

- `sh test/rodar-prova.sh` → **funciona** (249 checagens, 0 falhas)
- `sh tools/run_harness.sh` → **funciona** com assets sintéticos, que ele mesmo gera
- **build para PS2 → não funciona**, por falta do toolchain

O trabalho não foi perdido: os 12 commits estão no remoto, e o reset local para
`origin/arena/4c50659b-ps2projects` restaurou tudo. Para voltar a buildar para
PS2 é preciso reobter `PS2DEV_EE_MIN_FNF.tar.xz` em `google_drive/` (o
`assets-manifest.json` documenta a pasta e os ids de onde vêm os assets).

---

## 8. A medição que decide o port (adendo 2)

Esta seção responde, com dados reais de `assets-data/`, à pergunta que a seção
7 deixou em aberto: **quantas texturas vivas uma música precisa, e quanto de
VRAM elas custam.**

### 8.1 Os 21 palcos, medidos

Cada palco tem `props` (camadas de fundo, público, fumaça, carros) e 3
personagens. Contando props + personagens + 4 setas + 6 elementos de HUD:

| Palco | props | chars | texturas vivas |
|---|---|---|---|
| tankmanBattlefield | 18 | 3 | **31** |
| phillyStreetsErect | 15 | 3 | 28 |
| sserafim | 15 | 3 | 28 |
| phillyStreets | 14 | 3 | 27 |
| limoRideErect / mainStageErect | 10 | 3 | 23 |
| mainStage | 3 | 3 | 16 |
| spookyMansion | 1 | 3 | 14 |
| **média** | 8,0 | 3 | **21,0** |

O port hoje tem **5 texturas fixas** (`tex`, `tex2`, `gftex`, `stagetex`,
`fonttex`). O pior caso pede 31. **São 6,2× mais slots do que existem.**

### 8.2 O custo em VRAM, com as dimensões reais

`assets-data/stage-image-sizes.json` tem as dimensões reais de cada imagem.
Contando `w × h × 4` (PSMCT32) e quebrando na largura em tiles de 1024 px —
o limite de textura do GS:

| Palco | VRAM dos props | vs. 4 MB |
|---|---|---|
| limoRideErect | 1.619.192.832 | **386×** |
| mallXmasErect | 1.370.250.912 | 327× |
| sserafim | 1.294.190.624 | 309× |
| tankmanBattlefield | 1.247.157.856 | 297× |
| mainStage | 276.971.520 | 66× |
| spookyMansion | 283.281.408 | 68× |

**Nenhum palco cabe em resolução nativa.** O melhor caso ainda é 66× a VRAM
inteira. A diferença é de três ordens de magnitude — não é ajuste, é
reengenharia de asset.

### 8.3 Slot não é byte — e isso importa

`limoRideErect` tem 5 sprites apontando para **o mesmo atlas**
(`limo/henchmen`, 2048×2048): 5 slots, 1 textura. `mainStage` tem 3 props e 3
personagens, todos distintos.

Ou seja: **contagem de slots e contagem de bytes são problemas diferentes**, e
o `vram_cache.c` resolve o primeiro (despejo por LRU por chave) mas não o
segundo.

### 8.4 Quanto sobra por textura

| Framebuffers | Sobra p/ texturas | tankman (31) | mainStage (16) | school (21) |
|---|---|---|---|---|
| 640×448 PSM_32 (atual) | 1.900.544 B | 61.307 B = 247×247 | 118.784 B = 344×344 | 90.502 B = 300×300 |
| 512×384 PSM_16 | 3.407.872 B | 109.931 B = 331×331 | 212.992 B = 461×461 | 162.279 B = 402×402 |

Texturas de ~250-330 px de lado. É o tamanho típico de jogo de PS2 — **cabe**,
mas exige que os atlas de 4096×4096 sejam **fatiados por quadro de animação e
reduzidos em tempo de build**, não enviados inteiros.

### 8.5 A conclusão, e o que ela corrige

A intuição de que "resolução menor ajuda" está **metade certa**:

- **Resolução de tela** ajuda pouco: de 640×448 PSM_32 para 512×384 PSM_16
  quase dobra a VRAM de textura (1,9 → 3,4 MB). É ganho real, mas de 1,8×.
- **Resolução de textura** é o que decide: o gargalo são os atlas de 4096²,
  que precisam virar tiles de ~256 px por quadro de animação.

E o gargalo de **contagem** (31 vs 5 slots) é independente dos dois — resolve-se
com o `vram_cache.c`, que já existe e já está provado.

Portanto a arquitetura correta tem **três** peças, não uma:

1. **Fatiar e reduzir os atlas em tempo de build** — extrair quadro por quadro,
   limitar a 256-512 px, gerar pack por palco. É aí que os 386× encontram o
   1,9-3,4 MB disponível.
2. **Gerenciar slots com `vram_cache.c`** — despejo por LRU, que é o que
   permite 31 texturas vivas em 4 MB.
3. **Carregar/descarregar por estado** — a seção 7, que já é o modelo certo e
   hoje está quebrado nos dois pontos medidos lá.

### 8.6 O plano revisto de novo

| Fase | Item | Portão |
|---|---|---|
| 0 | Travamento no console | `BOOT.txt` localizando a parada |
| 1 | Packs do `.incbin` → pendrive | ELF encolhe 2.929.792 B; harness passa |
| 2 | **Fatiar atlas em build** | pack por palco ≤ orçamento medido em 8.4 |
| 3 | **Ligar `vram_cache.c` no `main.c`** | teste: alocar 31 slots, estourar, despejar, realocar |
| 4 | Estado de gameplay genérico | `bopeebo-hard` do início ao fim no harness |
| 5 | Scoring, health, miss, combo, accuracy, judgement, rating, results | chart conhecido + entrada scriptada |
| 6 | Song select, pausa, resultados, transições | título → semana → música → results |

A Fase 2 é nova e é a que a medição obrigou: sem ela, nenhuma das outras
importa, porque **não existe palco do jogo que caiba na VRAM do PS2**.
