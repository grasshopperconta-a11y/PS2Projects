#!/bin/sh
# Print the first directory that looks like a ps2dev installation.
#
#   ./find_ps2dev.sh            -> /usr/local/ps2dev, or nothing
#   PS2DEV=/where ./find_ps2dev.sh
#
# Why a script and not a loop in the .bat: the Windows launcher has to ask the
# shell a question, and piping that through cmd.exe's for /f means escaping the
# shell's own operators (||, $, quotes) for a second parser. Doing it here
# keeps one parser instead of two, and it is testable.
#
# /usr/local/ps2dev comes first because that is where ps2toolchain's
# build-all.sh installs, and it is where the usual installation ends up.
for p in "${PS2DEV:-}" /usr/local/ps2dev "$HOME/ps2dev" \
         /opt/ps2dev /usr/local/ps2sdk /var/tmp/ps2dev-root/ps2dev; do
    [ -n "$p" ] || continue
    if [ -x "$p/bin/ee-gcc" ] || [ -x "$p/ee/bin/ee-gcc" ]; then
        printf '%s\n' "$p"
        exit 0
    fi
done
exit 1
