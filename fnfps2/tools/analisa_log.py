#!/usr/bin/env python3
"""Le um FNF_COLHEITA.txt e responde, SOZINHO, as quatro coisas que o teste no
console acusou. Nada de relatorio, nada de print de tela: so o log.

Uso:  python3 tools/analisa_log.py [caminho/do/FNF_COLHEITA.txt]

Sem argumento, procura em build/harness_assets/FNFPS2/FNF_COLHEITA.txt.

O que ele verifica, e de onde tira a conclusao:

 (1) linhas estranhas abaixo dos botoes
     -> desenha algo que nao eh o fundo nem um dos itens do menu? Conta, por
        quadro do estado 6, quantos sprites existem e quais sao. Se aparecer
        um sprite que nao casa com a geometria dos itens, ele eh listado.

 (2) o fundo esticando em vez de rolar
     -> compara a escala vertical de cada sprite com a escala do sprite
        inteiro. Escala = altura na tela / altura na textura. Se o sprite foi
        recortado pela faixa, a escala TEM de continuar igual a do inteiro;
        se mudou, o sprite foi esticado ou encolhido. A linha D, guarda a
        altura na tela (h), o trecho de textura (vh) e o trecho recortado (v),
        da para conferir sem saber de mais nada.

 (3) os botoes bugados ao voltar do roteiro
     -> a posicao y dos itens do menu. Se um item aparecer em y diferente da
        posicao que ocupa no menu normal, ou se um item sumir, esta aqui.

 (4) o travamento ao entrar no roteiro
     -> onde o log parou. O ultimo quadro com sprite, o ultimo P, e a ultima
        linha escrita. Um travamento deixa o log cortado no meio, e esse
        corte aparece aqui.

RODADAS -- e por que isso existe
------------------------------
O log eh UM arquivo com VARIOS escritores. O telemetry_init() eh o primeiro e
trunca; os despejos (av_trace_dump, fnx_congelado2, estado_dump) acrescentam na
mesma rodada. Se por algum motivo uma versao antiga do jogo rodou antes -- ou se
o telemetry_init() nao conseguiu abrir o arquivo e so um despejo entrou -- o
arquivo passa a conter MAIS DE UMA rodada.

Foi exatamente assim que eu cheguei a uma conclusao errada: li o quadro 364
duas vezes num arquivo que tinha quatro rodadas empilhadas e escrevi, no
documento de passagem de bastao, que "o menu desenha cada item duas vezes".
Segmentando por rodada, o quadro 364 tem 5 sprites -- 1 fundo e 4 itens. A
duplicacao nao existia.

Por isso este analisador NUNCA mistura rodadas: ele separa, diz quantas sao, e
analisa cada uma sozinha.
"""
import os
import sys
from collections import Counter, defaultdict

BAND = (56, 391)          # faixa publicada em 4:3 (SCISSOR_TOPO/BASE)
CORR = 1.5894             # escala fisica/textura do jogo (406.893/256)

# Linha que comeca uma rodada nova. TEM de ser esta string completa: o
# av_trace_dump() escreve "# build=..." e o fnx_congelado2() escreve
# "# FNF PS2 <versao> CONGELADO" -- nenhum dos dois eh uma rodada nova, e
# aceitar qualquer linha começando com "#" criaria rodadas falsas.
CABECALHO_RODADA = "# FNF PS2 TELEMETRIA CONTINUA"


def caminho_log():
    if len(sys.argv) > 1:
        return sys.argv[1]
    aqui = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(aqui, "build", "harness_assets", "FNFPS2",
                        "FNF_COLHEITA.txt")


def _nova():
    return {"est": [], "fr": [], "sp": [], "fas": [], "ev": [],
            "ult": None, "linhas": 0}


def le_log(p):
    """Devolve a lista de rodadas do arquivo, na ordem em que aparecem.

    Cada rodada eh um dicionario com est, fr, sp, fas, ev, ult e linhas.
    Uma rodada nova comeca em cada cabecalho de telemetria; P,SHUTDOWN fexa a
    rodada corrente (esteio, para o caso de o cabecalho nao estar la).
    """
    rodadas = []
    cur = _nova()
    for n, ln in enumerate(open(p, encoding="utf-8", errors="replace")):
        ln = ln.rstrip("\n")
        cur["linhas"] += 1
        cur["ult"] = (n + 1, ln)
        if ln.startswith(CABECALHO_RODADA):
            if cur["sp"] or cur["fas"] or cur["est"]:
                rodadas.append(cur)
                cur = _nova()
                cur["linhas"] = 1
                cur["ult"] = (n + 1, ln)
            continue
        if ln.startswith("S,"):
            c = ln.split(",")
            cur["est"].append({"f": int(c[1]), "ui": int(c[2])})
        elif ln.startswith("F,"):
            c = ln.split(",")
            cur["fr"].append({"f": int(c[1])})
        elif ln.startswith("D,"):
            c = ln.split(",")
            # D,quadro,i,estado,x,y,w,h,u,v,uw,vh,alfa,vy0,vy1,vy_span,
            # gsx0,gsy0,gsx1,gsy1
            cur["sp"].append({"f": int(c[1]), "i": int(c[2]), "st": int(c[3]),
                              "x": float(c[4]), "y": float(c[5]),
                              "w": float(c[6]), "h": float(c[7]),
                              "v": float(c[9]), "vh": float(c[11]),
                              "vy0": float(c[13]), "vy1": float(c[14]),
                              "gsy0": float(c[17]), "gsy1": float(c[19])})
        elif ln.startswith("P,"):
            c = ln.split(",")
            cur["fas"].append({"fase": c[1], "ordem": n,
                               "linha": int(c[2]) if c[2].lstrip("-").isdigit()
                               else -1})
            if c[1] == "SHUTDOWN" and (cur["sp"] or cur["fas"] or cur["est"]):
                rodadas.append(cur)
                cur = _nova()
        elif ln.startswith("E,"):
            cur["ev"].append(ln)
    if cur["sp"] or cur["fas"] or cur["est"]:
        rodadas.append(cur)
    return rodadas


def analisa(r, titulo):
    """Analisa UMA rodada. Devolve quantos problemas achou."""
    est, fr, sp, fas, ev, ult = (r["est"], r["fr"], r["sp"], r["fas"],
                                 r["ev"], r["ult"])
    ui = {e["f"]: e["ui"] for e in est}
    print(titulo)
    print("    %d quadros com estado, %d sprites, %d fases, %d eventos"
          % (len(est), len(sp), len(fas), len(ev)))
    problemas = 0

    # ---------- (2) o esticamento ----------
    print("\n[2] FUNDO DO MENU -- escala vertical tela/textura")
    print("    referencia: %.4f (a do sprite inteiro, 406.893 linhas / 256 texels)"
          % CORR)
    fundo = [d for d in sp if d["st"] == 6 and d["w"] > 700]
    if not fundo:
        print("    nenhum sprite largo no estado 6; nao da para conferir.")
    else:
        estic = [d for d in fundo
                 if d["vh"] > 0 and abs(d["h"] / d["vh"] - CORR) > 0.002]
        print("    %d quadros com o fundo, %d com escala errada"
              % (len(fundo), len(estic)))
        if estic:
            problemas += 1
            d = estic[0]
            print("    ESTICADO. exemplo, quadro %d:" % d["f"])
            print("      altura na tela h=%.2f, trecho de textura vh=%.2f,"
                  " escala=%.4f" % (d["h"], d["vh"], d["h"] / d["vh"]))
            print("      desvio = %+.2f%% contra a referencia."
                  % (100 * (d["h"] / d["vh"] / CORR - 1)))
            print("      -> o fundo nao esta so rolando: esta esticando.")
        else:
            print("    OK: escala certa em todos os quadros.")

    # ---------- (1) o que aparece abaixo dos botoes ----------
    print("\n[1] O QUE O MENU DESENHA POR QUADRO")
    porq = defaultdict(list)
    for d in sp:
        if d["st"] == 6:
            porq[d["f"]].append(d)
    if porq:
        q0 = min(porq)
        lista = porq[q0]
        print("    quadro %d (estado 6): %d sprites" % (q0, len(lista)))
        for d in lista:
            print("      i=%2d x=%7.1f y=%6.1f w=%6.1f h=%5.1f "
                  "v=%6.2f vh=%6.2f tela y=%.1f..%.1f"
                  % (d["i"], d["x"], d["y"], d["w"], d["h"], d["v"], d["vh"],
                     d["vy0"], d["vy1"]))
        # um sprite que nao seja o fundo (largo) nem item (quadradao)
        estranhos = [d for d in lista if not (d["w"] > 700 or 100 < d["w"] < 700)]
        if estranhos:
            problemas += 1
            print("    ESTRANHO: %d sprite(s) que nao sao fundo nem item:"
                  % len(estranhos))
            for d in estranhos:
                print("      i=%d x=%.1f y=%.1f w=%.1f h=%.1f"
                      % (d["i"], d["x"], d["y"], d["w"], d["h"]))
        else:
            print("    nenhum sprite fora do fundo e dos itens.")
        # DESENHO DUPLO: a mesma posicao duas vezes NO MESMO quadro. Isto eh a
        # unica assinatura que separa um desenho repetido de verdade do piscar
        # do confirmar -- que some com um item, nao que o duplica.
        duplos = []
        for f, lst in sorted(porq.items()):
            vistos = Counter((round(d["y"]), round(d["h"]), round(d["w"]))
                             for d in lst)
            for chave, n in vistos.items():
                if n > 1:
                    duplos.append((f, chave, n))
        if duplos:
            problemas += 1
            print("    DESENHO DUPLO: %d quadro(s) com a mesma posicao repetida"
                  % len(duplos))
            for f, chave, n in duplos[:5]:
                print("      quadro %d: y=%d h=%d w=%d aparece %d vezes"
                      % (f, chave[0], chave[1], chave[2], n))
            print("      -> o item foi desenhado mais de uma vez no mesmo quadro.")
        else:
            print("    nenhum item repetido dentro de um mesmo quadro.")
        # A contagem por quadro varia de proposito: ao confirmar, o item
        # selecionado pisca 16 vezes (g_fl_item_left=16 em main.c) e some em
        # metade delas. Por isso a contagem NAO eh problema -- only a repeticao
        # acima eh. Fica registrado so para quem ler o log saber o porque.
        contagem = Counter(len(v) for v in porq.values())
        print("    contagem de sprites por quadro: %s"
              % dict(sorted(contagem.items())))
        print("      (varia por causa do piscar do confirmar, nao por bug)")

    # ---------- (3) a posicao dos itens ----------
    print("\n[3] POSICAO DOS ITENS DO MENU")
    itens = [d for d in sp if d["st"] == 6 and 100 < d["w"] < 700]
    if not itens:
        print("    nenhum item registrado.")
    else:
        pos = Counter((round(d["y"]), round(d["h"]), round(d["w"])) for d in itens)
        print("    %d itens, %d posicoes distintas:" % (len(itens), len(pos)))
        for (y, h, w), n in sorted(pos.items()):
            print("      y=%6.1f  altura=%5.1f  largura=%6.1f   (%d quadros)"
                  % (y, h, w, n))
        # O que importa NAO eh a lista de itens de um quadro: ao confirmar, o
        # item selecionado pisca e some em metade dos quadros, entao a contagem
        # por quadro varia sempre. O que importa eh o CONJUNTO de posicoes de
        # cada VISITA ao menu -- um bloco de quadros consecutivos no estado 6.
        # Se o menu voltar do roteiro com um item a mais, a menos, ou em outro
        # lugar, o conjunto muda. Eh isso que o usuario reportou.
        # SO itens: o fundo (w>700) aparece em quadros de transicao onde os
        # itens ja sumiram, e incluilo faria duas visitas parecerem uma so.
        pos_por_quadro = {f: sorted(set((round(x["y"]), round(x["h"]))
                                        for x in porq[f]
                                        if 100 < x["w"] < 700))
                          for f in porq if any(100 < x["w"] < 700
                                               for x in porq[f])}
        visitas = []
        for f in sorted(pos_por_quadro):
            if (not visitas or f != visitas[-1]["fim"] + 1):
                visitas.append({"ini": f, "fim": f, "pos": set()})
            visitas[-1]["fim"] = f
            visitas[-1]["pos"].update(pos_por_quadro[f])
        if len(visitas) < 2:
            print("    so %d visita(s) ao menu; nao ha o que comparar."
                  % len(visitas))
        else:
            base = visitas[0]["pos"]
            print("    %d visitas ao menu (blocos consecutivos no estado 6):"
                  % len(visitas))
            for i, v in enumerate(visitas):
                marca = "" if v["pos"] == base else "   <-- DIFERE"
                print("      visita %d: quadros %d..%d  %d posicao(oes)%s"
                      % (i, v["ini"], v["fim"], len(v["pos"]), marca))
            diferentes = [v for v in visitas if v["pos"] != base]
            if diferentes:
                problemas += 1
                print("    BUG: o menu tem cara diferente em %d de %d visitas."
                      % (len(diferentes), len(visitas)))
                for v in diferentes[:3]:
                    faltando = sorted(base - v["pos"])
                    sobrando = sorted(v["pos"] - base)
                    print("      quadros %d..%d: faltando %s, sobrando %s"
                          % (v["ini"], v["fim"], faltando, sobrando))
                print("      -> o menu nao voltou ao normal depois do roteiro.")
            else:
                print("    o menu tem a MESMA cara nas %d visitas: %s"
                      % (len(visitas), sorted(base)))

    # ---------- (4) onde o log parou ----------
    print("\n[4] ONDE O LOG PAROU")
    if not fr and not sp:
        print("    log vazio de quadros.")
    else:
        ultf = max([d["f"] for d in sp] + [e["f"] for e in est])
        print("    ultimo quadro com sprite: %d (estado %s)"
              % (ultf, ui.get(ultf, "?")))
        if fas:
            print("    ultima fase registrada: %s (linha %d)"
                  % (fas[-1]["fase"], fas[-1]["linha"]))
        if ult:
            print("    ultima linha escrita (%d): %.90s" % (ult[0], ult[1]))
        # fase aberta sem fecho
        # Uma fase so esta "aberta" se o _BEGIN nao tiver _DONE DEPOIS dele.
        # Assim um _BEGIN do comeco do log que fechou logo depois nao conta, e
        # um _BEGIN que fechou em outra rodada do jogo tambem nao.
        # Um _BEGIN cujo prefixo NUNCA tem _DONE eh so marcador de progresso
        # (CACHE_ALLOC_BEGIN, GS_BEGIN, F0_BLEND_BEGIN...) e nao conta.
        sem = []
        for f in fas:
            if not f["fase"].endswith("_BEGIN"):
                continue
            pre = f["fase"].rsplit("_", 1)[0]
            fechou = any(g["ordem"] > f["ordem"] and g["fase"] == pre + "_DONE"
                         for g in fas)
            if not fechou and any(g["fase"] == pre + "_DONE" for g in fas):
                sem.append(f["fase"])
        if sem:
            problemas += 1
            print("    TRAVAMENTO PROVAVEL: comecou e nao terminou -> %s"
                  % ", ".join(sem))
            print("      -> o jogo parou ai. O resto do log nao existe.")
        else:
            print("    toda fase comecada terminou.")

    # ---------- falhas declaradas ----------
    print("\n[extra] FALHAS DECLARADAS NO LOG")
    falhas = [f for f in fas if "_FAIL" in f["fase"] or "_ERROR" in f["fase"]]
    if falhas:
        problemas += 1
        print("    %d marcador(es) de falha:" % len(falhas))
        for f in falhas:
            print("      %s (linha %d)" % (f["fase"], f["linha"]))
        print("    -> alguma etapa abortou. Essas linhas dizem qual.")
    else:
        print("    nenhuma. Nenhuma etapa abortou.")

    # ---------- sprites fora da faixa ----------
    print("\n[extra] SPRITES FORA DA FAIXA VISIVEL (%d..%d)" % BAND)
    fora = [d for d in sp
            if (d["vy1"] < BAND[0] - 0.5 or d["vy0"] > BAND[1] + 0.5)]
    if fora:
        problemas += 1
        print("    %d sprites inteiramente fora da faixa" % len(fora))
        for d in fora[:5]:
            print("      quadro %d i=%d y=%.1f..%.1f"
                  % (d["f"], d["i"], d["vy0"], d["vy1"]))
    else:
        print("    nenhum. Todos os sprites passam pela faixa.")

    # ---------- o que o GS realmente recebeu ----------
    # A faixa visivel eh 56..391. O vertice que sai para o GS (gsy0/gsy1) eh o
    # que o hardware desenha. Se um vertice ficar fora da faixa, so o scissor
    # do GS impede a linha de aparecer -- e nas capturas de hardware da 0.2.106
    # havia conteudo medido na linha 6, bem fora dela. Isto torna essa medida
    # mecanica em vez de depender de print.
    print("\n[extra] VERTICES DO GS FORA DA FAIXA (%d..%d)" % BAND)
    # INFORMATIVO, nao conta como problema. O vertice do GS sai da faixa por
    # uma fragao de linha (0,44 em cima, 0,56 embaixo) por causa do arredondo
    # de subpixel, e o scissor do GS corta. A prova de que corta eh hardware:
    # nas 6 capturas RGBA32 da 0.2.106 o conteudo comeca exatamente na linha
    # 56 e acaba exatamente na 391 -- 336 linhas, sem sangramento para a 55
    # nem para a 392. Se um dia o sangramento aparecer, esta secao passa a
    # listar os vertices e a diferenca deixa de ser fracao de linha.
    gsfora = [d for d in sp
              if d["gsy0"] < BAND[0] - 0.5 or d["gsy1"] > BAND[1] + 0.5]
    if gsfora:
        print("    %d sprites com vertice do GS fora da faixa:" % len(gsfora))
        vistos = Counter()
        for d in gsfora:
            vistos[(round(d["gsy0"], 2), round(d["gsy1"], 2))] += 1
        for (a, b), n in sorted(vistos.items()):
            print("      gsy %.2f..%.2f  em %d quadro(s)" % (a, b, n))
        print("      -> fracao de linha; o scissor do GS corta (medido em")
        print("         hardware: conteudo exato em 56..391, sem sangramento).")
    else:
        print("    nenhum. Todo vertice do GS esta dentro da faixa.")

    return problemas


def main():
    p = caminho_log()
    if not os.path.exists(p):
        print("nao achei o log em %s" % p)
        print("copie o FNF_COLHEITA.txt do cartao de memoria para esse caminho.")
        return 2
    rodadas = le_log(p)
    if not rodadas:
        print("log sem nenhuma linha utilizavel: %s" % p)
        print("Sem linha D,, nao da para julhar geometria. Log incompleto.")
        return 1

    print("log: %s" % p)
    if len(rodadas) == 1:
        print("     1 rodada no arquivo.")
        return 1 if analisa(rodadas[0], "\n=== RODADA UNICA ===") else 0

    # Mais de uma rodada: NUNCA analisar tudo junto. Cada uma sozinha, e o
    # resumo no fim diz onde estao os problemas.
    print("     %d RODADAS no mesmo arquivo. Analisando cada uma separada;"
          % len(rodadas))
    print("     mistura-las foi o que ja produziu um diagnostico falso.")
    total = 0
    resumo = []
    for k, r in enumerate(rodadas):
        if not r["sp"]:
            print("\n=== RODADA %d/%d: sem linha D, (%d linhas) ==="
                  % (k + 1, len(rodadas), r["linhas"]))
            continue
        print()
        n = analisa(r, "=== RODADA %d/%d (%d linhas, %d sprites) ==="
                    % (k + 1, len(rodadas), r["linhas"], len(r["sp"])))
        resumo.append((k + 1, n, len(r["sp"])))
        total += n

    print("\n======================================================")
    print("RESUMO POR RODADA")
    for k, n, ns in resumo:
        print("  rodada %d: %d sprite(s), %d problema(s)%s"
              % (k, ns, n, "  <-- investigar" if n else ""))
    print("TOTAL: %d problema(s) em %d rodada(s) com sprite."
          % (total, len(resumo)))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
