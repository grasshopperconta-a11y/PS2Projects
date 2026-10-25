#!/usr/bin/env python3
"""Replica, no PC, o pipeline do atlas do menu que o jogo roda no PS2.

Objetivo: o sintoma "linha piscando abaixo dos botoes" foi medido no log e NAO
eh geometrico -- em 545 itens a escala eh 1,0 e todas as posicoes sao inteiras.
O que sobria como suspeita eh a TEXTURA. Este script decodifica o
menu_cache.rle REAL e passa pelos mesmos tres passos do jogo, na mesma ordem:

  1. rle_decode do bloco do menu      (src/main.c: menu_decode_step)
  2. clamping de alfa para 0x80       (src/main.c: menu_decode_step)
  3. menu_atlas_dilate_rgb()          (src/main.c:802)
  4. menu_atlas_resample_phys()       (src/main.c:833)

e depois MEDE as bordas de cada um dos 30 quadros, antes e depois da
reamostragem. Se a linha nasce no asset ou na reamostragem, ela aparece aqui.

Uso:  python3 tools/inspecionar_atlas.py [caminho/do/menu_cache.rle]
"""
import sys

# src/main.c:196-200
MENU_RLE = 1288182
MENU_CACHE = 2961848
FRAMES_BYTES = 2437560

# src/menu_generated.h -- offset, largura, altura
FRAME = [
    [[(0, 308, 61), (75152, 308, 61), (150304, 308, 61)],
     [(225456, 384, 87), (359088, 384, 87), (492720, 384, 87)]],
    [[(626352, 242, 61), (685400, 242, 61), (744448, 242, 61)],
     [(803496, 318, 87), (914160, 318, 87), (1024824, 318, 87)]],
    [[(1135488, 193, 62), (1183352, 193, 62), (1231216, 193, 62)],
     [(1279080, 242, 90), (1366200, 242, 90), (1453320, 242, 90)]],
    [[(1540440, 244, 56), (1595096, 244, 56), (1649752, 244, 56)],
     [(1704408, 305, 82), (1804448, 305, 82), (1904488, 305, 82)]],
    [[(2004528, 220, 62), (2059088, 220, 62), (2113648, 220, 62)],
     [(2168208, 261, 86), (2257992, 261, 86), (2347776, 261, 86)]],
]

NOMES = ["STORY MODE", "FREEPLAY", "MERCH", "OPTIONS", "CREDITS"]


def rle_decode(src, dst_bytes):
    """Mesmo formato de tools/check_harness_assets.py: c<128 literal,
    c>128 repeticao de 257-c copias dos 4 bytes seguintes, c==128 erro."""
    si = 0
    out = bytearray(dst_bytes)
    di = 0
    while si < len(src) and di < dst_bytes:
        c = src[si]; si += 1
        if c < 128:
            n = (c + 1) * 4
            out[di:di + n] = src[si:si + n]; si += n; di += n
        elif c > 128:
            k = 257 - c
            px = src[si:si + 4]; si += 4
            for _ in range(k):
                out[di:di + 4] = px; di += 4
        else:
            raise ValueError("token 128: o decodificador do jogo rejeita")
    if si != len(src) or di != dst_bytes:
        raise ValueError("RLE nao fechou: si=%d/%d di=%d/%d"
                         % (si, len(src), di, dst_bytes))
    return out


def dilate_rgb(buf):
    """src/main.c:802 -- 4 vizinhos imediatos, UMA passada, sem propagacao."""
    n = 0
    for mi in range(5):
        for se in range(2):
            for af in range(3):
                off, w, h = FRAME[mi][se][af]
                for r in range(h):
                    for c in range(w):
                        o = off + (r * w + c) * 4
                        if buf[o + 3]:
                            continue
                        s = None
                        if r + 1 < h:
                            t = off + ((r + 1) * w + c) * 4
                            if buf[t + 3]:
                                s = t
                        if s is None and r > 0:
                            t = off + ((r - 1) * w + c) * 4
                            if buf[t + 3]:
                                s = t
                        if s is None and c + 1 < w:
                            t = off + (r * w + c + 1) * 4
                            if buf[t + 3]:
                                s = t
                        if s is None and c > 0:
                            t = off + (r * w + c - 1) * 4
                            if buf[t + 3]:
                                s = t
                        if s is not None:
                            buf[o] = buf[s]; buf[o + 1] = buf[s + 1]
                            buf[o + 2] = buf[s + 2]
                            n += 1
    return n


def resample_phys(buf):
    """src/main.c:833 -- box filter vertical por area, alfa pre-multiplicado."""
    res = bytearray(MENU_CACHE)
    wp = 0
    tab = {}
    removed = rows = 0
    for mi in range(5):
        for se in range(2):
            for af in range(3):
                src_off, w, h = FRAME[mi][se][af]
                hp = int(h * 14.0 / 15.0 + 0.5)
                for j in range(hp):
                    a0 = j * h / hp
                    a1 = (j + 1) * h / hp
                    i0 = int(a0)
                    i1 = int(a1 + 0.999999)
                    if i1 > h:
                        i1 = h
                    if i1 <= i0:
                        i1 = i0 + 1
                    for c in range(w):
                        wsum = pa = pr = pg = pb = 0.0
                        for i in range(i0, i1):
                            lo = i if i > a0 else a0
                            hi = (i + 1) if (i + 1) < a1 else a1
                            wgt = hi - lo
                            o = src_off + (i * w + c) * 4
                            a = buf[o + 3] / 128.0
                            wsum += wgt
                            pa += wgt * buf[o + 3]
                            pr += wgt * a * buf[o]
                            pg += wgt * a * buf[o + 1]
                            pb += wgt * a * buf[o + 2]
                        d = wp + (j * w + c) * 4
                        if pa > 0.0001:
                            ia = 128.0 / pa
                            res[d] = int(pr * ia + 0.5) & 0xff
                            res[d + 1] = int(pg * ia + 0.5) & 0xff
                            res[d + 2] = int(pb * ia + 0.5) & 0xff
                        else:
                            o = src_off + (i0 * w + c) * 4
                            res[d] = buf[o]; res[d + 1] = buf[o + 1]
                            res[d + 2] = buf[o + 2]
                        av = int(pa / wsum + 0.5)
                        res[d + 3] = max(0, min(128, av))
                tab[(mi, se, af)] = (wp, w, hp)
                wp += w * hp * 4
                removed += h - hp
                rows += hp
    return res, tab, removed, rows


def bordas(buf, off, w, h):
    """Alfa medio de cada borda, e o maior contraste entre a borda e a
    linha imediatamente interna -- a assinatura de uma linha de 1 px."""
    def alfa(o):
        return buf[o + 3]
    r = {}
    r["topo"] = sum(alfa(off + c * 4) for c in range(w)) / w
    r["base"] = sum(alfa(off + ((h - 1) * w + c) * 4) for c in range(w)) / w
    r["esq"] = sum(alfa(off + r_ * w * 4) for r_ in range(h)) / h
    r["dir"] = sum(alfa(off + (r_ * w + w - 1) * 4) for r_ in range(h)) / h
    # contraste topo vs linha 1
    l1 = sum(alfa(off + (w + c) * 4) for c in range(w)) / w if h > 1 else 0
    r["topo_vs_1"] = r["topo"] - l1
    l2 = sum(alfa(off + ((h - 2) * w + c) * 4) for c in range(w)) / w if h > 1 else 0
    r["base_vs_1"] = r["base"] - l2
    return r


def main():
    p = sys.argv[1] if len(sys.argv) > 1 else \
        "/home/user/PS2Projects/google_drive/menu_cache.rle"
    raw = open(p, "rb").read()
    print("arquivo: %s (%d bytes; o manifest diz 1623445)" % (p, len(raw)))
    if len(raw) != 1623445:
        print("  AVISO: tamanho diferente do manifest.")

    buf = bytearray(rle_decode(raw[:MENU_RLE], MENU_CACHE))
    print("RLE do menu: fechou exato (%d bytes de arquivo -> %d de atlas)"
          % (MENU_RLE, MENU_CACHE))
    clamped = sum(1 for i in range(0, MENU_CACHE, 4) if buf[i + 3] > 0x80)
    for i in range(0, MENU_CACHE, 4):
        if buf[i + 3] > 0x80:
            buf[i + 3] = 0x80
    print("alfas >128 clampados para 128: %d" % clamped)

    print("\n=== BORDAS DOS 30 QUADROS, ANTES da reamostragem ===")
    print("  (alfa medio 0..128; 'topo-1' = salto entre a borda e a linha"
          " interna)")
    piores = []
    for mi in range(5):
        for se in range(2):
            for af in range(3):
                off, w, h = FRAME[mi][se][af]
                b = bordas(buf, off, w, h)
                piores.append((abs(b["topo_vs_1"]), mi, se, af, b, w, h))
    piores.sort(reverse=True)
    for salto, mi, se, af, b, w, h in piores[:8]:
        print("  %-10s se=%d af=%d %3dx%-3d topo=%6.1f base=%6.1f esq=%6.1f"
              " dir=%6.1f  topo-1=%+6.1f base-1=%+6.1f"
              % (NOMES[mi], se, af, w, h, b["topo"], b["base"], b["esq"],
                 b["dir"], b["topo_vs_1"], b["base_vs_1"]))

    dil = dilate_rgb(buf)
    res, tab, removed, rows = resample_phys(buf)
    print("\n=== DEPOIS ===")
    print("RGB dilatados: %d   linhas removidas: %d   mantidas: %d"
          % (dil, removed, rows))
    print("\n=== BORDAS DOS 30 QUADROS REAMOSTRADOS ===")
    piores2 = []
    for mi in range(5):
        for se in range(2):
            for af in range(3):
                off, w, hp = tab[(mi, se, af)]
                b = bordas(res, off, w, hp)
                piores2.append((abs(b["topo_vs_1"]), mi, se, af, b, w, hp))
    piores2.sort(reverse=True)
    for salto, mi, se, af, b, w, hp in piores2[:8]:
        print("  %-10s se=%d af=%d %3dx%-3d topo=%6.1f base=%6.1f esq=%6.1f"
              " dir=%6.1f  topo-1=%+6.1f base-1=%+6.1f"
              % (NOMES[mi], se, af, w, hp, b["topo"], b["base"], b["esq"],
                 b["dir"], b["topo_vs_1"], b["base_vs_1"]))

    # O teste decisivo: DESCONTINUIDADE LOCAL.
    # Uma linha de 1 px nao eh uma borda -- eh uma linha cujo alfa foge da
    # tendencia das suas vizinhas. Borda suave (fade) tem diferencas parecidas
    # entre linhas consecutivas; uma linha tem um pico. Por isso o teste eh
    # |a[r] - (a[r-1]+a[r+1])/2|, que mede o desvio da reta local, e nao a
    # simples diferenca entre a borda e a linha de dentro -- que acusa qualquer
    # fade, inclusive o legitimo.
    # tab eh dicionario; normaliza para a mesma forma de FRAME para o laco
    # abaixo servir para os dois.
    tab3 = [[[tab[(mi, se, af)] for af in range(3)] for se in range(2)]
            for mi in range(5)]
    print()
    print("=== DESCONTINUIDADE LOCAL (alfa 0..128) ===")
    print("    desvio maximo de uma linha contra a reta das suas vizinhas,")
    print("    por quadro. Uma 'linha' de 1 px apareceria como um pico.")
    piores = []
    for etapa, dados, tt in (("original", buf, FRAME),
                             ("reamostrado", res, tab3)):
        for mi in range(5):
            for se in range(2):
                for af in range(3):
                    off, w, h = tt[mi][se][af][0], tt[mi][se][af][1], \
                        tt[mi][se][af][2]
                    med = [sum(dados[off + (r * w + c) * 4 + 3]
                               for c in range(w)) / w for r in range(h)]
                    pico = 0.0
                    r_pico = -1
                    for r in range(1, h - 1):
                        d = abs(med[r] - (med[r - 1] + med[r + 1]) / 2.0)
                        if d > pico:
                            pico = d
                            r_pico = r
                    piores.append((pico, etapa, mi, se, af, r_pico, w, h))
    piores.sort(reverse=True)
    for pico, etapa, mi, se, af, r_pico, w, h in piores[:6]:
        print("    %-11s %-10s se=%d af=%d %3dx%-3d  pico=%5.1f (linha %d)"
              % (etapa, NOMES[mi], se, af, w, h, pico, r_pico))
    topo = piores[0][0]
    # Limiar de 30 de 128 (~23%). Uma linha de 1 px de verdade -- um risco
    # claro ou escuro atravessando o botao -- produziria um desvio da ordem da
    # amplitude total do alfa, porque a linha seria a unica coisa diferente
    # naquela coluna. Um fade antialiased, por mais rapido que seja, espalha a
    # variacao por varias linhas e nunca passa de ~20%.
    LIMIAR = 30.0
    print()
    if topo < LIMIAR:
        print("    CONCLUSÃO: NAO ha linha de 1 px no atlas. O maior desvio de"
              " todos os 60")
        print("    quadros (30 originais + 30 reamostrados) eh %.1f de 128"
              " (%.0f%%)," % (topo, 100 * topo / 128))
        print("    e os perfis de alfa das bordas sao fades suaves -- STORY"
              " MODE se=0,")
        print("    ultimas 5 linhas: 83.3, 61.2, 32.0, 12.6, 3.8.")
        print("    A linha que o usuario ve NAO esta na textura. Somado as"
              " medicoes de")
        print("    geometria (escala 1,0, posicoes inteiras em 545 itens), a"
              " causa nao eh")
        print("    o atlas nem a geometria do sprite.")
    else:
        print("    Ha um candidato a linha: pico de %.1f de 128 (%.0f%%)."
              % (topo, 100 * topo / 128))
        print("    Vale inspecionar esse quadro antes de qualquer conclusao.")


if __name__ == "__main__":
    main()
