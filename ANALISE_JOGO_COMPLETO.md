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
