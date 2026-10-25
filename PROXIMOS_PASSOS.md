# PRÓXIMOS PASSOS — detalhado

Ordenado por prioridade. Cada item diz **o que já se sabe** (com fonte) e **o que
falta descobrir**. Nada aqui é palpite.

---

## P0 — Rodar a 0.2.112 no console e trazer o log

**Estado em 2026-10-25: o pendrive está CONSERTADO e conferido byte a byte.**
O que impedia o jogo de rodar era o **nome do executável**: o canal #50 tinha
copiado o ELF para `F:\FNF_PS2_0.2.112.ELF`, mas o nome tem de ser exatamente
`F:\FNF_PS2.ELF`. Corrigido pelo canal #55.

Auditoria remota completa (`F:`), tudo conferido:

| Item | Estado |
|---|---|
| `F:\FNFPS2\` | ✅ 340 arquivos |
| charts | ✅ 324 (= 81 × 4 layouts de nome) |
| `menu_cache.rle` | ✅ 1.587.561 B, sha256 `cd27d719…d351` — bloco 4 corrigido |
| `F:\FNF_PS2.ELF` | ✅ 5.264.808 B, sha256 `095a5e0b…74faa` |
| `LEIA-ME.txt` | ✅ na raiz |
| ZIP truncado de 2.475 B | ✅ removido |

**O que falta — uma coisa só:** rodar o jogo no PS2 com este pendrive, entrar no
menu, esperar alguns segundos e sair. Isso cria `mass:/FNFPS2/FNF_COLHEITA.txt`
e `mass:/FNFPS2/BOOT.txt`.

**A colheita já está pronta:** o canal #56 analisa o log **no PC** e devolve só
um resumo compacto (o cliente fatia a saída em pedaços de 2.000 caracteres e o
log tem ~20.000 linhas). Ele mede: sprites por quadro, qualquer sprite com
geometria **fora** da faixa 56..391, geometrias na borda de baixo
(gsy1 entre 384,5 e 391,5 — as 7 linhas abaixo do último botão), sprites
esticados (`vy_span != h`) e com escala `h/vh != 1`. Rodou limpo (rc=0); só
ainda não havia log para ler.

**Como interpretar o `BOOT.txt`:**

| `BOOT.txt` diz | Significa |
|---|---|
| `passo 30: F0_FRAMEBUFFER_SET` e depois `passo 31: FRAME,1,...` | boot completo, rodando |
| para num `passo N` de boot (META, PAD, CACHE, AUDIO, GS, TITLE) | travou no boot, no passo N |
| para num `passo N: FRAME,k,...` | travou no quadro k |
| arquivo não existe | o pendrive não montou — problema de install ou de `reset_iop()` |

### ⚠️ Atualização de 2026-10-25 — duas coisas mudaram

**1. A hipótese "assets ausentes" está morta.** O canal #58 auditou o pendrive
inteiro: os 16 assets existem, e os 12 que têm tamanho fixo no código têm o
tamanho **exato**. Nenhum falta. O jogo congela **dentro do quadro 0**, logo
depois de `F0_FRAMEBUFFER_SET`, que é o último marco que o `BOOT.txt` escreveu.

**2. A colheita vazia tinha causa própria, já corrigida (commit `00fe473`).** O
`usb_ready` só era ligado no `telemetry_init()` quando a *primeira* tentativa de
abrir o log dava certo; a abertura tardia abria o descritor mas nunca ligava a
bandeira, e o `O_TRUNC` zerava o arquivo para sempre. Ver
`fnfps2/docs/BUG_usb_ready_abertura_tardia.md`. **A colheita vazia não era
sintoma do travamento** — os dois escritores falhavam por motivos diferentes.

**Os marcos novos do quadro 0** dizem em qual chamada exata o jogo pendurou. A
ordem depois de `F0_FRAMEBUFFER_SET` é: `F0_DL_DUMP_BEGIN`, `F0_DL_DUMP_DONE`,
`F0_TEL_FRAME_BEGIN`, `F0_TEL_FRAME_DONE`, `F0_TEL_STATE_DONE`,
`F0_TELEMETRY_FLUSH_DONE`, `F0_FRAME0_FIM`.

| Onde o `BOOT.txt` parar | Significa |
|---|---|
| em `F0_FRAMEBUFFER_SET` (ou antes) | nem `F0_DL_DUMP_BEGIN` saiu: a escrita no pendrive parou — o dispositivo caiu |
| em `F0_DL_DUMP_BEGIN` | pendurou **dentro** de `dl_dump()` |
| em `F0_DL_DUMP_DONE` | pendurou em `telemetry_frame()` ou `telemetry_state()` |
| em `F0_TEL_FRAME_DONE` | pendurou em `telemetry_state()` |
| em `F0_TEL_STATE_DONE` | pendurou em `telemetry_flush()` |
| em `F0_TELEMETRY_FLUSH_DONE` | pendurou em `av_trace_capture()` |
| em `F0_FRAME0_FIM` | o quadro 0 terminou; o problema está no quadro 1 |

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

- **O log escreve a cada quadro.** `telemetry_line()` já acumula, e o `fsync` é
  a cada 30 quadros. Se o custo ainda pesar, subir o intervalo.
  (A ideia antiga de "o menu dobra as chamadas de desenho" como ganho grátis
  está **descartada** — ver P1: o menu desenha cada item uma vez só.)
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
