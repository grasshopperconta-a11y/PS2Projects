# Fase 0 — estado do motor

Tudo aqui é verificado por teste que roda no PC. Nada depende do console
ainda; o console entra só no fim da fase, quando o Tutorial for
reconstruído sobre o motor.

```
gcc -O2 -Wall -Wextra -std=gnu11 -o tvc tools/teste_vram_cache.c src/engine/vram_cache.c && ./tvc
gcc -O2 -Wall -Wextra -std=gnu11 -o tio tools/teste_io_fila.c    src/engine/io_fila.c    && ./tio
```

---

## 1. Cache de VRAM — PRONTO e verificado

`src/engine/vram_cache.{c,h}`

Substitui os cinco slots fixos (`tex`, `tex2`, `gftex`, `stagetex`,
`fonttex`) que limitavam o port a 12 dos 21 palcos. Quem desenha pede
por chave; se já está residente o custo é zero; se falta espaço, despeja
o menos usado recentemente e funde buracos vizinhos.

Resultado do teste, com as demandas reais das cenas:

| cena | texturas vivas | bytes | despejos | falhas |
|---|---:|---:|---:|---:|
| mainStage | 3 | 752.640 | 0 | 0 |
| tankmanBattlefield | 13 | 625.664 | 0 | 0 |
| limoRide | 6 | 288.768 | 0 | 0 |
| school | 6 | 230.400 | 0 | 0 |

- 200 trocas de cena: sobra **523.264 B num único buraco**, 0 falhas.
  A fusão funciona e não há fragmentação.
- 3.600 quadros na cena mais pesada: **0 despejos** depois de aquecido,
  ou seja nada é reenviado à toa.

**Dois erros que este teste pegou no planejador de escalas:**
1. O veredito imprimia a escala de 16 bits rotulada como "32 bits".
2. O planejador não reservava VRAM para HUD, fonte e cenário —
   `327.680 + 294.912 + 524.288 = 1.146.880 B` que toda cena paga.
   Sobram **753.664 B por cena**, não 1.900.544. As escalas caíram de
   0,34–0,93 para **0,16–0,47**, e ainda assim as 21 cenas cabem.

---

## 2. Fila de E/S fatiada — PRONTA e verificada

`src/engine/io_fila.{c,h}`

O `usbhdfsd` não é reentrante. Este projeto perdeu dois ciclos para
isso: na 0.2.64 a captura corrompia o driver e matava música e
animações; na 0.2.74 serializei e a música só ficava muda. A fila
resolve as duas: uma dona só do dispositivo, e **nenhuma operação o
segura por mais de uma fatia de 32 KB**.

**Correção importante de um número meu.** Eu tinha modelado o teste a
37 MB/s e nada estourava — o que contradizia o console. 37 MB/s é a taxa
de *upload de textura do GS*, não do pendrive; o PS2 tem USB 1.1. A taxa
real sai de uma medição deste projeto: a carga do Tutorial lê
`524.288 + 1.239.417 + 1.375.989 = 3.139.694 B` em 4.972 ms de E/S pura,
ou seja **0,63 MB/s**.

Com o número certo o teste reproduz o bug real e mostra o que resolve:

| política | gravação total | pior espera do áudio | prazo 1.365 ms |
|---|---:|---:|---|
| A) sem fila, até 0.2.63 | 1.820 ms | 1.820 ms | **seca** |
| B) fatiada, sem prioridade | 2.237 ms | 1.872 ms | **seca** |
| C) fatiada, com prioridade | 2.237 ms | **52 ms** | ok, 26× de margem |

**Achado que eu não esperava: fatiar sozinho não resolve.** Por ordem de
chegada o áudio ainda espera a gravação quase inteira. É a prioridade
que salva. O preço é a captura ficar 23% mais lenta — aceito.

---

## 3. Simulador do GS — PRONTO, e já pagou o investimento

`tools/butterscotch/gs_sim.py` + `teste_gs_merch.py`

Reimplementa em Python as regras do GS que de fato nos mordem: os quatro
modos `WMS/WMT` (com `CLAMP` grampeando na textura inteira de lado
potência de dois e **ignorando** `MINU/MAXU`), a expansão `TEXA` do alfa
de 1 bit do PSMCT16, o alfa na escala 0..128, `NEAREST`/`LINEAR`,
scissor e as barras de 44 px. A VRAM é modelada **com lixo deliberado**,
porque inicializar com zero esconderia exatamente o tipo de defeito que
estamos caçando — foi assim que eu me enganei ao exportar PNG com alfa
forçado.

**Primeiro uso, e já respondeu uma pergunta que custaria um ciclo.**
Na 0.2.75 eu troquei `WRAP_CLAMP` por `WRAP_REGION_CLAMP` convencido de
ter achado o traço do MERCH. O console disse que não mudou nada. O
simulador explica por quê, e de forma incontestável: **as duas saídas
são byte a byte idênticas**, diferença máxima 0.

A razão é aritmética. O MERCH é 193×62, logo `TW=256 TH=64`, e no modo
`CLAMP` o GS pode amostrar `u 193..255` e `v 62..63`, que é lixo. Mas o
recorte de 1 px que entrou na 0.2.73 faz o port amostrar só `u 1..191` e
`v 1..60`. **Nunca alcança a área de lixo.** O modo de grampeamento é
irrelevante neste caso, e a correção da 0.2.75 era uma operação nula.

Fica registrado: essa foi a **quinta** hipótese errada minha sobre esse
traço, e a primeira derrubada sem gastar um teste seu.

**O que o simulador ainda não faz:** reproduzir o traço. Com o meu
modelo do desenho, o MERCH sai limpo. Ou seja, o defeito não é a arte,
não é o fundo, não é o meio pixel, não é o grampeamento. Falta algo no
meu modelo do que o port realmente manda para o GS.

## 4. O que falta na Fase 0

- **Despejo de lista de desenho.** Em vez de eu reconstruir o que o port
  desenha, fazer o port **despejar as chamadas reais de um quadro** para
  o pendrive, e o simulador reexecutar exatamente aquilo. Aí a
  reconstrução deixa de ser suposição minha. É o próximo passo e é
  barato: um gancho de telemetria que grava os parâmetros de cada
  sprite de um quadro.
- **Atlas em tempo de execução**, para juntar props pequenos.
- **Reconstruir o Tutorial** sobre o motor. Esse é o primeiro teste de
  hardware da fase.
