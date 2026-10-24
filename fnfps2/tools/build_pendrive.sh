#!/bin/sh
# Monta a pasta completa para copiar no pendrive.
#
# Layout que o jogo espera (src/main.c):
#   mass:/FNFPS2/assets/...                -> FNFPS2/assets/... na raiz do pendrive
#   mass:/FNFPS2/assets/songs/<id>/<d>.chart
#   mass:/FNFPS2/FNF_COLHEITA.txt          (criado pelo jogo, nao precisa existir)
#
# Uso: tools/build_pendrive.sh [dir-de-saida]
set -e
REPO=$(cd "$(dirname "$0")/.." && pwd)
cd "$REPO"

OUT=${1:-build/pendrive}
ASSETS=/home/user/PS2Projects/google_drive
ELF=build/FNF_PS2.ELF

rm -rf "$OUT"
mkdir -p "$OUT/FNFPS2/assets/songs"

echo "== copiando os 16 assets de runtime =="
# menu_cache.rle entra depois, pela secao de correcao -- nao aqui.
for f in title_alphabet.rgba title_prompt_l.rgba title_prompt_r.rgba \
         title_logoBumpin.frames title_gfDanceTitle.frames title_newgrounds.rgba \
         font.rgba font.widths menu_sfx.pcm \
         bf_frames.lz4f gf_frames.lz4f \
         mainstage_tutorial_parallax.rgba \
         tutorial_hud_official_320x256_gsalpha.rgba \
         audio_stems.pcm freakyMenu_48000.pcm; do
    if [ ! -f "$ASSETS/$f" ]; then
        echo "FALTA $f em $ASSETS" >&2
        exit 1
    fi
    cp "$ASSETS/$f" "$OUT/FNFPS2/assets/$f"
done

# menu_cache.rle -- a copia do Drive PODE estar velha, e isso jah aconteceu.
#
# Medicao que prova: o arquivo do Drive tem 1.623.445 bytes, mas o jogo le
# exatamente PRELOAD_RLE_BYTES = MENU_RLE+FONT+STORY+ST_TITLES =
# 1.288.182+38.342+72.402+188.635 = 1.587.561. A copia do Drive tem o bloco 4
# (story titulos) de outra versao: 224.519 B de origem para 379.264 B de
# destino, onde o jogo espera 188.635 para 306.180. Os tres primeiros blocos
# decodificam perfeito -- so o quarto estah velho, e eh justamente o que
# desenha os nomes das semanas do modo historia com a fonte errada.
#
# Portanto: nao confiar na copia do Drive. A correcao eh deterministica e jah
# validada (tools/fix_menu_cache_block4.py preserva os blocos 1 a 3 byte a
# byte e regera so o 4 com a fonte VCR real), entao ela eh APLICADA aqui, em
# todo build. Um AVISO nao basta: eu ignoraria o aviso e entregaria o pendrive
# com o bug da fonte.
WANT=1587561
MC="$ASSETS/menu_cache.rle"
[ -f "$MC" ] || { echo "FALTA $MC" >&2; exit 1; }
HAVE=$(wc -c < "$MC")
FIXED="$OUT/FNFPS2/assets/menu_cache.rle"
mkdir -p "$(dirname "$FIXED")"
if [ "$HAVE" = "$WANT" ]; then
    echo "   menu_cache.rle: $HAVE bytes, jah eh a versao corrigida"
    cp "$MC" "$FIXED"
else
    echo "   menu_cache.rle: $HAVE bytes != $WANT -- bloco 4 velho, regerando"
    python3 tools/fix_menu_cache_block4.py "$ASSETS" "$FIXED" >&2 || {
        echo "FALHOU a regeneracao do bloco 4" >&2; exit 1; }
    NEW=$(wc -c < "$FIXED")
    [ "$NEW" = "$WANT" ] || {
        echo "FALHOU: gerei $NEW bytes, esperado $WANT" >&2; exit 1; }
    echo "   menu_cache.rle regerado: $NEW bytes (blocos 1-3 preservados)"
fi
# e o bloco 4 tem de decodificar no tamanho que story_titles_restore() espera
python3 - "$FIXED" <<'PY' || exit 1
import sys, os
MENU_RLE, FONT_RLE, STORY_RLE, ST_RLE = 1288182, 38342, 72402, 188635
ST_RAW = 306180
p = sys.argv[1]
d = open(p, "rb").read()
off = MENU_RLE + FONT_RLE + STORY_RLE
if len(d) < off + ST_RLE:
    print("arquivo curto: %d < %d" % (len(d), off + ST_RLE)); sys.exit(1)
blk = d[off:off + ST_RLE]
si = di = 0
while si < len(blk) and di < ST_RAW:
    c = blk[si]; si += 1
    if c < 128:
        n = (c + 1) * 4; di += n; si += n
    elif c > 128:
        di += (257 - c) * 4; si += 4
    else:
        print("token 128 no bloco 4"); sys.exit(1)
if si != len(blk) or di != ST_RAW:
    print("bloco 4 nao fechou: si=%d/%d di=%d/%d" % (si, len(blk), di, ST_RAW))
    sys.exit(1)
print("   bloco 4 (story titulos): %d B -> %d B, fecha exato" % (ST_RLE, ST_RAW))
PY

echo "== copiando os charts =="
# O jogo tenta QUATRO caminhos, em ordem (sr_chart_layout_count()):
#   0: songs/<id>/<d>.chart      -- a arvore do jogo original
#   1: songs/<id>-<d>.chart      -- plano, um nivel so
#   2: charts/<id>-<d>.chart     -- plano, outra pasta
#   3: charts/<id>/<d>.chart     -- arvore, outra pasta
# Os planos existem porque num pendrive de verdade o usbhdfsd do PS2 nao
# conseguiu abrir songs/tutorial/normal.chart, mesmo com o arquivo la. O
# harness offline abre o layout 0 sem problema, entao so o console pode dizer
# qual vale -- por isso os quatro vao no pendrive e o jogo escolhe.
for f in build/charts/*.chart; do
    b=$(basename "$f")            # tutorial-easy.chart
    diff=${b##*-}                 # easy.chart
    diff=${diff%.chart}           # easy
    id=${b%-$diff.chart}          # tutorial
    mkdir -p "$OUT/FNFPS2/assets/songs/$id" "$OUT/FNFPS2/assets/charts/$id"
    cp "$f" "$OUT/FNFPS2/assets/songs/$id/$diff.chart"
    cp "$f" "$OUT/FNFPS2/assets/songs/$id-$diff.chart"
    cp "$f" "$OUT/FNFPS2/assets/charts/$id-$diff.chart"
    cp "$f" "$OUT/FNFPS2/assets/charts/$id/$diff.chart"
done
echo "   $(ls build/charts | wc -l) charts x 4 layouts = $(( $(ls build/charts | wc -l) * 4 )) arquivos"

echo "== copiando o ELF =="
if [ ! -f "$ELF" ]; then
    echo "FALTA $ELF -- baixe do Drive (id 17-GBt7YM8fkc4ZBP9Xo5g-ksAy_qN9Jl)" >&2
    exit 1
fi
cp "$ELF" "$OUT/FNF_PS2.ELF"

# Um LEIA-ME na raiz do pendrive. A build 0.2.108 foi dada como "nao abriu" e
# a installacao errada explica isso sozinha: o jogo le mass:/FNFPS2/assets/...,
# entao se a pasta FNFPS2 nao estiver na RAIZ do pendrive, o jogo nao acha asset
# nenhum, dorme para sempre e nao escreve log onde se espera. Este arquivo tira
# essa duvida.
cat > "$OUT/LEIA-ME.txt" <<'FIM'
FNF PS2 -- COMO INSTALAR
========================

1. Descompacte este ZIP DIRETO NA RAIZ DO PENDRIVE.
   Ao terminar, a raiz do pendrive tem de ficar assim:

       FNF_PS2.ELF
       FNFPS2/
       LEIA-ME.txt

   A pasta FNFPS2 tem de estar na RAIZ, nao dentro de outra pasta.
   Se ficar mass:/FNFPS2/FNFPS2/... o jogo NAO abre.

2. Rode FNF_PS2.ELF pelo seu lancador (uLE, OPL, ESR, etc).

3. Para eu poder diagnosticar qualquer coisa so pelo log, mande de volta:

       mass:/FNFPS2/FNF_COLHEITA.txt

   Se esse arquivo nao existir, procure na RAIZ do pendrive:
       mass:/FNF_COLHEITA.txt
   (o jogo tenta os dois lugares; se a pasta FNFPS2 nao estiver
   na raiz, ele escreve na raiz.)

   Desde a versao 0.2.112 o log eh SUBSTITUIDO a cada partida: uma execucao,
   um arquivo. Nao precisa mais apagar nada antes de testar -- e se o arquivo
   vier com conteudo de varias execucoes, a versao do ELF eh anterior a
   0.2.112 e o log nao pode ser lido de uma vez so.

O log tem uma linha por sprite por quadro, com a geometria ja recortada.
Com ele da para ver, sem voce descrever nada: sprite fora da faixa visivel,
fundo esticado, item do menu deslocado, e em qual quadro o jogo parou.
FIM

echo
echo "== conteudo =="
find "$OUT" -type f | wc -l
du -sh "$OUT"
echo
echo "pronto em $OUT"
echo "copie o CONTEUDO de $OUT para a raiz do pendrive"
