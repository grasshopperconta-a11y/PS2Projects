# ANALISE DO TESTE NO PS2 -- 2026-10-16

Relato do usuario, logs (`FNF_COLHEITA.txt`, 20.204 linhas) e 4 capturas de
framebuffer (640x448 RGBA32) recebidos juntos.

Build testada: `0.2.105-aceite-exato`, revisao `c873a40`.
Pacote: `FNF_PS2_PENDRIVE.zip` (ELF + 16 assets + 81 charts).


## 0. O que o log diz de imediato

Todas as 10 tentativas de captura falharam:

```
phase=RAW_MENU_PAUSE  row=2898  code=2404352
phase=RAW_FAILED      row=-1    code=-2
```

`capture_framebuffer_raw()` devolve -2 quando `g_capture_raw_fd < 0`. O fd eh
aberto UMA vez no boot:

```c
g_capture_raw_fd=open("mass:/FNFPS2/FNF_SCREEN_0000.rgba.txt",
                      O_WRONLY|O_CREAT|O_TRUNC,0666);
```

e so eh reaberto no bloco `if(r==0)`. Ou seja: **se a abertura do boot falhar,
ou se uma captura falhar, TODAS as seguintes falham para sempre.** As 4 capturas
que recebi (0001..0004, 1.146.880 bytes = 640*448*4) sao de uma execucao
anterior -- nesta, nenhuma foi escrita. `FNF_SCREEN_0000.rgba.txt` tem 0 bytes.


## 1. Tutorial sem notas, sem barra, personagens parados -- CAUSA RAIZ ACHADA

O despejo de estado do quadro 9242 (ui_state 8) diz tudo:

```
[TUTORIAL] cena pronta 1 status 0 | audio 0
  packs: bf 1239417 bytes quadro 4 | gf 1375989 bytes quadro 0
  chart: status -1 notas 0 eventos 0 cursor 0 vistos 0
```

e a fase de preparo:

```
phase=TUT_CHART_BEGIN  code=0
phase=TUT_CHART_DONE   code=-1      <-- FALHOU
```

`chart_load()` devolve **-1 somente quando `open()` falha** (src/chart.c:73).
Os pacotes CFZ4 carregaram com os tamanhos certos (1.239.417 e 1.375.989), a
cena carregou, o HUD carregou, o audio tocou. So o chart nao abriu.

Consequencia em cadeia, todas confirmadas pelo relato:

- `g_chart_info.note_count = 0` -> nao ha nota para desenhar -> **notas e
  barrinha de acerto nao aparecem**.
- `chart_events_bind()` com 0 eventos -> nada dirige a animacao de canto dos
  personagens -> **BF e GF parados** (o despejo mostra `canto: bf -1 gf 0`).
- sem eventos de camera, ela fica onde nasceu -> **camera parada no BF**.

O caminho montado eh `mass:/FNFPS2/assets/songs/tutorial/normal.chart`
(`sr_chart_path`, src/engine/song_registry.c:103), e o ZIP tem exatamente esse
arquivo. Portanto a falha esta na leitura desse caminho no USB do PS2, nao no
empacotamento: os 15 outros arquivos de `mass:/FNFPS2/assets/*` abriram
normalmente no mesmo instante (`TUT_SCENE_DONE code=0`,
`TUT_NOTE_ATLAS_DONE code=0`).

Hipoteses, em ordem de probabilidade:

1. **A arvore `songs/` com 27 subdiretorios nao sobreviveu a extracao.** O
   usuario apagou a pasta antiga e extraiu o zip; se o extrator nao criou os
   diretorios aninhados, so os arquivos soltos em `assets/` funcionariam --
   que eh exatamente o sintoma (tudo funciona, so o chart falha).
2. **Limite do driver USB do PS2** (`usbhdfsd`) com 108 entradas dentro de
   `songs/`. Nao da para descartar sem testar.
3. O chart eh aberto no meio da transicao, com o barramento USB contestado.

A correcao tem de ser robusta as tres: **tentar varios layouts e registrar qual
abriu**, e **embutir uma copia plana** (`songs/<id>-<difficulty>.chart` e
`charts/<id>-<difficulty>.chart`) para cobrir o caso de o driver nao aceitar a
arvore aninhada.


## 2. Fonte diferente no menu story -- CAUSA RAIZ ACHADA

Eu regravei o bloco 4 de `menu_cache.rle` (os titulos do story) renderizando os
9 nomes com a **`font.rgba`**, que eh a fonte principal do jogo (atlase 384x192,
grade 16x6 de celulas 24x32, advance em `font.widths`).

O original nao usa essa fonte. O menu story usa a **fonte VCR**, que eh uma
mascara de alfa de 160x120 decodificada de um blob RLE que mora DENTRO de
`menu_sfx.pcm`:

```c
sf=story_font_alpha_decode(g_menu_sfx_pixels+241920u+22656u, 7672u,
                           g_font_pixels, 160u*120u);
```

(src/main.c, transicao para o story; 241920+22656 = 264.576.) Depois o alfa eh
comprimido para 0..128 e subido como textura 160x120, e o texto eh desenhado por
`story_vcr()`. Por isso a fonte sai diferente: **eu usei a fonte errada.**

A correcao eh re-renderizar os 9 titulos com essa mascara de 160x120 em vez de
`font.rgba`. O blob ja foi validado: 7.672 bytes -> 19.200 pixels, consumo e
producao exatos.


## 3. Fundo e itens do menu saindo das barras pretas -- CAUSA RAIZ ACHADA

Verdade do hardware, nao palpite. A lista de desenho do quadro 4324
(ui_state 6, selection 2, cam_y 360):

```
[PROPORCAO] modo 4:3 | fator vy 0.933333 | offset 56.0 | scissor 56..391
[DESENHO] ultima lista: 5 sprites
   0 tex   573440 tbw 320  242x57  v (199.0,181.0)-(441.0,238.0)
   1 tex   737280 tbw 256  193x58  v (224.0,255.0)-(417.0,313.0)
   2 tex   655360 tbw 320  244x52  v (198.0,332.0)-(442.0,384.0)
   3 tex   813056 tbw 512  220x58  v (210.0,404.0)-(430.0,462.0)   <-- 404 > 391
   4 tex   944128 tbw 384  384x81  v (128.0, 94.0)-(512.0,175.0)
```

O sprite 3 (`stagetex`, o item CREDITS) eh desenhado em y 404..462. O scissor
termina em 391. E a medicao das capturas confirma, linha por linha:

```
tela2: linhas nao-pretas 46..447 de 448     (scissor deveria ser 56..391)
tela3: linhas nao-pretas  0..402 de 448
tela1: linhas nao-pretas 56..391 de 448     (esta correta, + 1 pixel na linha 6)
```

Ou seja: **quando a camera do menu sai do repouso, os itens passam a ser
desenhados fora da area de jogo e o scissor nao os corta.** Em tela1 (cam_y no
repouso, selection 0) o scissor funciona. Em tela2/tela3 (camera movida) nao.

A aritmetica do item:

```c
float camoff=(menu_cam_y-360.0f)*0.4f;
float cy=(40.0f+160.0f*mi-camoff)*.5f;
```

Para cam_y=360 (camoff=0) e mi=4: cy=340 -> vy(340)=373, dentro. Mas o sprite
sai em 404, que corresponde a cy~372. Ha um desvio entre o cy calculado e o y
real do sprite -- provavelmente porque `cy` so cobre o TOPO do item e a altura
do sprite (58) mais o espaçamento empurram o item para baixo, e nada limita
`cy` ao intervalo [0,360].

O fundo nao eh o culpado: ele usa parallax proprio
(`bg_y=-37.978227f-(menu_cam_y-360.0f)*0.085f`, altura 435,96) e ha um
comentario no codigo afirmando que a cobertura sobra para todo cam_y em
[40,680]. A tabela esa prova estao em `tools/prova_fix_02105.py` (nao esta no
repo -- precisa ser recriada).

**O que estah faltando eh a garantia de que o ITEM caiba na viewport.** O
original em Flixel faz o menu rolar e somecer nas bordas; o porto desenha o
item inteiro e deixa o GS decidir. A correcao eh calcular a faixa visivel de
`cy` a partir da altura real de cada sprite e saltar (ou recortar) o item que
nao caiba, como o codigo JA FAZ no story menu:

```c
if(vy(yy+hh)<269.0f||vy(yy)>391.0f)continue;   /* src/main.c, ui_state==7 */
```

Esse mesmo padrao -- e nao o scissor -- eh o que o story menu usa para nao
desenhar titulo fora da area. O menu principal nao tem essa verificacao.


## 4. Menu story quase todo preto na captura 4

```
tela4: linhas nao-pretas 6..55 de 448
```

So uma faixa de 10 linhas no topo. O usuario relatou que os botoes do story
"estao aparecendo e animados normalmente", entao esta captura provavelmente
pegou a transicao (o `story_assets` so fica 1 quando `back_titles_done` da 0).
De qualquer forma, o despejo do quadro 24190 (ui_state 7) mostra
`fonttex extensao 160x120`, que eh a fonte VCR carregada -- entao o fundo do
story e os titulos existem; a captura pegou um quadro de transicao.


## 5. Plano de correcao

Ordem por impacto.

### P0 -- destravar o tutorial (bug 1)

`src/main.c`, no bloco do chart do tutorial:

1. Trocar a resolucao de caminho unica por uma busca tentativa:
   `songs/<id>/<difficulty>.chart`, depois `songs/<id>-<difficulty>.chart`,
   depois `charts/<id>-<difficulty>.chart`.
2. Registrar no log QUAL caminho abriu e o codigo de cada tentativa, para que
   um -1 no console diga o caminho em vez de so o numero.
3. Embarcar no pacote do pendrive as tres copias (a arvore aninhada + a plana),
   para que a correcao funcione mesmo que o driver USB nao aceite subdiretorio.

### P0 -- a fonte do story (bug 2)

`tools/fix_menu_cache_block4.py`:

1. Parar de usar `font.rgba`. Usar a mascara de alfa de 160x120 decodificada do
   blob RLE em `menu_sfx.pcm` offset 264.576.
2. Descobrir a geometria dos glifos nessa mascara (provavelmente largura fixa
   por caractere) medindo o blob -- e so entao renderizar.
3. Rever o bloco 4 para exatamente 188.635 bytes -> 306.180 bytes, como hoje.

### P1 -- itens do menu fora da area de jogo (bug 3)

`src/main.c`, no laco de itens do `ui_state==6`:

1. Computar a altura real do sprite (`fr[1]`, `fr[2]`) e a faixa visivel de `cy`
   com a mesma regra que o story menu ja usa: pular o item que nao caiba.
2. Manter o parallax do fundo como estah (ele nao eh o problema).
3. Rever a prova de cobertura para TODO cam_y em [40,680] com a altura real de
   cada um dos 5 itens, e nao so com a altura do fundo.

### P1 -- captura de tela confiavel (bug 0)

`src/main.c`:

1. Tentar reabrir `g_capture_raw_fd` quando a captura falhar, em vez de deixar
   -1 para sempre. Uma falha hoje mata todas as capturas seguintes.
2. Registrar o codigo de abertura do boot no log, para separar "nao abriu no
   boot" de "falhou no readback".

### P2 -- verificacao antes de entregar

1. `python3 tools/check_real_assets.py <raiz>` nos assets novos.
2. `PS2H_ROOT=<pacote> ./build/fnf_harness` com os assets REAIS, exigtindo
   `chart: status 0 notas >0 eventos >0` no despejo -- hoje o harness passa
   com o chart sintetico, que sempre existe no host.
3. Nova captura no console para confirmar as linhas 56..391 em todos os estados.
