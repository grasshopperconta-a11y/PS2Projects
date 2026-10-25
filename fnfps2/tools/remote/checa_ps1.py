#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador estrutural de PowerShell.

NAO substitui o PowerShell de verdade -- nao tenho um aqui. Mas pega a classe
de erro que jah me mordeu: o cliente foi entregue com um erro de sintaxe e so
descobrimos quando o usuario rodou.

O erro era este (fnf-remote-client.ps1, linhas 176-177):

    $txt = ("RECUSADO ... area protegida "
            + "(System32 / Windows). ..." -f $atingiu)

O parser do PowerShell nao aceita a quebra de linha depois de uma string
completa dentro de parenteses: ele trata a quebra como fim de instrucao e
reclama que falta o ')'. Erro: MissingEndParenthesisInExpression.

Este verificador olha tres coisas:

  1. string aberta e nao fechada na mesma linha
     (em PowerShell string comum nao atravessa linha; so here-string @"..@)
  2. parenteses/chaves/colchetes dessincronizados
  3. linha terminando em string completa seguida de linha comecando com
     operador binario -- o padrao exato que quebrou

Uso:
    python3 checa_ps1.py <arquivo.ps1> [outro.ps1 ...]
"""

import sys

ABRE = {"(": ")", "{": "}", "[": "]"}
FECHA = {")": "(", "}": "{", "]": "["}
OPERADORES = ("+", "-", "*", "/", "%", "-and", "-or", "-xor", "-not",
              "-eq", "-ne", "-lt", "-gt", "-le", "-ge", "-like", "-notlike",
              "-match", "-notmatch", "-f", "-join", "-split", "-replace",
              "-is", "-as", "-in", "-contains")


class Estado(object):
    """Estado do scanner, que precisa sobreviver de linha em linha por causa
    dos comentarios de bloco <# ... #>."""

    def __init__(self):
        self.em_bloco = False      # dentro de <# ... #>
        self.em_here = None        # '"' ou "'" se dentro de here-string
        self.pilha = []            # (), {}, [] abertos


def escanear(linha, est):
    """Atualiza est com o que achar na linha. Devolve lista de problemas."""
    probs = []
    i, n = 0, len(linha)
    in_dq = in_sq = False
    ultimo_util = None             # (char) do ultimo char que nao eh espaco

    while i < n:
        c = linha[i]

        # ---- comentario de bloco <# ... #>
        if est.em_bloco:
            if c == "#" and i + 1 < n and linha[i + 1] == ">":
                est.em_bloco = False
                i += 2
                continue
            i += 1
            continue

        # ---- here-string @" ... "@  (multilinha, nao contamos nada dentro)
        if est.em_here:
            if est.em_here == '"':
                if c == '"' and i > 0 and linha[i - 1] == "@":
                    est.em_here = None
                    i += 1
                    continue
            else:
                if c == "'" and i > 0 and linha[i - 1] == "@":
                    est.em_here = None
                    i += 1
                    continue
            i += 1
            continue

        # ---- escape de PowerShell
        if c == "`" and i + 1 < n:
            i += 2
            continue

        # ---- string comum
        if in_dq:
            if c == '"':
                if i + 1 < n and linha[i + 1] == '"':
                    i += 2
                    continue
                in_dq = False
                ultimo_util = '"'
            i += 1
            continue
        if in_sq:
            if c == "'":
                if i + 1 < n and linha[i + 1] == "'":
                    i += 2
                    continue
                in_sq = False
                ultimo_util = "'"
            i += 1
            continue

        # ---- inicio de here-string
        if c == "@" and i + 1 < n and linha[i + 1] in "\"'":
            est.em_here = linha[i + 1]
            i += 2
            continue

        # ---- inicio de comentario de bloco
        if c == "<" and i + 1 < n and linha[i + 1] == "#":
            est.em_bloco = True
            i += 2
            continue

        # ---- comentario de linha
        if c == "#":
            break

        if c == '"':
            in_dq = True
            i += 1
            continue
        if c == "'":
            in_sq = True
            i += 1
            continue

        if c in ABRE:
            est.pilha.append(c)
        elif c in FECHA:
            if not est.pilha or est.pilha[-1] != FECHA[c]:
                probs.append("fecha '%s' sem abrir correspondente" % c)
            else:
                est.pilha.pop()
        if c not in " \t\r":
            ultimo_util = c
        i += 1

    if in_dq:
        probs.append('string com " nao foi fechada na linha')
    if in_sq:
        probs.append("string com ' nao foi fechada na linha")

    return probs, ultimo_util


def checa(caminho):
    with open(caminho, encoding="utf-8") as f:
        linhas = f.read().split("\n")

    est = Estado()
    problemas = []
    # para a regra 3 preciso do ultimo char util de cada linha e do primeiro
    # token da seguinte
    infos = []
    for raw in linhas:
        probs, ultimo = escanear(raw, est)
        num = len(infos) + 1
        for p in probs:
            problemas.append("linha %d: %s" % (num, p))
        primeiro = raw.strip().split()[0] if raw.strip().split() else ""
        infos.append((num, ultimo, primeiro))

    # regra 3: string completa no fim + operador no comeco da proxima
    for k in range(len(infos) - 1):
        num, ultimo, _ = infos[k]
        _, _, primeiro_prox = infos[k + 1]
        if ultimo in ('"', "'") and primeiro_prox:
            # tira parentese inicial: "(+ \"x\"" ou "+ \"x\""
            tok = primeiro_prox.lstrip("([{").split()[0] if primeiro_prox.lstrip("([{").split() else ""
            if tok in OPERADORES or primeiro_prox in OPERADORES:
                problemas.append(
                    "linha %d-%d: string completa no fim da linha e '%s' no "
                    "comeco da seguinte -- o parser do PowerShell trata a "
                    "quebra como fim de instrucao (MissingEndParenthesis)"
                    % (num, num + 1, tok or primeiro_prox))

    if est.pilha:
        problemas.append("fim do arquivo com %d grupo(s) aberto(s): %s"
                         % (len(est.pilha), "".join(est.pilha)))
    return problemas


def main():
    if len(sys.argv) < 2:
        print("uso: checa_ps1.py <arquivo.ps1> ...")
        return 2
    total = 0
    for caminho in sys.argv[1:]:
        probs = checa(caminho)
        if probs:
            total += len(probs)
            print("FALHA  %s" % caminho)
            for p in probs:
                print("        %s" % p)
        else:
            print("PASSA  %s" % caminho)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
