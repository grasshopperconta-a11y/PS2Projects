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
for f in title_alphabet.rgba title_prompt_l.rgba title_prompt_r.rgba \
         title_logoBumpin.frames title_gfDanceTitle.frames title_newgrounds.rgba \
         font.rgba font.widths menu_sfx.pcm menu_cache.rle \
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

# menu_cache.rle corrigido.
# A copia do Drive JA eh a corrigida: tools/fix_menu_cache_block4.py reconstruiu
# so o bloco 4 (story titulos, que precisa da fonte VCR) e preservou os blocos
# 1 a 3 byte a byte. O /tmp/mc_fixed.rle que era copiado aqui era de uma
# rodada anterior da ferramenta e ficou velho -- copiar de /tmp entregava o
# bloco 4 antigo no pendrive mesmo com a raiz de assets certa. Agora a fonte
# unica eh a raiz de assets, e ela eh verificada antes de seguir.
if [ ! -f "$ASSETS/menu_cache.rle" ]; then
    echo "FALTA $ASSETS/menu_cache.rle" >&2
    exit 1
fi
WANT=$(python3 - <<'EOF'
import struct
# PRELOAD_RLE_BYTES: o main.c le exatamente esse tanto e ignora o resto, entao
# um arquivo maior nao falha aqui -- falha depois, dentro de story_titles_restore.
print(1587561)
EOF
)
HAVE=$(wc -c < "$ASSETS/menu_cache.rle")
if [ "$HAVE" != "$WANT" ]; then
    echo "   AVISO: menu_cache.rle tem $HAVE bytes, esperado $WANT" >&2
    echo "           (bloco 4 dos story titulos pode estar na versao errada)" >&2
else
    echo "   menu_cache.rle: $HAVE bytes, versao corrigida (bloco 4 story titulos)"
fi

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

echo
echo "== conteudo =="
find "$OUT" -type f | wc -l
du -sh "$OUT"
echo
echo "pronto em $OUT"
echo "copie o CONTEUDO de $OUT para a raiz do pendrive"
