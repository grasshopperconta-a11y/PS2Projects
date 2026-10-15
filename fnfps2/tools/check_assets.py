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
    ap.add_argument("--links", action="store_true",
                    help="write assets-faltando.html with one download link per "
                         "missing asset, so a browser that is already signed in "
                         "can fetch them without copying ids by hand")
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

    # A page with one link per missing asset. Drive will not hand a file to an
    # unauthenticated wget, and the browser is already signed in, so a page of
    # links is the reliable way to get them -- no ids to copy by hand.
    if args.links and (missing or wrong_size):
        _write_links(man, missing, wrong_size)

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




def _write_links(man, missing, wrong_size):
    """Write assets-faltando.html: one clickable link per asset still needed."""
    rows = []
    for name, meta in missing:
        rows.append((name, meta["bytes"], "faltando",
                     "https://drive.google.com/file/d/%s/view" % meta["drive_id"]))
    for name, meta, got in wrong_size:
        rows.append((name, meta["bytes"], "tamanho errado (%d B)" % got,
                     "https://drive.google.com/file/d/%s/view" % meta["drive_id"]))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "assets-faltando.html")
    out = os.path.normpath(out)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("""<!doctype html>
<meta charset="utf-8">
<title>Assets que faltam</title>
<style>
 body { font: 15px/1.5 system-ui, sans-serif; max-width: 60em; margin: 2em auto; padding: 0 1em; }
 h1 { font-size: 1.3em; }
 p  { color: #555; }
 li { margin: .5em 0; }
 a  { color: #06c; }
 .sz { color: #888; font-size: .85em; }
 .bad { color: #a60; }
</style>
<h1>Assets que faltam</h1>
<p>Clique em cada link, baixe o arquivo, e mova todos para a pasta
<code>assets/</code> ao lado desta pagina. Depois rode
<code>./build.sh --check-assets</code> de novo &mdash; ele confere o tamanho
byte a byte, ent&atilde;o um download pela metade &eacute; pego.</p>
<ol>
""")
        for name, size, why, url in rows:
            fh.write('<li><a href="%s">%s</a> <span class="sz">%s &middot; '
                     '%d bytes</span>%s</li>\n'
                     % (url, name, why, size,
                        ' <span class="bad">&larr; baixar de novo, veio '
                        'incompleto</span>' if why != "faltando" else ""))
        fh.write('</ol>\n<p>Ou a pasta inteira, se preferir: '
                 '<a href="%s">%s</a></p>\n'
                 % (man["drive_folder_url"], man["drive_folder_url"]))
    print("\nLinks escritos em: assets-faltando.html")


if __name__ == "__main__":
    sys.exit(main())