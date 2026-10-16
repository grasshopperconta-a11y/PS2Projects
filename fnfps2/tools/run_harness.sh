#!/bin/sh
# Harness de link + execucao: compila o JOGO DE VERDADE (main.c e todos os
# modulos) contra o codigo REAL de draw/packet do ps2sdk, e executa no PC com
# um pacote de tamanho limitado e zona de guarda.
#
# O que ele pega que o console nao pega:
#   - estouro do pacote de quadro: morre aqui, com o numero do quadro e o
#     tamanho real, em vez de corromper a memoria do PS2 em silencio;
#   - envio DMA acima de QWC_MAX (65535), que o DMAC rechaca;
#   - asset que nao abriu, com o caminho exato;
#   - escrita na zona de guarda, que prova que algo passou do limite.
#
# Uso:  tools/run_harness.sh [quadros] [raiz-dos-assets]
# Variaveis: PS2H_FRAMES, PS2H_ROOT, PS2H_STRICT, PS2SDK_HEADERS

set -u

REPO=$(cd "$(dirname "$0")/.." && pwd)
cd "$REPO" || exit 1

FRAMES=${1:-${PS2H_FRAMES:-240}}
ROOT=${2:-${PS2H_ROOT:-build/harness_assets}}
ASSET_ROOT=${ASSET_ROOT:-build/harness_assets}

SDK=${PS2SDK_HEADERS:-/tmp/fnf-ps2sdk-headers}
if [ ! -f "$SDK/common/include/tamtypes.h" ]; then
    echo "== baixando os fontes do ps2sdk em $SDK =="
    rm -rf "$SDK"
    git clone --depth 1 -q https://github.com/ps2dev/ps2sdk.git "$SDK" || {
        echo "FALHA: nao consegui obter o ps2sdk. Defina PS2SDK_HEADERS."; exit 1; }
fi

INC=$(find "$SDK" -type d -name include | sed 's|^|-I|' | tr '\n' ' ')
FLAGS="-O1 -g -std=gnu11 -D_EE -Itools/ps2shim $INC -Isrc -Isrc/engine -Itest/ps2harness -Wall -Wextra -Wno-int-to-pointer-cast -Wno-pointer-to-int-cast -Wno-unused-parameter"
# --wrap: conta as chamadas de desenho do ps2sdk sem alterar uma linha do draw.c
WRAPS="-Wl,--wrap=draw_rect_filled -Wl,--wrap=draw_rect_textured -Wl,--wrap=draw_setup_environment -Wl,--wrap=draw_texture_transfer"

mkdir -p build

# O codigo de draw eh o do ps2sdk, nao uma reimplementacao: assim a contagem
# de quadwords de cada primitiva eh exatamente a que o console vera.
#
# Um unico ajuste, e ele eh mecanico: draw_log2() usa __asm__("plzcw"), que so
# existe no MIPS. O harness roda no PC, entao esse bloco #ifdef _EE vira o
# caminho portatil que o proprio ps2sdk ja tem no #else. NADA MAIS eh tocado --
# e o diff abaixo prova isso, falhando o build se alguem mudar outra coisa.
HOSTDIR=build/ps2sdk_host
mkdir -p "$HOSTDIR"
for f in draw draw2d draw_environment; do
    cp "$SDK/ee/draw/src/$f.c" "$HOSTDIR/$f.c"
done
python3 - "$HOSTDIR" <<'PYEOF'
import sys, re, subprocess
d = sys.argv[1]
orig = "/tmp/fnf-ps2sdk-headers/ee/draw/src"
# Troca o corpo asm de draw_log2 pelo caminho portatil do #else.
src = open(d + "/draw.c").read()
new = src.replace(
    '#ifdef _EE\n\t__asm__ __volatile__ ("plzcw %0, %1\\n\\t" : "=r" (res) : "r" (x));\n#else\n',
    '#if 0\n\t__asm__ __volatile__ ("plzcw %0, %1\\n\\t" : "=r" (res) : "r" (x));\n#else\n')
if new == src:
    sys.exit("harness: nao encontrei o bloco plzcw em draw.c -- o ps2sdk mudou?")
open(d + "/draw.c", "w").write(new)
# Prova: a unica diferenca contra o original eh essa linha.
for f in ("draw", "draw2d", "draw_environment"):
    r = subprocess.run(["diff", "-u", orig + "/" + f + ".c", d + "/" + f + ".c"],
                       capture_output=True, text=True).stdout
    changed = [l for l in r.split("\n") if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
    if f == "draw" and changed != ["-#ifdef _EE", "+#if 0"]:
        sys.exit("harness: diff inesperado em draw.c: %r" % changed)
    if f != "draw" and changed:
        sys.exit("harness: %s.c foi alterado sem necessidade: %r" % (f, changed))
print("  draw do ps2sdk: 1 linha adaptada (plzcw), 0 linhas de logica tocadas")
PYEOF
[ $? -eq 0 ] || exit 1

DRAWSRC="$HOSTDIR/draw.c $HOSTDIR/draw2d.c $HOSTDIR/draw_environment.c"

echo "== compilando o harness (jogo real + draw real do ps2sdk) =="
gcc $FLAGS \
    src/main.c src/audio_ring.c src/chart.c src/chart_events.c src/telemetry.c \
    src/engine/song_registry.c src/engine/vram_cache.c src/engine/io_fila.c \
    src/iomanX_irx.c src/fileXio_irx.c src/usbd_irx.c src/usbhdfsd_irx.c src/audsrv_irx.c \
    src/title_packs.S src/story_packs.S \
    test/ps2harness/ps2h.c \
    $DRAWSRC \
    -o build/fnf_harness -lm $WRAPS -lpthread 2> build/harness_cc.log
rc=$?
if [ $rc -ne 0 ]; then
    echo "FALHOU a compilacao do harness:"
    grep -E "error:" build/harness_cc.log | head -30
    exit 1
fi
nwarn=$(grep -c "warning:" build/harness_cc.log)
echo "  compilou: $(wc -c < build/fnf_harness) bytes, $nwarn avisos"

echo
echo "== gerando a raiz de assets (o jogo le tudo de mass:/FNFPS2/assets) =="
python3 tools/gen_harness_assets.py "$ASSET_ROOT" || exit 1

echo
echo "== executando $FRAMES quadros com raiz de assets '$ROOT' =="
# Watchdog sempre ligado: uma ferramenta de verificacao que fica pendurada sem
# dizer onde eh pior do que uma que falha. PS2H_WATCHDOG esta em segundos.
PS2H_FRAMES="$FRAMES" PS2H_ROOT="$ROOT" PS2H_WATCHDOG="${PS2H_WATCHDOG:-180}" PS2H_STRICT="${PS2H_STRICT:-1}" \
    timeout -s KILL $(( ${PS2H_WATCHDOG:-120} + 30 )) ./build/fnf_harness
rc=$?
if [ $rc -eq 137 ] || [ $rc -eq 9 ]; then
    echo
    echo "HARNESS: o jogo travou e foi morto. Veja o backtrace acima."
    exit 1
fi

echo
if [ $rc -eq 0 ]; then
    echo "HARNESS: terminou sem travamento."
else
    echo "HARNESS: encerrou com codigo $rc."
fi
exit $rc
