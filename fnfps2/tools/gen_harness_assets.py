#!/usr/bin/env python3
"""Gera a raiz de assets que o harness precisa para rodar o jogo inteiro.

O jogo le tudo de mass:/FNFPS2/assets/... . Na vida real esses arquivos estao no
memory card do PS2; no host o harness traduz mass:/ para esta pasta.

Por que sintetizar em vez de copiar: os assets de arte nao estao no repositorio
(so os pacotes .S e os .lz4f de verificacao). Sem eles o jogo para no inicio e
o harness nao exercita quase nada -- exatamente o cenario que nao serve para
achar erro.

O sintetizador produz conteudo VALIDO para cada formato, com as dimensoes
certas, para que o codigo real de leitura/decodificacao/textura corra. Os
pixels sao padroes deterministicos (nada de aleatorio) para que duas rodadas
sejam comparaveis.
"""

import os
import struct
import sys

# ---------------------------------------------------------------- formatos ----
# RLE do jogo: um byte de controle c.
#   c < 128  -> literal: (c+1)*4 bytes copiados literalmente
#   c > 128  -> repeticao: os 4 bytes seguintes repetidos (257-c) vezes
#   c == 128 -> erro no decodificador
# O decodificador exige que o fluxo consuma EXATAMENTE src_bytes e produza
# EXATAMENTE dst_bytes, senao devolve erro. Por isso o gerador resolve as duas
# contas ao mesmo tempo em vez de apenas "comprimir".


def _distribute(total, count, lo=1, hi=128):
    """Divide 'total' em 'count' valores entre lo e hi."""
    if count == 0:
        if total != 0:
            raise ValueError("nada para distribuir")
        return []
    if total < count * lo or total > count * hi:
        raise ValueError(f"impossivel distribuir {total} em {count} partes [{lo},{hi}]")
    base = total // count
    rem = total - base * count
    out = [base + (1 if i < rem else 0) for i in range(count)]
    return out


def make_rle(dst_bytes, src_bytes, seed=0):
    """Monta um fluxo RLE que decodifica exatamente dst_bytes a partir de
    exatamente src_bytes de arquivo."""
    if dst_bytes % 4 or src_bytes < 0:
        raise ValueError("dst_bytes tem de ser multiplo de 4")

    # R tokens de repeticao (maximo, 128 pixels cada) + L tokens literais.
    #   decoded = 512*R + 4*sum(m)          (m = pixels de cada literal)
    #   arquivo =   5*R + 4*sum(m) + L
    #   =>  arquivo - decoded = L - 507*R
    # Resolvemos R por busca: L = 507*R + (src_bytes - dst_bytes)
    chosen = None
    for R in range(0, 5_000_000):
        L = 507 * R + (src_bytes - dst_bytes)
        if L < 1:
            continue
        rem_d = dst_bytes - 512 * R
        if rem_d < 0 or rem_d % 4:
            continue
        sum_m = rem_d // 4
        if sum_m < L or sum_m > 128 * L:
            continue
        chosen = (R, L, sum_m)
        break
    if not chosen:
        raise ValueError(
            f"sem solucao RLE para decoded={dst_bytes} arquivo={src_bytes}")

    R, L, sum_m = chosen
    ms = _distribute(sum_m, L, 1, 128)

    out = bytearray()
    # pixels de repeticao: gradiente estavel, para o atlas nao ser uniforme
    for i in range(R):
        out.append(129)                       # count = 257-129 = 128
        out += bytes(((i * 7) & 0xFF, (i * 13) & 0xFF, (i * 29) & 0xFF, 0x80))
    for i, m in enumerate(ms):
        out.append(m - 1)                     # (c+1)*4 = m*4 bytes
        for j in range(m):
            out += bytes(((i + j * 3) & 0xFF, (i * 5 + j) & 0xFF,
                          (i * 11 + j * 7) & 0xFF, 0x40))
    if len(out) != src_bytes:
        raise ValueError(f"RLE gerou {len(out)} bytes, esperado {src_bytes}")
    return bytes(out)


def rgba_pattern(w, h, seed=0, alpha=0xFF):
    """Textura RGBA deterministica, com linhas e blocos para nao ser plana."""
    out = bytearray(w * h * 4)
    for y in range(h):
        for x in range(w):
            o = (y * w + x) * 4
            out[o + 0] = (x * 3 + y + seed) & 0xFF
            out[o + 1] = (x + y * 5 + seed) & 0xFF
            out[o + 2] = (x * 7 + y * 2 + seed * 3) & 0xFF
            out[o + 3] = alpha if ((x >> 3) + (y >> 3)) % 3 else 0x00
    return bytes(out)


def pcm(n, freq=440, rate=48000):
    """PCM 16bit mono: onda quadrada, para o anel de audio ter dados de verdade."""
    out = bytearray(n)
    for i in range(n // 2):
        v = 0x1000 if (i // (rate // freq // 2)) % 2 else -0x1000
        struct.pack_into("<h", out, i * 2, v)
    return bytes(out)


# ------------------------------------------------------------------ assets ----
MENU_CACHE = 2_961_848
MENU_RLE = 1_288_182
FONT_RLE = 38_342
STORY_RLE = 72_402
STORY_TITLES_RLE = 188_635
PRELOAD = MENU_RLE + FONT_RLE + STORY_RLE + STORY_TITLES_RLE


def build(root):
    a = os.path.join(root, "FNFPS2", "assets")
    os.makedirs(a, exist_ok=True)

    files = {
        # --- preload unico: 4 blocos RLE concatenados, cada um exato ---
        "menu_cache.rle":
            make_rle(MENU_CACHE, MENU_RLE)
            + make_rle(384 * 192 * 4, FONT_RLE)
            + make_rle(512 * 256 * 4, STORY_RLE)
            + make_rle(306_180, STORY_TITLES_RLE),
        "menu_sfx.pcm": pcm(281_088, 220),
        "audio_stems.pcm": pcm(1 << 18, 196),
        "freakyMenu_48000.pcm": pcm(1 << 18, 330),

        # --- texturas cruas RGBA ---
        "font.rgba": rgba_pattern(384, 192, 1),
        "title_alphabet.rgba": rgba_pattern(384, 192, 2),
        "title_prompt_l.rgba": rgba_pattern(512, 192, 3),
        "title_prompt_r.rgba": rgba_pattern(320, 192, 4),
        "title_newgrounds.rgba": rgba_pattern(181, 175, 5),
        "mainstage_tutorial_parallax.rgba": rgba_pattern(320, 224, 6),
        "tutorial_hud_official_320x256_gsalpha.rgba": rgba_pattern(320, 256, 7),

        # --- quadros brutos ---
        "title_logoBumpin.frames": rgba_pattern(320, 240, 8),
        "title_gfDanceTitle.frames": rgba_pattern(256, 235, 9),

        # --- tabela de larguras de glifo ---
        "font.widths": bytes([(i % 24) + 4 for i in range(96)]),
    }

    for name, data in files.items():
        p = os.path.join(a, name)
        with open(p, "wb") as f:
            f.write(data)

    total = sum(len(v) for v in files.values())
    print(f"assets sinteticos: {len(files)} arquivos, {total:,} bytes, em {a}")
    for name in ("menu_cache.rle", "font.rgba", "title_gfDanceTitle.frames"):
        print(f"  {name:34s} {len(files[name]):>10,} bytes")
    return a


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "build/harness_assets"
    build(root)
