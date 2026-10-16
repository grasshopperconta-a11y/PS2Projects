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

`tools/run_harness.sh` compila **o jogo de verdade** (`main.c` e todos os
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
| **Pad roteirizado** | `PS2H_INPUT` aperta botões em quadros escolhidos, para o jogo atravessar título → menu → story → tutorial |
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
sh tools/run_harness.sh 1400             # padrao: atravessa o jogo inteiro
sh tools/run_harness.sh 60 build/harness_assets
PS2H_INPUT="200:CROSS,600:CROSS" ./build/fnf_harness
```

Variáveis: `PS2H_FRAMES`, `PS2H_ROOT`, `PS2H_INPUT`, `PS2H_STRICT`,
`PS2H_WATCHDOG`, `PS2H_QWORDS_CAP`, `PS2H_FORCE_QWC`, `PS2SDK_HEADERS`.

## Cobertura: o jogo inteiro, não só a tela de título

A primeira versão do harness rodava 240 quadros **parados na tela de título**.
Passava, mas não exercitava nada arriscado — o menu, o story e o tutorial
nunca rodavam. Esse é o pior tipo de verde: um teste que passa sem testar.

O roteiro padrão resolve isso. Os quadros não são chute: vieram do próprio log
do jogo, que registra o quadro exato de cada troca de estado.

```
200  CROSS   titulo -> menu principal          (state=6  no quadro 365)
420  CROSS   menu (STORY MODE) -> story menu   (state=7  no quadro 516)
600  CROSS   story menu -> tutorial            (state=8  no quadro 615)
```

E a suíte **exige** que esses três estados apareçam no log, mais o chart do
tutorial carregado. Se o jogo parar antes, o teste falha — não passa em
silêncio.

## Os dois testes negativos

Um detector que nunca dispara não vale nada, e ninguém notaria a diferença.
Por isso a suíte **força** o estouro e exige que o harness morra com a
mensagem certa:

```sh
PS2H_QWORDS_CAP=8     ./build/fnf_harness   # pacote de 8 qw  -> zona de guarda
PS2H_FORCE_QWC=70000  ./build/fnf_harness   # DMA de 70000 qw -> acima de QWC_MAX
```

Ambos têm de falhar. Se algum deles passar, o detector quebrou.

## Assets sintéticos

O jogo lê tudo de `mass:/FNFPS2/assets/`. Na vida real isso está no memory card
do PS2; no host, `tools/gen_harness_assets.py` gera conteúdo **válido** para
cada formato, com as dimensões exatas, para que o código real de leitura,
decodificação e textura rode.

`tools/check_harness_assets.py` valida cada arquivo **replicando os
decododificadores do jogo em Python**. Quatro formatos exigem resolver duas
contas ao mesmo tempo, porque o decodificador devolve erro se qualquer uma não
fechar:

| Asset | Formato | Conta |
|---|---|---|
| `menu_cache.rle` | 4 blocos RLE concatenados | cada um consome exatamente seu tamanho e produz exatamente o decodificado |
| blob em `menu_sfx.pcm` | RLE de alfa, 1 byte por pixel | 7.672 bytes → 19.200 pixels |
| `bf_frames.lz4f` | CFZ4 + LZ4 | 43 quadros de 262.128 B, pacote < 8 MB |
| `gf_frames.lz4f` | CFZ4 + LZ4 | 87 quadros de 196.480 B, pacote < 8 MB |

Os charts do tutorial são os **de verdade**, convertidos pelo conversor do
próprio repositório — não faz sentido sintetizar chart quando o real existe.

Três erros meus apareceram só ao validar, e todos eram do tipo que passaria
batido no console:

1. A extensão de tamanho do LZ4 começava com um `0` marcador. O decodificador
   lê bytes de extensão **enquanto** valem 255 e para no primeiro diferente —
   então o `0` cortava a extensão pela metade.
2. Os literais e o match estavam em tokens separados. No LZ4 os dois dividem o
   **mesmo** token: nibble alto para os literais, baixo para `match - 4`.
3. A ordem estava errada: no LZ4 o **offset (2 bytes) vem antes** da extensão
   do match.

## Resultado atual

```
quadros executados ............ 1401
maior pacote construido ....... 616 quadwords (limite pedido 4096)
ESTOUROS DE PACOTE ............ 0
escritas na zona de guarda .... 0
envios DMA acima de QWC_MAX ... 0
uploads de textura ........... 1376 chamadas, 253 MB
setup_environment ............ 1759
chamadas de desenho .......... 108268  (preenchidos 2136, texturizados 106132)
E/S: opens/falhas/leituras ... 69 / 0 / 7073 (leituras curtas 0)
RESULTADO: PASSOU
```

O maior pacote real ficou em **616 dos 4096** disponíveis. A tela de título
usa 299; o tutorial, com 106 mil chamadas de desenho em 1401 quadros, é o que
realmente estica o pacote — e é justamente o estado que a primeira versão do
harness nunca alcançava.
