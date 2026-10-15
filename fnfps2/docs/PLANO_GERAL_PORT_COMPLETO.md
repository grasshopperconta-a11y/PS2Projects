# Plano geral — port completo de FNF v0.8.6 para PlayStation 2

Documento de trabalho. Tudo aqui é medido ou derivado, não estimado por
impressão. Onde eu não sei, está escrito que não sei.

---

## 0. A premissa, revista

Você citou o port de PS1 como prova de que dá. Concordo com a lição que
ele ensina, e ela é a base deste plano: **o que torna um port completo
viável não é reduzir qualidade, é reprojetar o motor para a máquina.**
O PS1 não roda FNF com texturas menores; ele roda uma reimplementação
feita para o hardware dele.

O nosso erro até aqui foi o oposto: um `main.c` de 1.209 linhas que
cresceu por acréscimo, com cinco slots de textura fixos e uma máquina de
estados escrita à mão. Isso levou o Tutorial até perto da fidelidade e
não leva o resto. A conta que prova:

```
bs.py plano-cena
  12 palcos cabem na arquitetura de hoje, 9 NAO cabem.
  tankmanBattlefield  3 chars + 10 props animados = 13 slots (faltam 8)
  limoRideErect 11 | limoRide 10 | phillyStreetsErect 7
```

Baixar resolução não cria slot. Então a Fase 0 deste plano não é
conteúdo: é motor.

---

## 1. O tamanho exato do problema

| item | quantidade |
|---|---:|
| código Haxe | 122.038 linhas em 517 arquivos |
| idem, sem editores e depuração | **92.700 linhas** |
| scripts `.hxc` interpretados | 79 |
| nosso port hoje | **1.209 linhas de C** |
| personagens | 47 |
| palcos | 21 |
| semanas | 10 |
| músicas | 28 |
| imagens `.png` | 685 |
| spritesheets Sparrow `.xml` | 266 |
| pastas Animate Atlas | 88 |
| áudios `.ogg` | 431 |
| vídeos `.mp4` | 8 |
| fontes `.ttf`/`.otf` | 25 |
| **shaders `.frag`** | **12** |

Três desses merecem atenção especial, porque não têm equivalente direto
no PS2:

- **Os 12 shaders.** O GS não tem shader programável. Efeitos como a
  gradação de cor das variantes *Erect* e os filtros de pixel precisam
  ser reimplementados um a um com recursos fixos do GS (blending, CLUT,
  passes extras) ou não existirão. **Vou tratar cada um individualmente
  e registrar o que for impossível.**
- **Os 8 vídeos.** O PS2 tem a IPU, que decodifica MPEG-2. Dá, mas é um
  subsistema novo: converter com `ffmpeg` para MPEG-2 em resolução baixa
  e escrever um decodificador em streaming. É uma fase própria.
- **As 25 fontes.** Viram atlas de bitmap pré-renderizados em alguns
  corpos fixos. Texto dinâmico com qualquer corpo não vai existir.

---

## 2. Arquitetura alvo

Substituir o `main.c` atual por um motor pequeno, dirigido por dados.
Cinco camadas:

### 2.1 Plataforma (`plat/`)
- **Fila de E/S serializada.** O `usbhdfsd` não é reentrante; já nos
  custou dois travamentos duros. Toda leitura e escrita passa por uma
  fila com uma única thread dona do dispositivo.
- **Áudio em streaming** com o anel atual, já corrigido com parada
  cooperativa.
- **Entrada** de controle e, opcionalmente, teclado USB (`ps2kbd`) para
  o console de depuração.

### 2.2 Gráficos (`gfx/`)
- **Alocador de VRAM com cache e despejo (LRU).** Fim dos cinco slots
  fixos. O cache conhece o custo de cada textura e despeja a menos usada
  quando falta espaço. É isto que destrava os 9 palcos impossíveis.
- **Atlas em tempo de execução**: vários props animados pequenos
  empacotados numa textura só, para gastar um slot em vez de dez.
- **Regras de amostragem corretas** desde o início: `REGION_CLAMP` com
  `MINU/MAXU/MINV/MAXV`, `TEXA` para PSMCT16, blit 1:1 em coordenada
  inteira. Tudo que aprendemos a duras penas vira padrão.

### 2.3 Dados (`data/`, gerado)
Tabelas C emitidas pelo Butterscotch a partir dos JSON oficiais:
personagens, palcos, níveis, estilos de nota, charts, eventos. **Nada
digitado à mão.**

### 2.4 Jogo (`game/`)
As regras de verdade, escritas em C com a linha da fonte citada ao lado
de cada constante. Conductor, strumline, julgamento, vida, câmera,
personagens, eventos de chart, telas.

### 2.5 Conteúdo
Semana a semana, alimentado só por dados.

---

## 3. O laço de trabalho precisa mudar

Hoje cada alteração custa uma ida e volta ao seu console. O traço do
MERCH consumiu **cinco ciclos** e continua aberto. Com mais de cem itens
pela frente, esse é o gargalo maior que o código.

**Fase 0 inclui um renderizador offline** que desenha qualquer tela do
port aqui no PC, com os mesmos números e as mesmas regras do GS. Já
provei o conceito: foi o `simular-menu` que localizou o bug do
grampeamento por eliminação. Com ele, o console passa a validar
**marcos**, não cada mudança.

---

## 4. Fases, com critério de aceitação

| fase | entrega | pronto quando |
|---|---|---|
| **0** | Motor: fila de E/S, cache de VRAM, atlas em runtime, renderizador offline | O Tutorial atual roda igual, mas sobre o motor novo, e o simulador reproduz a tela |
| **1** | Butterscotch completo: imagens, áudio, fontes, charts, tabelas | Um comando converte o jogo inteiro e recusa o que não couber |
| **2** | Núcleo de gameplay fiel | Week 1 inteira jogável com julgamento, vida, combo, eventos |
| **3** | Todas as telas | Title, Main, Story, Freeplay, Options, Pause, Game Over, Results |
| **4** | Conteúdo semana a semana | Cada semana entra por dados, sem código novo |
| **5** | Cauda longa | Easter eggs, cutscenes com IPU, shaders possíveis |

Cada fase termina com um teste no seu console. Dentro da fase, a
validação é offline.

---

## 5. O QUE VOCÊ PRECISA BAIXAR

Tudo abaixo vai para **uma pasta só**, que chamaremos de `C:\FNFPORT`.
Crie ela primeiro.

### 5.1 Código-fonte oficial, versão exata (≈4 MB)

```
https://github.com/FunkinCrew/Funkin/archive/refs/tags/v0.8.6.zip
```
Extraia em `C:\FNFPORT\`. Deve ficar:
```
C:\FNFPORT\Funkin-0.8.6\source\funkin\...
```

### 5.2 Assets oficiais, commit exato (≈1,26 GB)

```
https://github.com/FunkinCrew/funkin.assets/archive/9300719cb261d23f72344807055be6d109c9949c.zip
```
Extraia em `C:\FNFPORT\`. Deve ficar:
```
C:\FNFPORT\funkin.assets-9300719cb261d23f72344807055be6d109c9949c\preload\...
C:\FNFPORT\funkin.assets-9300719cb261d23f72344807055be6d109c9949c\shared\...
```
**Renomeie essa pasta para `assets`**, fica mais curto:
```
C:\FNFPORT\assets\preload\...
C:\FNFPORT\assets\shared\...
```

> Esse commit é o mesmo que venho usando em todas as derivações do
> projeto. Não troque por `main`: já me enganei uma vez lendo `main` com
> assets da v0.8.6.

### 5.3 Python 3.11 ou mais novo

```
https://www.python.org/downloads/windows/
```
Na instalação, marque **"Add python.exe to PATH"**.

Depois abra o Prompt de Comando e rode:
```
pip install pillow numpy lz4
```

### 5.4 FFmpeg (para áudio e vídeo)

```
https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
```
Extraia e copie `ffmpeg.exe` para `C:\FNFPORT\ferramentas\ffmpeg.exe`.

### 5.5 Estrutura final esperada

```
C:\FNFPORT\
   Funkin-0.8.6\           <- codigo fonte oficial
   assets\                 <- assets oficiais, renomeado
   ferramentas\
      ffmpeg.exe
   butterscotch\           <- eu te mando, no proximo ciclo
   saida\                  <- criada pelo programa, vai para o pendrive
```

**Não precisa baixar o ps2sdk nem compilador.** A compilação do código
acontece aqui comigo; você só roda a conversão de assets, que é o que
não cabe do meu lado (1,26 GB contra o meu limite de workspace).

---

## 6. Como o trabalho vai fluir

1. Você baixa e extrai o acima, uma vez só.
2. Eu te mando o **Butterscotch** como uma pasta `butterscotch\` com um
   `CONVERTER.cmd` de dois cliques.
3. Você roda. Ele lê `Funkin-0.8.6\` e `assets\`, calcula o orçamento de
   cada cena, converte tudo que couber, **recusa e relata o que não
   couber**, e escreve em `saida\`.
4. Você me manda o **relatório** que ele gera (um `.txt` pequeno, não os
   assets).
5. Eu escrevo o código C contra esse relatório e te mando o ELF.
6. O instalador grava `saida\` mais o ELF no pendrive.

---

## 7. O que eu não vou prometer

- **Precisão infalível em 100% do jogo.** Os easter eggs e os detalhes
  pequenos vivem nas 92.700 linhas de código, não nos JSON. Cada um é
  trabalho manual. Vou implementar todos que conseguir e **manter uma
  lista pública do que ficou de fora**, com o motivo.
- **Os 12 shaders.** Alguns não têm tradução para o GS. Vou atacar um a
  um e registrar os impossíveis.
- **Prazo.** Não sei quantos ciclos. Sei que a Fase 0 derruba o custo de
  todos os seguintes, e por isso ela vem primeiro.

---

## 8. Decisão que preciso de você

A Fase 0 **reescreve o `main.c`**. O Tutorial atual, que você aprovou
depois de muitos ciclos, vai ser reconstruído sobre o motor novo. Ele
deve sair igual, e o simulador existe para garantir isso, mas é uma
reescrita.

A alternativa é continuar acrescentando no `main.c` atual, que é mais
seguro a curto prazo e não chega nos 9 palcos impossíveis.

Eu recomendo a reescrita. Mas a decisão muda o plano inteiro, então
prefiro que seja sua.
