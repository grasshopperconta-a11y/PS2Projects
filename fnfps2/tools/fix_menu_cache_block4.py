#!/usr/bin/env python3
"""Reconstrói o bloco 4 (story titulos) de menu_cache.rle.

O arquivo que esta no Drive tem o bloco 4 de uma versao diferente: 224.519 bytes
de origem para 379.264 bytes de destino, enquanto o jogo espera 188.635 para
306.180. Os tres primeiros blocos decodificam perfeito, entao so o quarto esta
velho. Este script mantem os tres blocos reais intactos e reescreve so o quarto,
renderizando os 9 nomes do menu story com a FONT.RGBA REAL.

Uso: python3 tools/fix_menu_cache_block4.py <dir-dos-assets> [saida]
"""
import os
import struct
import sys

MENU_RLE = 1_288_182
FONT_RLE = 38_342
STORY_RLE = 72_402
ST_TITLES_RLE = 188_635
ST_TITLES_RAW = 306_180

FW, FH = 384, 192
CELL_W, CELL_H = 24, 32
GLYPHS = 96

# src/story_titles_generated.h
STORY_TITLES = [
    (0, 222, 41), (36408, 180, 44), (68088, 180, 44), (99768, 179, 44),
    (131272, 177, 44), (162424, 182, 46), (195912, 180, 46),
    (229032, 182, 50), (265432, 167, 61),
]
# src/main.c: g_story_names[9]
STORY_NAMES = [
    "TEACHING TIME", "DADDY DEAREST", "SPOOKY MONTH", "PICO",
    "MOMMY MUST MURDER", "RED SNOW", "HATING SIMULATOR FT. MOAWLING",
    "TANKMAN FT. JOHNNYUTAH", "DUE DEBTS",
]


def load_font(assets):
    rgba = open(os.path.join(assets, "font.rgba"), "rb").read()
    widths = open(os.path.join(assets, "font.widths"), "rb").read()
    if len(rgba) != FW * FH * 4:
        raise SystemExit("font.rgba tem %d bytes, esperado %d" % (len(rgba), FW * FH * 4))
    if len(widths) != GLYPHS:
        raise SystemExit("font.widths tem %d bytes, esperado %d" % (len(widths), GLYPHS))
    return rgba, widths


def glyph_alpha(font, n):
    """Devolve uma matriz CELL_H x CELL_W com o alpha do glifo n (0..95)."""
    cx = (n % 16) * CELL_W
    cy = (n // 16) * CELL_H
    rows = []
    for r in range(CELL_H):
        row = []
        for c in range(CELL_W):
            row.append(font[((cy + r) * FW + cx + c) * 4 + 3])
        rows.append(row)
    return rows


def render_text(font, widths, text, w, h):
    """Renderiza text centralizado num canvas w x h RGBA32, branco com o alpha
    do glifo. A escala escolhe o maior tamanho que caberia na largura."""
    if not text:
        return bytearray(w * h * 4)
    # largura natural na escala 1 (o jogo avanca advance*0.5 por glifo)
    natural = sum(widths[ord(ch) - 32] for ch in text if 32 <= ord(ch) <= 127) * 0.5
    if natural <= 0:
        return bytearray(w * h * 4)
    # cabe pela largura e pela altura; o menor dos dois ganha
    scale = min((w * 0.90) / natural, (h * 0.70) / 16.0)
    if scale <= 0:
        return bytearray(w * h * 4)
    draw_w = 12 * scale
    draw_h = 16 * scale
    total = natural * scale
    x = (w - total) * 0.5
    y = (h - draw_h) * 0.5
    out = bytearray(w * h * 4)
    cache = {}

    def px(cx, cy, alpha):
        if cx < 0 or cy < 0 or cx >= w or cy >= h:
            return
        o = (cy * w + cx) * 4
        if alpha > out[o + 3]:
            out[o] = out[o + 1] = out[o + 2] = 0xFF
            out[o + 3] = alpha

    for ch in text:
        n = ord(ch) - 32
        if not (0 <= n < GLYPHS):
            n = ord('?') - 32
        adv = widths[n] * 0.5 * scale
        if n not in cache:
            cache[n] = glyph_alpha(font, n)
        g = cache[n]
        # mapeia o cell 24x32 para o retangulo draw_w x draw_h
        for gy in range(CELL_H):
            fy = y + gy * (draw_h / CELL_H)
            iy = int(fy)
            for gx in range(CELL_W):
                a = g[gy][gx]
                if a == 0:
                    continue
                fx = x + gx * (draw_w / CELL_W)
                ix = int(fx)
                px(ix, iy, a)
                px(ix + 1, iy, a)
        x += adv
    return out


# ---------------------------------------------------------------- codificador
def rle_encode_exact(raw, target_bytes):
    """Codifica raw (multiplo de 4 bytes) num fluxo RLE que consuma EXATAMENTE
    target_bytes e produza exatamente len(raw). O decodificador do jogo devolve
    -4 se qualquer uma das duas contas nao fechar, entao as duas tem de bater.

    Formato (src/main.c rle_decode):
      c <  128 : literal, (c+1) pixels,  custa 1 + 4*(c+1) bytes de origem
      c >  128 : repeat,  (257-c) px,    custa 5 bytes de origem
                                   (1 de controle + 4 do pixel repetido)
      c == 128 : invalido
    """
    px = [tuple(raw[i:i + 4]) for i in range(0, len(raw), 4)]
    P = len(px)
    # tokens: (tipo, pixels, dado)
    #   tipo 'L': literal, dado = lista de pixels
    #   tipo 'R': repeat,  dado = pixel repetido
    toks = []
    i = 0
    while i < P:
        j = i
        while j < P and px[j] == px[i]:
            j += 1
        run = j - i
        # um token de repeat cobre no maximo 128 pixels
        while run >= 2:
            k = min(128, run)
            toks.append(['R', k, px[i]])
            i += k
            run -= k
        if run == 1:
            # literal: acumula enquanto o proximo nao repetir
            lit = [px[i]]
            i += 1
            while i < P and len(lit) < 128:
                k = i
                while k < P and px[k] == px[i]:
                    k += 1
                if k - i >= 2:
                    break
                lit.append(px[i])
                i += 1
            toks.append(['L', len(lit), lit])

    def size(toks):
        s = 0
        for t in toks:
            s += 5 if t[0] == 'R' else 1 + 4 * t[1]
        return s

    # Ajuste fino para bater o orcamento exato.
    def split_one_literal():
        for idx, t in enumerate(toks):
            if t[0] == 'L' and t[1] >= 2:
                half = t[1] // 2
                a = ['L', half, t[2][:half]]
                b = ['L', t[1] - half, t[2][half:]]
                toks[idx:idx + 1] = [a, b]
                return True
        return False

    def merge_two_literals():
        for idx in range(len(toks) - 1):
            if toks[idx][0] == 'L' and toks[idx + 1][0] == 'L':
                if toks[idx][1] + toks[idx + 1][1] <= 128:
                    m = ['L', toks[idx][1] + toks[idx + 1][1],
                         toks[idx][2] + toks[idx + 1][2]]
                    toks[idx:idx + 2] = [m]
                    return True
        return False

    def literal_to_repeat():
        # so da certo se todos os pixels do literal forem iguais
        for idx, t in enumerate(toks):
            if t[0] == 'L' and len(set(t[2])) == 1 and 2 <= t[1] <= 128:
                toks[idx] = ['R', t[1], t[2][0]]
                return True
        return False

    def repeat_to_literal():
        """Um repeat de m pixels custa 2 bytes; o mesmo conteudo como literal
        custa 1 + 4m. A saida decodificada eh IDENTICA, so o fluxo incha -- e eh
        exatamente isso que eu preciso para bater o orcamento sem mudar a
        imagem. Um literal nao passa de 128 pixels, entao runs longos quebram."""
        for idx, t in enumerate(toks):
            if t[0] != 'R':
                continue
            m = t[1]
            p = t[2]
            chunks = []
            left = m
            while left > 0:
                k = min(128, left)
                chunks.append(['L', k, [p] * k])
                left -= k
            toks[idx:idx + 1] = chunks
            return True
        return False

    guard = 0
    while size(toks) < target_bytes and guard < 5_000_000:
        guard += 1
        if not split_one_literal():
            if not repeat_to_literal():
                break
    guard = 0
    while size(toks) > target_bytes and guard < 5_000_000:
        guard += 1
        if not merge_two_literals():
            if not literal_to_repeat():
                break

    if size(toks) != target_bytes:
        raise SystemExit(
            "nao consegui bater o orcamento: tenho %d bytes, preciso %d"
            % (size(toks), target_bytes))

    out = bytearray()
    produced = 0
    for t in toks:
        if t[0] == 'R':
            n = 257 - t[1]
            if not (129 <= n <= 255):
                raise SystemExit("repeat de %d pixels nao cabe num token" % t[1])
            out.append(n)
            out += bytes(t[2])
            produced += t[1]
        else:
            n = t[1] - 1
            if not (0 <= n <= 127):
                raise SystemExit("literal de %d pixels nao cabe num token" % t[1])
            out.append(n)
            for p in t[2]:
                out += bytes(p)
            produced += t[1]
    if produced * 4 != len(raw):
        raise SystemExit("produzi %d pixels, esperado %d" % (produced, len(raw) // 4))
    return bytes(out)


def decode_check(src, want):
    si = di = 0
    n = len(src)
    while si < n and di < want:
        c = src[si]; si += 1
        if c < 128:
            k = (c + 1) * 4
            if si + k > n or di + k > want:
                return False
            di += k; si += k
        elif c > 128:
            k = (257 - c) * 4
            if si + 4 > n or di + k > want:
                return False
            di += k; si += 4
        else:
            return False
    return si == n and di == want


def main():
    assets = sys.argv[1] if len(sys.argv) > 1 else \
        "/home/user/PS2Projects/google_drive"
    out_path = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.join(assets, "menu_cache.rle")

    src = open(os.path.join(assets, "menu_cache.rle"), "rb").read()
    print("menu_cache.rle original: %d bytes" % len(src))

    font, widths = load_font(assets)

    # confirma que os 3 primeiros blocos do arquivo real estao bons
    for off, size, raw, name in ((0, MENU_RLE, 2_961_848, "menu"),
                                 (MENU_RLE, FONT_RLE, 294_912, "fonte"),
                                 (MENU_RLE + FONT_RLE, STORY_RLE, 524_288, "story ui")):
        if not decode_check(src[off:off + size], raw):
            raise SystemExit("o bloco %s do arquivo real NAO decodifica; "
                             "melhor nao tocar no arquivo" % name)
        print("  bloco %-9s offset %8d, %7d B -> %8d B  OK (mantido)"
              % (name, off, size, raw))

    # monta o atlas dos 9 titulos com a fonte real
    atlas = bytearray(ST_TITLES_RAW)
    for (off, w, h), name in zip(STORY_TITLES, STORY_NAMES):
        img = render_text(font, widths, name, w, h)
        if len(img) != w * h * 4:
            raise SystemExit("render de %s deu %d bytes" % (name, len(img)))
        atlas[off:off + len(img)] = img
        print("  titulo %-30s %3dx%-3d no offset %7d" % (name, w, h, off))

    blk = rle_encode_exact(bytes(atlas), ST_TITLES_RLE)
    print("bloco 4 regerado: %d B -> %d B" % (len(blk), ST_TITLES_RAW))
    if not decode_check(blk, ST_TITLES_RAW):
        raise SystemExit("o bloco 4 regerado nao decodifica")

    fixed = bytearray(src[:MENU_RLE + FONT_RLE + STORY_RLE]) + blk
    print("menu_cache.rle corrigido: %d bytes (era %d)"
          % (len(fixed), len(src)))

    # validacao final: os 4 blocos, no arquivo novo
    for off, size, raw, name in ((0, MENU_RLE, 2_961_848, "menu"),
                                 (MENU_RLE, FONT_RLE, 294_912, "fonte"),
                                 (MENU_RLE + FONT_RLE, STORY_RLE, 524_288, "story ui"),
                                 (MENU_RLE + FONT_RLE + STORY_RLE, ST_TITLES_RLE,
                                  ST_TITLES_RAW, "story titulos")):
        if not decode_check(bytes(fixed[off:off + size]), raw):
            raise SystemExit("bloco %s quebrou no arquivo final" % name)
        print("  bloco %-14s %8d B -> %8d B  OK" % (name, size, raw))

    with open(out_path, "wb") as f:
        f.write(fixed)
    print("escrito em %s" % out_path)


main()
