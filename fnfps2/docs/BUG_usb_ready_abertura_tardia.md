# Bug encontrado: `usb_ready` nunca é ligado na abertura tardia do log

## O sintoma

`FNF_COLHEITA.txt` com **0 bytes** no pendrive, enquanto `BOOT.txt` tem conteúdo
normal (36 bytes, `passo 31: F0_FRAMEBUFFER_SET`).

## A causa, medida no código

Em `src/telemetry.c`, a variável `usb_ready` é colocada em `1` em **um único
lugar do arquivo inteiro**:

```
telemetry.c:245:    usb_ready = 1;
```

E esse lugar é dentro de `telemetry_init()`, **depois** do `log_try_open()` e
depois do teste `if (log_fd < 0) return init_result;`.

O `log_try_open()` é chamado de novo em dois outros pontos — a "segunda chance",
uma vez por quadro:

```
telemetry.c:348:        log_try_open(&dummy);   /* dentro de telemetry_frame() */
telemetry.c:416:        log_try_open(&dummy);   /* dentro de telemetry_state() */
```

Nesses dois pontos, se o log finalmente abrir, `log_fd` passa a ser `>= 0`, mas
`usb_ready` **continua 0** — ninguém o liga.

E todas as funções de escrita começam assim:

```
telemetry.c:350:    if (!usb_ready || log_fd < 0 || output_error) return;
telemetry.c:378:    if (!usb_ready || log_fd < 0 || output_error) return;
telemetry.c:391:    if (!usb_ready || log_fd < 0 || output_error) return;
telemetry.c:418:    if (!usb_ready || log_fd < 0 || output_error) return;
telemetry.c:428:    if (!usb_ready) return;   /* telemetry_flush() */
telemetry.c:438:    if (!usb_ready) return;
telemetry.c:486:    if (!usb_ready) return -1;
```

## Consequência

Se o `log_try_open()` falhar **durante o init** — que é exatamente o cenário que
o comentário do próprio código descreve: o pendrive demora mais de 6,5 s para
montar e o init desiste cedo — então:

1. `usb_ready` fica em `0` para o resto da sessão;
2. a abertura tardia até consegue abrir `log_fd` (com `O_TRUNC`, isto é,
   **apagando** o conteúdo anterior);
3. mas **nenhuma escrita sai nunca mais**, porque todas as saídas testam
   `usb_ready` primeiro;
4. o resultado é um arquivo que existe, foi truncado para 0 bytes, e nunca mais
   recebeu um byte — exatamente o `FNF_COLHEITA.txt` de 0 bytes observado.

`BOOT.txt` continua funcionando porque `boot_mark()` em `main.c` abre o **seu
próprio** descritor (`open("mass:/FNFPS2/BOOT.txt", O_WRONLY|O_CREAT|O_TRUNC)`)
e não depende dessa máquina. É por isso que um arquivo tem dado e o outro não:
**a escrita de boot e a escrita da telemetria falham por motivos diferentes.**

## Por que isso importa para o diagnóstico da tela preta

A hipótese anterior era "`telemetry_flush()` bloqueia no pendrive". Essa
hipótese exige `usb_ready == 1`. Mas se `usb_ready == 0`, o `telemetry_flush()`
**retorna na primeira linha** e não pode travar. Os dois estados são
mutuamente exclusivos, e o arquivo de 0 bytes aponta para `usb_ready == 0`.

Ou seja: a colheita vazia **não é sintoma do travamento** — é um defeito
independente, e possivelmente o motivo de a gente estar sem telemetria há três
rodadas.

## Correção

Ligar `usb_ready` no lugar certo: dentro de `log_try_open()`, no instante em que
o descritor abre com sucesso. Assim a segunda chance passa a valer de verdade, e
qualquer abertura bem-sucedida — na primeira tentativa ou na quadragésima —
habilita as escritas.

O cabeçalho (`build=`, `elf=`) hoje sai no init porque `usb_ready` é ligado lá.
Se a abertura for tardia, o cabeçalho tem de sair **na abertura**, não no init,
senão o arquivo começa sem dizer que build é essa.
