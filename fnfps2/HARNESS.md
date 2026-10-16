# Harness de link + execução — o que é e por que existe

## O problema que ele resolve

Os testes em `test/` exercitam os módulos do motor **isolados**: leem charts,
convertem FCH4, conferem o registro de músicas. Isso pega erro de lógica, mas
não pega o que só aparece quando **o jogo inteiro está ligado e rodando**:
estouro do pacote de desenho, envio DMA grande demais, acesso a endereço do GS
que não existe no PC, caminho `mass:/` que não abre.

No PS2 esses erros não travam. Eles **corrompem memória em silêncio**, e o
sintoma aparece quadros ou minutos depois, longe da causa — o cenário mais
caro de depurar que existe, e justamente o que você pediu para eliminar
*antes* de testar no console.

## O que o harness faz

`tools/run_harness.sh` compila **o jogo de verdade** (`src/main.c` e todos os
módulos) contra o **código real de `draw`/`packet`/`dma` do ps2sdk** — não uma
reimplementação — e executa no PC com:

| Peça | O que faz |
|---|---|
| **Pacote limitado** | `packet_init(n)` reserva exatamente `n` quadwords, como no PS2 |
| **Zona de guarda** | 64 quadwords logo depois, preenchidos com veneno. Qualquer escrita ali é estouro |
| **Morte imediata** | No primeiro estouro: `abort()` com o número do quadro, o tamanho real, o limite e o backtrace |
| **Limite de DMA** | `dma_channel_send_*` recusa acima de `QWC_MAX` (65535), que o DMAC rejeita |
| **Registradores do GS** | `0x12000000` mapeado de verdade com `MAP_FIXED`, `CSR` com o bit FINISH ligado — o `draw.c` do ps2sdk roda sem uma linha alterada |
| **`mass:/` → host** | `mass:/FNFPS2/assets/x` vira `<raiz>/FNFPS2/assets/x`, por interposição em nível de objeto |
| **Threads reais** | `CreateThread`/`StartThread` disparam pthreads de verdade, então a thread de pré-carga do título roda |
| **Pad** | `padGetState` estável, SELECT segurado (o combo de saída do jogo) e START por um quadro no fim |
| **Watchdog** | Se travar, imprime **onde** parou em vez de ficar pendurado sem dizer nada |
| **Shutdown distinto** | O jogo termina chamando `SleepThread()` e nunca volta do `main`. O harness reconhece isso como sucesso; em qualquer outro momento é falha |

A fidelidade dos quadwords é **exata**, porque quem conta é o `draw.c` do
ps2sdk, não uma estimativa:

```
draw_rect_filled          3
draw_rect_textured        4
draw_setup_environment   15
draw_finish               2
draw_texture_flush        3
draw_scissor_area         2
draw_texture_transfer     2 + dados
```

A única adaptação no código do ps2sdk é mecânica: `#ifdef _EE` → `#if 0` em
volta do bloco `__asm__("plzcw")` de `draw_log2`. O script prova com `diff -u`
que **essa é a única mudança** e que `draw2d.c`/`draw_environment.c` estão
intatos.

## Como usar

```sh
sh tools/run_harness.sh 240              # 240 quadros, assets sintéticos
sh tools/run_harness.sh 60 outrami       # outra raiz de assets
PS2H_FRAMES=600 ./build/fnf_harness      # direto, depois de construído
```

Variáveis: `PS2H_FRAMES`, `PS2H_ROOT`, `PS2H_STRICT`, `PS2H_WATCHDOG`,
`PS2H_QWORDS_CAP`, `PS2H_FORCE_QWC`, `PS2SDK_HEADERS`.

## Os dois testes negativos

Um detector que nunca dispara não vale nada, e ninguém notaria a diferença.
Por isso a suite (`test/run_tests.sh`) **força** o estouro e exige que o
harness morra com a mensagem certa:

```sh
PS2H_QWORDS_CAP=8   ./build/fnf_harness   # pacote de 8 qw  -> zona de guarda
PS2H_FORCE_QWC=70000 ./build/fnf_harness  # DMA de 70000 qw -> acima de QWC_MAX
```

Ambos têm de falhar. Se algum deles passar, o detector quebrou.

## Assets sintéticos

O jogo lê tudo de `mass:/FNFPS2/assets/`. Na vida real isso está no memory card
do PS2; no host, `tools/gen_harness_assets.py` gera conteúdo **válido** para
cada formato, com as dimensões exatas, para que o código real de leitura,
decodificação RLE e textura rode:

- `.rgba` / `.frames` — RGBA cruo, nas dimensões que o jogo espera;
- `.pcm` — PCM 16 bit mono, para o anel de audio ter dados de verdade;
- `font.widths` — tabela de larguras de glifo;
- `menu_cache.rle` — os 4 blocos RLE concatenados, cada um resolvido para
  consumir **exatamente** o tamanho do arquivo e produzir **exatamente** o
  tamanho decodificado. O decodificador do jogo devolve erro se as duas contas
  não fecharem, então o gerador resolve as duas ao mesmo tempo em vez de
  apenas "comprimir".

Os pixels são padrões determinísticos, então duas rodadas são comparáveis.

## Resultado atual

```
quadros executados ............ 241
maior pacote construido ....... 299 quadwords (limite pedido 4096)
ESTOUROS DE PACOTE ............ 0
escritas na zona de guarda .... 0
envios DMA acima de QWC_MAX ... 0
uploads de textura ........... 293 chamadas, 80 MB
setup_environment ............ 241
chamadas de desenho .......... 1102
E/S: opens/falhas/leituras ... 47 / 0 / 1247 (leituras curtas 0)
RESULTADO: PASSOU
```

O maior pacote real ficou em 299 dos 4096 disponíveis — folgo confortável, e
agora isso está **medido**, não presumido.
