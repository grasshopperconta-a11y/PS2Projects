#!/usr/bin/env python3
"""Check that every asset the port reads at runtime is on disk, and that its
size matches the size Google Drive reports.

    ./check_assets.py assets            # check a directory
    ./check_assets.py --missing-only    # just list what is absent

The sizes come from assets-manifest.json, so a truncated download -- which is
the usual way a pendrive copy goes wrong -- is caught here rather than as a
crash on the console. Nothing is modified.
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.normpath(os.path.join(HERE, "..", "assets-manifest.json"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("directory", nargs="?", default="assets")
    ap.add_argument("--missing-only", action="store_true")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    with open(MANIFEST) as fh:
        man = json.load(fh)

    assets = {n: m for n, m in man["assets"].items() if m.get("required")}
    required = len(assets)
    missing, wrong_size, ok = [], [], []

    for name, meta in sorted(assets.items()):
        path = os.path.join(args.directory, name)
        if not os.path.isfile(path):
            missing.append((name, meta))
            continue
        got = os.path.getsize(path)
        if got != meta["bytes"]:
            wrong_size.append((name, meta, got))
        else:
            ok.append(name)

    if args.as_json:
        print(json.dumps(
            {"required": required, "present": ok, "missing": [m[0] for m in missing],
             "wrong_size": [w[0] for w in wrong_size]},
            indent=2))
        return 0

    if not args.missing_only:
        print("%d of %d required assets present and correctly sized" % (len(ok), required))
        for name in ok:
            print("  ok      %s" % name)

    if wrong_size:
        print()
        print("%d asset(s) are the wrong size -- the download was interrupted:" % len(wrong_size))
        for name, meta, got in wrong_size:
            print("  %s" % name)
            print("      expected %d bytes, found %d (Drive id %s)"
                  % (meta["bytes"], got, meta["drive_id"]))

    if missing:
        print()
        print("%d required asset(s) are missing:" % len(missing))
        for name, meta in missing:
            print("  %s  (%d bytes)" % (name, meta["bytes"]))
            print("      Drive file id: %s" % meta["drive_id"])
        print()
        print("Download them from %s" % man["drive_folder_url"])
        print("and put them in %s/" % args.directory.rstrip("/"))

    if missing or wrong_size:
        return 1
    if args.missing_only:
        print("all %d required assets are present and correctly sized" % required)
    return 0


if __name__ == "__main__":
    sys.exit(main())
