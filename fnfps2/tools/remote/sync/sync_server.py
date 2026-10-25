#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Servidor da ponte sincrona. Roda no MEU sandbox, nao no PC do usuario.

O problema que isto resolve: o canal ntfy eh assincrono por natureza -- eu
publico, o PC do usuario poleia, executa, responde, e ALGUEM precisa colar a
resposta de volta. Nao existe "enviar e receber na mesma mensagem" por aquele
caminho.

Aqui o caminho eh outro. O servidor fica de pe e eu leio o resultado DENTRO do
mesmo turno:

    eu -> POST /enqueue  {cmd}            (guarda na fila, devolve o id)
    PC -> GET  /next                       (o agente poleia, pega o comando)
    PC -> POST /result {id, rc, out, err}  (executou e devolveu)
    eu -> GET  /result/<id>                (leio o resultado, ainda no turno)

A latencia eh a do poleia do agente (0,5 s) mais a execucao. Para um build de
17 s, a espera dominante eh o build, nao a ponte.

So stdlib: http.server. Roda em qualquer Python 3 sem instalar nada.

    python3 sync_server.py --porta 8780
"""

import argparse
import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# ----------------------------------------------------------------- estado
LOCK = threading.Lock()
PENDENTES = []          # fila de comandos esperando o agente
RESULTADOS = {}         # id -> resultado
PROXIMO_ID = [1]
AGENTE_VISTO = [0.0]    # ultima vez que o agente de sinal de vida
AGENTE_INFO = [""]
INICIO = time.time()

TEMPO_LIMITE = 600      # segundos; um build do PS2 leva ~20 s, com folga


# ----------------------------------------------------------------- handlers
class Ponte(BaseHTTPRequestHandler):
    # Sem validacao de Host: o preview do Arena serve por um host que nao eh
    # localhost, e o agente do usuario tambem. Recusar por Host quebraria os
    # dois -- que eh exatamente o defeito que esta ponte existe para nao ter.
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        pass

    def _json(self, obj, codigo=200):
        corpo = json.dumps(obj).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corpo)

    def _html(self, texto):
        corpo = texto.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def _corpo(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0:
            return {}
        bruto = self.rfile.read(n)
        try:
            return json.loads(bruto.decode("utf-8"))
        except Exception:
            return {}

    # ------------------------------------------------------------ GET
    def do_GET(self):
        caminho = self.path.split("?")[0]

        if caminho == "/":
            self._html(pagina())
            return

        if caminho == "/next":
            # O agente pede trabalho. Devolve o proximo comando ou diz que nao
            # ha nada. Nunca bloqueia: o agente e quem faz o poleia.
            with LOCK:
                if PENDENTES:
                    job = PENDENTES.pop(0)
                else:
                    job = None
            if job is None:
                self._json({"id": 0})
            else:
                self._json({"id": job["id"], "cmd": job["cmd"],
                            "limite": job.get("limite", TEMPO_LIMITE)})
            return

        if caminho.startswith("/result/"):
            try:
                cid = int(caminho.rsplit("/", 1)[1])
            except ValueError:
                self._json({"erro": "id invalido"}, 400)
                return
            with LOCK:
                r = RESULTADOS.get(cid)
            if r is None:
                self._json({"pronto": False})
            else:
                self._json({"pronto": True, "id": cid, "rc": r["rc"],
                            "out": r["out"], "err": r["err"],
                            "segundos": r["segundos"]})
            return

        if caminho == "/estado":
            with LOCK:
                self._json({
                    "pendentes": len(PENDENTES),
                    "resultados": len(RESULTADOS),
                    "agente_visto_ha": round(time.time() - AGENTE_VISTO[0], 1)
                    if AGENTE_VISTO[0] else None,
                    "agente": AGENTE_INFO[0],
                    "no_ar_ha": round(time.time() - INICIO, 1),
                })
            return

        self._json({"erro": "caminho desconhecido: %s" % caminho}, 404)

    # ------------------------------------------------------------ POST
    def do_POST(self):
        caminho = self.path.split("?")[0]
        dados = self._corpo()

        if caminho == "/enqueue":
            cmd = (dados.get("cmd") or "").strip()
            if not cmd:
                self._json({"erro": "cmd vazio"}, 400)
                return
            with LOCK:
                cid = PROXIMO_ID[0]
                PROXIMO_ID[0] += 1
                PENDENTES.append({"id": cid, "cmd": cmd,
                                  "limite": int(dados.get("limite", TEMPO_LIMITE))})
            self._json({"id": cid})
            return

        if caminho == "/ping":
            # O agente se anuncia. Serve para eu saber, antes de mandar o
            # primeiro comando, se tem alguem do outro lado.
            with LOCK:
                AGENTE_VISTO[0] = time.time()
                AGENTE_INFO[0] = (dados.get("info") or "")[:200]
            self._json({"ok": True})
            return

        if caminho == "/result":
            try:
                cid = int(dados.get("id"))
            except (TypeError, ValueError):
                self._json({"erro": "id invalido"}, 400)
                return
            with LOCK:
                RESULTADOS[cid] = {
                    "rc": int(dados.get("rc", -1)),
                    "out": dados.get("out", "")[:200000],
                    "err": dados.get("err", "")[:50000],
                    "segundos": float(dados.get("segundos", 0)),
                }
            self._json({"ok": True})
            return

        self._json({"erro": "caminho desconhecido: %s" % caminho}, 404)


def pagina():
    with LOCK:
        pend = len(PENDENTES)
        res = len(RESULTADOS)
        visto = ("ha %.1f s" % (time.time() - AGENTE_VISTO[0])
                 if AGENTE_VISTO[0] else "nunca")
        info = AGENTE_INFO[0] or "-"
        no_ar = time.time() - INICIO
    # Sem formatacao por %: o CSS tem "width:100%" e o % quebra o operador.
    # Ja quebrou uma vez, em producao, com ValueError. Concatenacao nao falha.
    return (
        "<!doctype html><meta charset=utf-8>"
        "<title>FNF ponte sincrona</title>"
        "<style>"
        "body{font:15px/1.5 system-ui,sans-serif;max-width:760px;"
        "margin:40px auto;padding:0 16px;background:#111;color:#e8e8e8}"
        "h1{font-size:20px;margin:0 0 4px}small{color:#888}"
        "table{border-collapse:collapse;margin:18px 0;width:100%}"
        "td{padding:6px 10px;border-bottom:1px solid #2a2a2a}"
        "td:first-child{color:#8ab;width:150px}"
        ".ok{color:#6c6}code{background:#1c1c1c;padding:2px 5px;"
        "border-radius:3px}"
        "</style>"
        "<h1>FNF &mdash; ponte sincrona</h1>"
        "<small>Eu mando um comando, o agente no seu PC executa, eu leio a "
        "resposta no mesmo turno. Esta pagina eh so para voce ver que esta "
        "no ar.</small>"
        "<table>"
        "<tr><td>agente visto</td><td>" + visto + "</td></tr>"
        "<tr><td>quem eh</td><td><code>" + info + "</code></td></tr>"
        "<tr><td>na fila</td><td>" + str(pend) + "</td></tr>"
        "<tr><td>resultados</td><td>" + str(res) + "</td></tr>"
        "<tr><td>no ar ha</td><td>" + ("%.0f s" % no_ar) + "</td></tr>"
        "</table>"
        "<p><small>Para parar: feche esta aba e o processo. O agente no seu "
        "PC pode ficar rodando: se o servidor nao responde, ele apenas "
        "continua poleando.</small></p>"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--porta", type=int, default=8780)
    ap.add_argument("--host", default="0.0.0.0")
    a = ap.parse_args()
    srv = ThreadingHTTPServer((a.host, a.porta), Ponte)
    print("ponte sincrona em http://%s:%d" % (a.host, a.porta), flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()
