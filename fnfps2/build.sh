#!/bin/sh
# Build the FNF PS2 port in one command.
#
#   ./build.sh              build, then validate the ELF
#   ./build.sh --deploy     build, then stage the memory-card layout
#   ./build.sh --deploy-only stage the memory-card layout from the ELF you have
#   ./build.sh --fast       build with -O1 instead of -O2, to iterate quickly
#   ./build.sh --quick      build only, skip the offline suite and validation
#   ./build.sh --clean      delete every object and start over
#   ./build.sh --tests      run only the offline suite (no PS2 toolchain needed)
#   ./build.sh --help
#
# The offline suite runs first on purpose: it is pure C plus Python, it needs no
# toolchain, and it catches the mistakes that are expensive to find in a PS2
# build. A chart that does not load or a chart-events regression fails here in
# about ten seconds instead of after a full compile.
#
# The toolchain is NOT built here. It cannot be: this sandbox has no network
# access to the archives it needs, and the PS2 SDK's own build wants bison, flex,
# m4, texinfo, autoconf, automake, libtool and cmake, none of which can be
# installed. What this script does is find the toolchain you already have, use
# it, and tell you clearly when it is missing.

set -u

PROG=$(basename "$0")
HERE=$(cd "$(dirname "$0")" && pwd)
cd "$HERE" || exit 1

# ---------------------------------------------------------------- arguments

DO_TESTS=1
DO_BUILD=1
DO_DEPLOY_ONLY=0
FAST=0
DO_VALIDATE=1
DO_DEPLOY=0
DO_CLEAN=0
JOBS=""
TARGET="fnf_ps2_m84.elf"

while [ $# -gt 0 ]; do
    case "$1" in
        --deploy)  DO_DEPLOY=1 ;;
        --deploy-only) DO_DEPLOY=1; DO_BUILD=0; DO_TESTS=0 ;;
        --fast)    FAST=1 ;;
        --quick)   DO_TESTS=0; DO_VALIDATE=0 ;;
        --tests)   DO_BUILD=0; DO_VALIDATE=0 ;;
        --clean)   DO_CLEAN=1 ;;
        --no-tests) DO_TESTS=0 ;;
        --jobs)    shift; JOBS="${1:-}" ;;
        --jobs=*)  JOBS="${1#--jobs=}" ;;
        --elf)     shift; TARGET="${1:-}" ;;
        -h|--help)
            sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
            exit 0 ;;
        *) echo "$PROG: unknown option '$1' (try --help)" >&2; exit 2 ;;
    esac
    shift
done

# ------------------------------------------------------------------ output

if [ -t 1 ]; then
    C_RED=$(printf '\033[31m'); C_GRN=$(printf '\033[32m')
    C_YEL=$(printf '\033[33m'); C_BLD=$(printf '\033[1m'); C_OFF=$(printf '\033[0m')
else
    C_RED=""; C_GRN=""; C_YEL=""; C_BLD=""; C_OFF=""
fi

step() { printf '%s==>%s %s\n' "$C_BLD" "$C_OFF" "$1"; }
ok()   { printf '    %sok%s   %s\n' "$C_GRN" "$C_OFF" "$1"; }
warn() { printf '    %swarn%s %s\n' "$C_YEL" "$C_OFF" "$1"; }
die()  { printf '\n%s%s%s\n' "$C_RED" "$1" "$C_OFF" >&2; exit 1; }

# ------------------------------------------------------------ the toolchain

# Where the toolchain might live, in the order to try. The first is the one the
# build has been reproduced with; the rest are the usual places an installer
# puts it, so a fresh machine does not need an environment variable set.
find_toolchain() {
    for d in \
        "${PS2DEV:-}" \
        /var/tmp/ps2dev-root/ps2dev \
        /usr/local/ps2dev \
        /opt/ps2dev \
        "$HOME/ps2dev" \
        /usr/local/ps2sdk
    do
        [ -n "$d" ] || continue
        if [ -x "$d/bin/ee-gcc" ] || [ -x "$d/ee/bin/ee-gcc" ]; then
            printf '%s\n' "$d"; return 0
        fi
        if [ -f "$d/ps2sdk/Makefile.pref" ] || [ -x "$d/ps2sdk/bin/ee-gcc" ]; then
            printf '%s\n' "$d"; return 0
        fi
    done
    return 1
}

# ------------------------------------------------------------------- start

START=$(date +%s)
echo
step "FNF PS2 build"
printf '    target %s, %s cores\n' "$TARGET" "$(nproc 2>/dev/null || echo '?')"

# ------------------------------------------------------------- clean first

if [ "$DO_CLEAN" = 1 ]; then
    step "clean"
    make clean >/dev/null 2>&1
    rm -rf build
    ok "objects and build output removed"
fi

# --------------------------------------------------- offline suite, no SDK

if [ "$DO_TESTS" = 1 ]; then
    step "offline suite (no PS2 toolchain needed)"
    if ! command -v gcc >/dev/null 2>&1; then
        warn "no host gcc, skipping the offline suite"
    elif ! command -v python3 >/dev/null 2>&1; then
        warn "no python3, skipping the offline suite"
    else
        T0=$(date +%s)
        if ./test/run_tests.sh >build-tests.log 2>&1; then
            ok "all suites passed ($(($(date +%s) - T0))s)"
        else
            printf '\n'
            # Show the tail of the log, which is where a failure reports itself,
            # rather than making the user scroll the whole thing.
            tail -25 build-tests.log
            rm -f build-tests.log
            die "the offline suite failed. Fix that first -- a PS2 build would
     only repeat the same mistake more slowly."
        fi
        rm -f build-tests.log
    fi
fi

# ------------------------------------------------------------------- build

if [ "$DO_BUILD" = 1 ] && [ "$DO_DEPLOY_ONLY" = 0 ]; then
    PS2DEV=$(find_toolchain) || PS2DEV=""
    if [ -z "$PS2DEV" ]; then
        cat >&2 <<'MSG'

  No PS2 toolchain found.

  Looked in:  $PS2DEV, /var/tmp/ps2dev-root/ps2dev, /usr/local/ps2dev,
              /opt/ps2dev, ~/ps2dev, /usr/local/ps2sdk

  This sandbox cannot build one for you: the PS2 SDK's build needs bison, flex,
  m4, texinfo, autoconf, automake, libtool and cmake, and none of them can be
  installed here. On your Ubuntu box:

      git clone https://github.com/ps2dev/ps2toolchain
      cd ps2toolchain && ./build-all.sh

  then either put it in one of the paths above, or:

      export PS2DEV=/path/to/ps2dev
      ./build.sh

MSG
        exit 1
    fi

    export PS2DEV
    export PS2SDK="$PS2DEV/ps2sdk"
    case ":$PATH:" in
        *":$PS2DEV/bin:"*) ;;
        *) export PATH="$PS2DEV/bin:$PS2DEV/ee/bin:$PS2DEV/iop/bin:$PS2SDK/bin:$PATH" ;;
    esac

    step "building with $(basename "$PS2DEV")"
    [ -x "$PS2DEV/bin/ee-gcc" ] || [ -x "$PS2DEV/ee/bin/ee-gcc" ] \
        || warn "ee-gcc not on PATH; the SDK's Makefile.pref will supply it"

    N=$(nproc 2>/dev/null || echo 1)
    [ -n "$JOBS" ] && N="$JOBS"

    # FNX_EXTRA is appended after -O2, so a trailing -O1 wins. This is the
    # Makefile's own extension point; overriding EE_CFLAGS on the command line
    # would discard the -D_EE that Makefile.pref composes and the build would
    # break in tamtypes.h, which is exactly what its comment warns about.
    EXTRA=""
    if [ "$FAST" = 1 ]; then
        EXTRA="-O1"
        printf '    %sfast build%s: -O1, no validation, timing on screen\n' "$C_YEL" "$C_OFF"
    fi

    # Capture the log so a failure can be reported as the errors alone. A PS2
    # build with -Wall -Wextra produces hundreds of lines, and the one that
    # matters is easy to lose in them.
    if make -j"$N" $EXTRA "$TARGET" >build.log 2>&1; then
        ok "compiled ($(($(date +%s) - START))s total)"
    else
        printf '\n%s%s%s\n' "$C_RED" "build failed. The errors, and the lines around them:" "$C_OFF" >&2
        # error: lines first, then the few lines before each so the failing
        # source line is visible, then the last of the log for context.
        grep -n -E 'error:|Error [0-9]|undefined reference|No such file|cannot find' build.log \
            | head -40
        printf '\n%s\n' "--- context ---"
        grep -n -B2 -A2 -E 'error:' build.log | head -60
        printf '\n%s\n' "--- full log: build.log ---"
        rm -f build.log
        die "build failed"
    fi
    rm -f build.log

    [ -f "$TARGET" ] || die "make reported success but $TARGET is not there"

    # ---------------------------------------------------------- validate
    if [ "$DO_VALIDATE" = 1 ]; then
        step "validating $TARGET"
        SIZE=$(wc -c <"$TARGET" | tr -d ' ')
        # The build this port is reproduced with produces 5,089,600 bytes. A
        # large jump means something was linked in that should not be, or a
        # pack stopped being embedded.
        if [ "$SIZE" -lt 1000000 ]; then
            die "$TARGET is only $SIZE bytes; something did not link in"
        fi
        if [ "$SIZE" -gt 20000000 ]; then
            warn "$TARGET is $SIZE bytes, larger than the 5,089,600 B baseline"
        else
            ok "$TARGET is $SIZE bytes (baseline 5,089,600)"
        fi

        if command -v file >/dev/null 2>&1; then
            F=$(file -b "$TARGET")
            case "$F" in
                *ELF*MIPS*|*MIPS*ELF*) ok "it is a MIPS ELF" ;;
                *) die "$TARGET is not a MIPS ELF: $F" ;;
            esac
        else
            warn "no 'file' command, skipping the ELF type check"
        fi

        if command -v ee-objdump >/dev/null 2>&1; then
            if ee-objdump -h "$TARGET" 2>/dev/null | grep -q '\.text'; then
                ok "it has a .text section"
            else
                warn "could not read the section table"
            fi
        fi
    fi
fi

# ------------------------------------------------------------------ deploy

if [ "$DO_DEPLOY" = 1 ]; then
    step "staging the memory-card layout"
    [ -f "$TARGET" ] || die "nothing to deploy: $TARGET does not exist"

    # The port reads everything under mass:/FNFPS2/. The ELF goes at the root of
    # that folder and the assets under assets/, with each song's chart at
    # assets/songs/<id>/<difficulty>.chart -- which is the layout the registry
    # builds, so the packaging and the loader cannot disagree.
    OUT="${FNF_DEPLOY:-build/ps2}"
    rm -rf "$OUT"
    mkdir -p "$OUT/FNFPS2/assets"

    cp "$TARGET" "$OUT/FNFPS2/" || die "could not copy the ELF"
    ok "ELF -> $OUT/FNFPS2/$(basename "$TARGET")"

    # The assets are not in the workspace: twelve of them exist only on the
    # pendrive. Rather than fail, stage what is here and list what is missing,
    # so the user knows exactly what to copy across.
    if [ -d assets ] && [ -n "$(ls -A assets 2>/dev/null)" ]; then
        cp -r assets/. "$OUT/FNFPS2/assets/" 2>/dev/null
        ok "assets -> $OUT/FNFPS2/assets/ ($(find "$OUT/FNFPS2/assets" -type f | wc -l | tr -d ' ') files)"
    else
        warn "no assets/ directory in the workspace"
    fi

    # The charts, laid out the way the registry expects them.
    if [ -d build/charts ]; then
        for f in build/charts/*.chart; do
            [ -e "$f" ] || continue
            b=$(basename "$f" .chart)
            sid=${b%-*}
            diff=${b##*-}
            mkdir -p "$OUT/FNFPS2/assets/songs/$sid"
            cp "$f" "$OUT/FNFPS2/assets/songs/$sid/$diff.chart"
        done
        ok "charts -> $OUT/FNFPS2/assets/songs/ ($(find "$OUT/FNFPS2/assets/songs" -name '*.chart' | wc -l | tr -d ' ') files)"
    fi

    printf '\n    Copy %s/FNFPS2/ to the memory card as mass:/FNFPS2/\n\n' "$OUT"
    printf '    The port also reads these, which are not in the workspace and\n'
    printf '    must come from the pendrive:\n'
    for a in bf_frames.lz4f gf_frames.lz4f mainstage_tutorial_parallax.rgba \
             font.rgba font.widths freakyMenu_48000.pcm menu_sfx.pcm \
             audio_stems.pcm menu_cache.rle \
             tutorial_hud_official_320x256_gsalpha.rgba \
             title_alphabet.rgba title_newgrounds.rgba \
             title_prompt_l.rgba title_prompt_r.rgba \
             title_logoBumpin.frames title_gfDanceTitle.frames; do
        printf '      assets/%s\n' "$a"
    done
    printf '\n'
fi

printf '%sdone%s in %ss\n\n' "$C_GRN" "$C_OFF" "$(($(date +%s) - START))"
exit 0
