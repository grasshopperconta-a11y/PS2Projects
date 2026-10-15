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

echo "== bs_dados.h stage table matches the game's own JSON =="
python3 tools/check_bs_dados.py
echo

echo "== stage geometry =="
python3 tools/dump_stage_geometry.py
echo

echo "== chart converter =="
python3 tools/fnf_to_fch3.py --selftest
echo

# The converter's own selftest uses synthetic charts, which is how two bugs
# survived for so long. This converts the REAL charts and loads them with the
# REAL loader, so the two halves of the pipeline are checked against each
# other and against the game's own data.
echo "== real charts -> FCH3 -> real loader =="
mkdir -p build/charts
for f in assets-data/charts/*-chart.json; do
    sid=$(basename "$f" -chart.json)
    for diff in easy normal hard; do
        python3 tools/fnf_to_fch3.py \
            --metadata "assets-data/songs/$sid-metadata.json" \
            --chart "$f" \
            --difficulty "$diff" -o "build/charts/$sid-$diff.chart" >/dev/null
    done
done
$CC $FLAGS test/test_chart_limits.c -o /tmp/fnf_test_chart_limits
/tmp/fnf_test_chart_limits build/charts
echo

for f in build/charts/*.chart; do
    base=$(basename "$f" .chart)
    sid=${base%-*}
    diff=${base##*-}
    # the expected note count comes from the JSON itself, not from the test
    want=$(python3 -c "
import json
d = json.load(open('assets-data/charts/$sid-chart.json'))
print(len(d['notes'].get('$diff', [])))")
    if ! /tmp/fnf_test_real_chart "$f" "$want" "$sid" >/dev/null 2>&1; then
        echo "  FAIL: $base"
        /tmp/fnf_test_real_chart "$f" "$want" "$sid" || true
        exit 1
    fi
done
echo "  all $(ls build/charts | wc -l) charts load in the real loader"
echo

echo "ALL SUITES PASSED"
