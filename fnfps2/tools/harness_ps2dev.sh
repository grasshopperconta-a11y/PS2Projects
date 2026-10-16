#!/bin/sh
# Monta o toolchain ps2dev a partir de google_drive/tree/ e compila o ELF com os
# flags exatos do Makefile.eeglobal do ps2sdk. Veja HARNESS_TOOLCHAIN.md para o
# porquê de cada flag e para a armadilha dos nomes repetidos de header.
#
# Uso: tools/harness_ps2dev.sh [versao] [elf-de-saida] [dir-de-objetos]

set -u

REPO=$(cd "$(dirname "$0")/.." && pwd)
SRC="$REPO"
[ -f "$SRC/src/main.c" ] || SRC="$REPO/fnfps2"
DL="$SRC/google_drive/tree"
[ -d "$DL" ] || DL="$REPO/google_drive/tree"

R=${PS2DEV_HARNESS:-/tmp/ps2dev}
VER=${1:-0.2.105-aceito-exato}
OUT=${2:-/tmp/fnf_ps2_m84.elf}
O=${3:-/tmp/harness-objs}

if [ ! -f "$DL/bin/mips64r5900el-ps2-elf-gcc" ]; then
    echo "FALTA o toolchain em $DL"
    echo "Os binários somam ~100 MB e o snapshot do workspace os podou."
    echo "Veja HARNESS_TOOLCHAIN.md: ele lista o que baixar do Drive."
    exit 1
fi

# A árvore de destino reproduz o layout do $PS2DEV. cp -r de uma vez: os
# subdiretórios são o que impede os headers homônimos de se sobrescrever.
rm -rf "$R"
mkdir -p "$(dirname "$R")"
cp -r "$DL" "$R"

G="$R/libexec/gcc/mips64r5900el-ps2-elf/15.2.0"
GG="$R/lib/gcc/mips64r5900el-ps2-elf/15.2.0"
chmod +x "$R"/bin/* "$G"/cc1 "$G"/lto1 "$G"/lto-wrapper 2>/dev/null

# Sem prefixo: o driver procura "as"/"ld" nus, e sem estes links pega o
# assembler x86 do host, que rejeita -EL.
( cd "$R/bin" && for n in as ld ar nm strip objcopy ranlib readelf size strings objdump c++filt; do
    ln -sf "mips64r5900el-ps2-elf-$n" "$n"; done )

cd "$SRC" || exit 1
export PATH="$R/bin:$PATH"

# Flags: Makefile.eeglobal define EE_CFLAGS e a regra de link. O projeto acrescenta
# -Isrc -Isrc/engine e o -DFNF_PS2_VERSION.
CF="-D_EE -G0 -O2 -Wall -Wextra -Werror=implicit-function-declaration -std=gnu11"
CF="$CF -I$R/ps2sdk/ee/include -I$R/ps2sdk/common/include -I. -Isrc -Isrc/engine"

rm -rf "$O"; mkdir -p "$O"
fail=0
for f in src/*.c src/engine/*.c src/*.S; do
    [ -f "$f" ] || continue
    o="$O/$(basename "$f" | sed 's/\.[cS]$/.o/')"
    "$R/bin/mips64r5900el-ps2-elf-gcc" $CF \
        -DFNF_PS2_VERSION="\"$VER\"" -c "$f" -o "$o" 2>&1 | grep -E "error:"
    [ -f "$o" ] || { echo "FALHOU: $f"; fail=1; }
done
[ "$fail" = 0 ] || exit 1
echo "objetos: $(ls "$O"/*.o | wc -l)  bytes: $(cat "$O"/*.o | wc -c)"

# O link: -T com o linkfile do ps2sdk e -zmax-page-size=128. Sem os dois o ELF
# sai com o layout default do ld, que é menor e nao é o que o console espera.
"$R/bin/mips64r5900el-ps2-elf-gcc" -T"$R/ps2sdk/ee/startup/linkfile" -O2 \
    -o "$OUT" "$O"/*.o \
    -L"$R/ps2sdk/ee/lib" -L"$R/mips64r5900el-ps2-elf/lib" -Wl,-zmax-page-size=128 \
    -ldraw -lgraph -lpacket -ldma -lmath3d -lpad -laudsrv -lfileXio \
    -lpatches -lkernel -lcglue -lcdvd -lpthreadglue \
    -Wl,-Map,"${OUT%.elf}.map" 2>&1 | grep -E "error|undefined|cannot find"

[ -f "$OUT" ] || { echo "LINK FALHOU"; exit 1; }
echo "ELF: $OUT  $(wc -c < "$OUT") bytes"
