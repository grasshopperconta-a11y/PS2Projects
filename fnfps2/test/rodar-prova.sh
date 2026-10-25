#!/bin/sh
# Roda a prova do port por EXECUCAO, no PC, sem PS2.
#
# O que este script faz:
#   1. compila os 6 modulos do port que rodam no host (chart, chart_events,
#      song_registry, vram_cache, io_fila, audio_ring)
#   2. compila o shim de host (pthreads por baixo das primitivas do PS2)
#   3. compila e roda test/prova_port.c
#   4. gera o relatorio de cobertura POR FUNCAO com gcov
#
# Por que 6 e nao 8: main.c e telemetry.c dependem de ps2sdk (libmc, libpad,
# gsKit, audsrv). Eles NAO rodam no host -- a prova deles eh outra: a
# compilacao completa para o PS2, que nao emite um warning sequer.
#
# Uso: sh test/rodar-prova.sh
set -e
cd "$(dirname "$0")/.."

SRC=src
INC="-I$SRC -I$SRC/engine -Itest/host-shim"
OUT=/tmp/prova_port_build
rm -rf "$OUT"; mkdir -p "$OUT"

echo "== compilando os modulos do port =="
for m in chart chart_events; do
    gcc -O1 -g --coverage -std=gnu11 $INC -c $SRC/$m.c -o $OUT/$m.o
done
for m in song_registry vram_cache io_fila; do
    gcc -O1 -g --coverage -std=gnu11 $INC -c $SRC/engine/$m.c -o $OUT/$m.o
done
gcc -O1 -g --coverage -std=gnu11 $INC -c $SRC/audio_ring.c -o $OUT/audio_ring.o
gcc -O1 -g --coverage -std=gnu11 $INC -c test/host-shim/host_thread_stubs.c \
    -o $OUT/host_thread_stubs.o
gcc -O1 -g --coverage -std=gnu11 $INC -c test/prova_port.c -o $OUT/prova_port.o

echo "== ligando =="
gcc --coverage -o $OUT/prova_port $OUT/prova_port.o $OUT/chart.o \
    $OUT/chart_events.o $OUT/song_registry.o $OUT/vram_cache.o \
    $OUT/io_fila.o $OUT/audio_ring.o $OUT/host_thread_stubs.o \
    -lm -lpthread

echo "== rodando =="
cd "$OUT"
./prova_port
rc=$?
if [ $rc -ne 0 ]; then echo "PROVA FALHOU (rc=$rc)"; exit $rc; fi

echo
echo "== cobertura por funcao (funcao com 0 linhas executadas NAO foi testada) =="
for m in chart chart_events song_registry vram_cache io_fila audio_ring; do
    gcov -f -o . $m.gcda 2>/dev/null | grep -A1 '^Function' | paste - - - \
      | sed 's/^Function //;s/Lines executed://;s/^\x27//;s/\x27\t/\t/' \
      | sed "s/^/$m\t/"
done | tee cobertura.txt

zero=$(grep -cE '(^|[^0-9])0\.00% of [1-9]' cobertura.txt || true)
echo
echo "funcoes sem nenhuma linha executada: $zero  (tem de ser 0)"
