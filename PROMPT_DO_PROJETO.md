# Prompt do projeto — port de Friday Night Funkin' para PlayStation 2

> Use este texto como brief. Ele descreve **o que é o projeto, o que já está
> medido, e as regras que não se negociam**. Ele **não** diz como implementar —
> as decisões de arquitetura são suas, e devem ser justificadas por medição.

---

## 1. A ideia

Existe um port de **Friday Night Funkin'** para PlayStation 2, escrito em C
contra o **ps2sdk oficial**, rodando no hardware real (EE + GS + DMA + USB +
audsrv).

O jogo original é feito em Haxe/flixel. Este port não é uma reimplementação
aproximada: ele reproduz o comportamento do original, incluindo constantes que
vieram dos fontes do jogo (por exemplo `CHART_BOP_DECAY 0.95f` de
`PlayState.hx:1217`, `CHART_DEFAULT_BOP_INTENSITY 1.015f` de
`Constants.DEFAULT_BOP_INTENSITY`).

O objetivo é **o jogo inteiro**: 27 músicas, 46 personagens, 21 palcos, 3
dificuldades. Hoje só o tutorial é jogável.

A documentação oficial do ps2sdk está no repositório, em
`docs/ps2sdk-compendium/` (11 partes) e `PS2SDK-Complete-Documentation.md`.
**Toda decisão de gráfico, DMA, textura ou áudio deve se apoiar nela, não em
suposição sobre como o GS funciona.**

---

## 2. Estado medido (não é estimativa)

| | |
|---|---|
| Linhas de código | 3.652 em 8 arquivos |
| Funções | 200 |
| Estados de UI | `ui_state` ∈ {0 título, 6 menu, 7 story, 8 tutorial} |
| **Jogável** | **só o tutorial** |
| Charts | 81 convertidos (27 músicas × 3 dificuldades), 672 KB, 34.325 notas |
| Personagens | 46 no registro, **sem pack** |
| Palcos | 21 no registro, **sem pack** |
| accuracy / judgement / rating / results | **zero menções no código** |

### O gargalo, medido

Os 8 buffers de VRAM somam **4.169.728 dos 4.194.304 B** do GS — **99,4%** — com
o próprio código comentando *"VRAM livre apos o fonttex: 163.840 B"*. Sobram
160 KB, e **não existe `graph_vram_free` em lugar nenhum**: as 6 chamadas de
`graph_vram_allocate` estão todas na inicialização (linhas 1346-1352 de
`main.c`).

Além disso, `src/title_packs.S` e `src/story_packs.S` usam `.incbin`, então
**2.929.792 B de packs ficam em `.rodata` o tempo todo**, usados por apenas 2
dos 4 estados.

### O módulo que já resolve metade disso

`src/engine/vram_cache.c` é um alocador de VRAM com despejo por
menos-usado-recentemente. Está **provado por execução**: 12 funções, 100% de
cobertura de linhas, zero funções sem executar.

O cabeçalho dele diz, com palavras do próprio autor:

> *"O port atual tem CINCO texturas fixas: tex, tex2, gftex, stagetex e
> fonttex. Cada personagem ou prop animado precisa de uma, e isso limita a nove
> palcos do jogo, entre eles o tankmanBattlefield, que sozinho pede treze.
> **Reduzir resolução nao cria slot: o que falta é quantidade de texturas vivas,
> não tamanho.** Este modulo substitui os slots fixos."*

**`main.c` usa esse módulo zero vezes.** Só o teste usa.

### A RDRAM não é o gargalo

| Categoria | Bytes | % de 32 MB |
|---|---|---|
| Permanente | 7.760.289 | 23,1% |
| Scratch (buffers de decode) | 13.652.092 | 40,7% |
| Streaming (por estado) | 5.841.006 | 17,4% |
| **Tudo carregado** | **27.253.387** | **81,2%** |

Sobra 11,58 MB. Ou seja: **carregar tudo não estoura a RAM** — o problema é o
que precisa estar *desenhável ao mesmo tempo* na VRAM.

---

## 3. As três camadas de prova que já existem

Use-as. Elas são o que separa afirmação de medição.

| Camada | O que prova | Como rodar |
|---|---|---|
| Prova por execução | 89 funções dos 6 módulos puros, com cobertura por função | `sh test/rodar-prova.sh` |
| Harness de link + execução | `main.c` inteiro, compilado contra o `draw`/`packet` **real** do ps2sdk, rodando no PC com roteiro de botões que atravessa o jogo | `sh tools/run_harness.sh 1400 build/harness_assets` |
| ASan + UBSan | o jogo inteiro com todos os buffers instrumentados | `sh tools/run_harness_asan.sh` |

O harness pega, no PC, o que corromperia a memória do PS2 em silêncio:
estouro de pacote de quadro, envio DMA acima de `QWC_MAX`, escrita em zona de
guarda, e asset que não abriu. Resultado da última rodada completa:

```
quadros executados ............ 1401
ESTOUROS DE PACOTE ............ 0
escritas na zona de guarda .... 0
envios DMA acima de QWC_MAX ... 0
botoes do roteiro executados . 12 de 12
RESULTADO: PASSOU
```

**Nada entra sem passar por essas camadas.**

---

## 4. As regras que não se negociam

1. **Tudo é portado segundo a documentação oficial do ps2sdk**
   (`docs/ps2sdk-compendium/`). Se uma decisão de gráfico, DMA, textura ou
   áudio não pode ser citada na documentação, ela não está pronta.

2. **Nada é criado sem motivo.** Só três motores justificam código novo:
   - **otimizar** ou portar melhor para o PS2;
   - **corrigir bug**;
   - **implementar de fato algo do jogo original** que está faltando.

   Não existe "vou fazer deste jeito porque prefiro". Se não é um dos três, não
   se faz.

3. **Nada é afirmado sem medição.** Um número que não saiu de um comando não
   entra em documento nenhum. Onde não se mediu, escreve-se que não se mediu.

4. **A convenção se lê do fonte, não se adivinha.** Este projeto já perdeu
   rodadas inteiras por suposição: índices de easing que não existiam, `p0`/`p1`
   de um evento invertidos, um carregador que devolvia `-1` onde se esperava
   outra coisa. Antes de afirmar como algo funciona, ler.

5. **Nada avança com portão em aberto.** Cada fase termina quando a medição
   passa, não quando o código compila.

---

## 5. O que já está provado e não se mexe sem motivo

- O carregador de charts (formato v3 e v4, checksum FNV-1a, tabelas de strings
  e blocos) — 249 checagens, 0 falhas.
- As 13 easings, com a matemática de cada uma conferida contra a fórmula do
  flixel.
- O registro de músicas, validado contra `assets-data/` e os JSON do jogo.
- O anel de áudio, com a thread de produtor rodando de verdade.
- A fila de I/O fatiada, que foi o que resolveu a corrupção do `usbhdfsd`.

---

## 6. Perguntas em aberto — decidir por medição, não por preferência

1. **Slots de VRAM.** O `vram_cache.c` já existe e está provado, mas `main.c`
   não o usa. Qual é o número real de texturas vivas que uma música precisa, e
   em que momento do quadro? Isso se mede, não se estima.

2. **Os packs do `.incbin`.** 2.929.792 B ficam permanentes na ELF, usados por
   2 dos 4 estados. Passar a carregá-los do pendrive por estado encolhe a ELF e
   libera RAM — mas muda o caminho de init. Qual é o custo real de tempo de
   carga, medido, contra o ganho?

3. **Ordem.** A Fase 0 (o jogo trava no console depois de mostrar o primeiro
   texto) é o que bloqueia testar. A Fase do alocador de VRAM é o que bloqueia
   o jogo inteiro. Qual vem primeiro, e por quê?

4. **O travamento atual.** O harness passa 1400 quadros sem travar, então não é
   lógica de jogo. É hardware que o harness não emula: audsrv, USB, VSYNC,
   timing do IOP. O `BOOT.txt` para em `passo 66: FRAME`. O que vem depois
   desse marco?

5. **Resolução.** A intuição de que "resolução menor ajuda" é parcialmente
   falsa: o próprio `vram_cache.h` diz que reduzir resolução não cria slot. Mas
   resolução consome VRAM de framebuffer, e framebuffer não é textura. Qual é a
   conta real — e ela depende da resposta da pergunta 1.

---

## 7. O que não prometer

Não existe garantia de zero erros. Quem promete isso sem medir já errou neste
projeto três vezes seguidas.

O que existe no lugar da promessa:

- cada afirmação medida;
- portão por fase;
- as três camadas de prova acima, que pegam no PC o que destruiria a memória
  do PS2 em silêncio.

O risco que **nenhuma** camada cobre é hardware puro: audsrv, USB, VSYNC,
timing do IOP. Para isso a prova é o console, e a preparação é o `BOOT.txt` com
marcos suficientes para dizer exatamente onde parou.

---

## 8. Ressalva sobre o estado do workspace

Entre turnos, o workspace foi restaurado mais de uma vez e perdeu diretórios
gitignored: `google_drive/` (com o tarball do toolchain ps2dev, 42 MB) e os
assets de runtime. Um commit local não pushado também foi perdido por um
`reset --hard` — **a lição é commitar e pushar na mesma volta**.

O histórico não foi perdido: os commits estão no remoto
`origin/arena/4c50659b-ps2projects`.

Consequência medida:

- `sh test/rodar-prova.sh` → funciona (249 checagens, 0 falhas)
- `sh tools/run_harness.sh` → funciona, com assets sintéticos que ele gera
- **build para PS2 → não funciona**, por falta do toolchain

`assets-manifest.json` documenta a pasta do Drive e os ids de onde vêm os
assets. Reobter o tarball é o primeiro passo para voltar a buildar para PS2.
