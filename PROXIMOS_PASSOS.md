# PRÓXIMOS PASSOS — detalhado

Ordenado por prioridade. Cada item diz **o que já se sabe** (com fonte) e **o que
falta descobrir**. Nada aqui é palpite.

---

## P0 — Confirmar que a 0.2.111 funciona no console

**Por que é prioridade zero:** as builds 0.2.108, 0.2.109 e 0.2.110 não abriram.
A 0.2.111 corrige a causa raiz do log vazio (reabertura tardia do arquivo) e
adiciona marca por quadro. **Nenhuma dessas duas coisas foi confirmada em
hardware.** Até ser, nenhuma outra afirmação sobre o estado do projeto é segura.

**O que pedir ao usuário:** rodar a 0.2.111 e devolver dois arquivos:

- `mass:/FNFPS2/FNF_COLHEITA.txt` — se vier com conteúdo, o log funciona;
- `mass:/FNFPS2/BOOT.txt` — diz em qual quadro o jogo parou, se parou.

**Como interpretar:**

| `BOOT.txt` diz | Significa |
|---|---|
| `passo 30: F0_FRAMEBUFFER_SET` e depois `passo 31: FRAME,1,...` | boot completo, rodando |
| para num `passo N` de boot (META, PAD, CACHE, AUDIO, GS, TITLE) | travou no boot, no passo N |
| para num `passo N: FRAME,k,...` | travou no quadro k |
| arquivo não existe | o pendrive não montou — problema de install ou de `reset_iop()` |

---

## P1 — ❌ DESCARTADO: "o menu desenha cada item duas vezes" NÃO EXISTE

**Esta descoberta estava registrada aqui como o problema número 1 do projeto.
Ela é FALSA e veio de um defeito meu. Fica documentada porque a causa do erro é
a parte mais útil de lembrar.**

**O que eu afirmei:** que no estado 6 um quadro tinha 8 sprites em vez de 4, cada
item desenhado duas vezes, na ordem 1,2,3,4 / 1,2,3,4, com geometria idêntica.

**O que a medição mostra:** o log do harness continha **quatro execuções** no
mesmo arquivo — a linha `P,SHUTDOWN` aparecia 4 vezes — porque `telemetry.c`
abria o `FNF_COLHEITA.txt` com `O_APPEND`. Li o quadro 364 duas vezes, uma em
cada execução, e interpretei como desenho duplo.

**A prova:** com o log aberto por `O_TRUNC` (uma rodada, um arquivo), o quadro
364 tem **5 sprites** — 1 fundo e 4 itens, cada um uma vez só. Não existe
segunda passagem, não existe duplicação de alpha, e o laço de itens de
`src/main.c` está correto: para `selection=0` ele gera mi = 1,2,3,4,0, cada um
uma vez.

**Corrigido em 0.2.112** (commit `d2eed51`), com teste de regressão em
`test/run_tests.sh` que proíbe os dois falsos positivos: item repetido dentro do
mesmo quadro, e menu com "cara diferente" entre visitas.

**O que ainda NÃO sei:** de onde vem a "linha estranha abaixo dos botões" que o
usuário reporta desde o início. Não tenho dado que a explique. Nas 6 capturas de
hardware da 0.2.106 o único conteúdo fora da faixa visível (56..391) eram **3
pixels escuros na linha 6**, em x=256..258 — no TOPO da tela, não embaixo dos
botões. Não tiro conclusão nenhuma a partir daí.

---

## P2 — ❌ DESCARTADO (localmente): o menu NÃO volta diferente

**O sintoma:** o usuário reporta, desde a 0.2.105, que ao voltar do modo
história para o menu principal os botões aparecem bugados.

**O que foi medido em 0.2.112:** comparando o **conjunto de posições por visita**
(um bloco de quadros consecutivos no estado 6), e não a lista por quadro:

```
2 visitas ao menu (blocos consecutivos no estado 6):
  visita 0: quadros 364..497  4 posições
  visita 1: quadros 500..514  4 posições
o menu tem a MESMA cara nas 2 visitas:
  [(94, 81), (181, 57), (255, 58), (332, 52)]
```

**Por que o alarme antigo era falso:** a contagem de sprites por quadro varia de
propósito. Ao confirmar um item, `menu_flicker_step()` (main.c:856) pisca o item
selecionado **16 vezes** (`g_fl_item_left=16`, `g_fl_item_tl=0.06`) e some em
metade desses quadros. Um quadro com 3 itens em vez de 4 é a animação do
confirmar, não um bug. Nos quadros 498-499 só o fundo aparece — é a transição.

**O que falta:** o usuário precisa descrever melhor o sintoma, ou mandar uma
captura/log do console. "Bugado" pode ser: cor errada, texto trocado, posição
errada, item faltando, ou animação travada — e cada uma dessas tem causa
diferente. Sem dado que as distinga, não há diagnóstico. **Perguntar antes de
mexer no código.**

---

## P3 — Travamento ao entrar no modo história

**O que já se sabe:** o harness atravessa o jogo inteiro 12 vezes sem travar,
incluindo 5 ciclos de tutorial. Não é reproduzível localmente.

**O que falta:** um log do console travando. Com a marca por quadro dos
primeiros 300 quadros, o `BOOT.txt` vai dizer o quadro exato. Daí é isolar o
estado (`ui_state`) e a transição na linha `S,` anterior.

---

## P4 — Tutorial

**Sintomas reportados:** câmera travada no BF, nenhuma nota, nenhuma barra de
acerto, personagens não animando, música toca.

**O que já se sabe:** há código escrito para isso no repositório, não confirmado
em hardware. O estado 8 (tutorial) aparece 14.000 vezes no log do harness —
ou seja, é exercitado, mas os sintomas são visuais e o log não media animação
de personagem.

**O que falta:** confirmar em hardware, e se persistir, usar o log para medir.
O log tem `note_hits`, `note_misses`, `note_combo`, `note_score`,
`note_feedback` na linha `S,` — se as notas não aparecem, esses campos ficam em
zero e dizem se o chart carregou.

---

## P5 — Otimização (objetivo declarado do usuário)

O usuário pediu explicitamente **otimizar o máximo possível no console
original**. Frentes já identificadas:

- **O menu dobra as chamadas de desenho** (P1). Corrigir isso é otimização de
  graça.
- **O log escreve a cada quadro.** `telemetry_line()` já acumula, e o `fsync` é
  a cada 30 quadros. Se o custo ainda pesar, subir o intervalo.
- **VRAM:** `tools/vram_budget.py` existe para medir. Rodar e ver a margem.

---

## O que NÃO fazer

- **Não entregar build sem compilar limpo, rodar a suite e provar a correção.**
- **Não afirmar causa sem dado.** Três builds foram perdidas assim.
- **Não empilhar hipóteses.** Se uma build não funciona, a próxima **reverte** o
  suspeito antes de tentar outro.
- **Não confiar no harness para I/O, tempo ou sincronização.** Ele finge
  `write()` e `fsync()` como instantâneos.
- **Não remover o `LEIA-ME.txt` do pendrive** nem o marcador `BOOT.txt`.
