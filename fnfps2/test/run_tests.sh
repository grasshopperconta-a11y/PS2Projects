#!/bin/sh
# Offline test suite for the pure-C engine modules.
# These modules have no PS2 dependency on purpose (see each header), so they
# are exercised on the PC against the real data before anything is built for
# the console.
set -e
cd "$(dirname "$0")/.."
CC=${CC:-gcc}
# -Isrc is needed because song_registry.c includes bs_dados.h from src/, and
# -Isrc/engine because it includes its own header and the generated data.
# -Itest/ps2sdk-shim supplies the u8/u16/u32 typedefs the chart loader takes
# from tamtypes.h, so the loader can be tested unmodified on the PC.
FLAGS="-O2 -Wall -Wextra -Werror -std=gnu11 -Isrc -Isrc/engine -Itest/ps2sdk-shim"

echo "== vram_cache + io_fila =="
$CC $FLAGS test/test_engine.c src/engine/vram_cache.c src/engine/io_fila.c -o /tmp/fnf_test_engine
/tmp/fnf_test_engine
echo

echo "== song_registry =="
$CC $FLAGS test/test_registry.c src/engine/song_registry.c -o /tmp/fnf_test_registry
/tmp/fnf_test_registry
echo

# The committed C must be a rendering of the committed JSON. If someone edits
# song_registry_data.inc by hand, or drops a JSON in without re-running the
# generator, this is where it is caught.
echo "== song_registry is generated from assets-data/ =="
python3 tools/gen_song_registry.py --check
echo

echo "== chart converter =="
python3 tools/fnf_to_fch3.py --selftest
echo

# The converter's own selftest uses synthetic charts, which is how the two bugs
# below survived for so long. This converts a REAL chart and loads it with the
# REAL loader, so the two halves of the pipeline are checked against each other.
echo "== real chart -> FCH3 -> real loader =="
for diff in easy normal hard; do
    python3 tools/fnf_to_fch3.py \
        --metadata assets-data/songs/tutorial-metadata.json \
        --chart assets-data/charts/tutorial-chart.json \
        --difficulty "$diff" -o "/tmp/tutorial-$diff.chart" >/dev/null
    # the expected note count comes from the JSON itself, not from the test
    want=$(python3 -c "
import json,sys
d=json.load(open('assets-data/charts/tutorial-chart.json'))
print(len(d['notes']['$diff']))")
    printf '  %-7s ' "$diff:"
    /tmp/fnf_test_real_chart "/tmp/tutorial-$diff.chart" "$want" | tail -1
done
echo

echo "ALL SUITES PASSED"
