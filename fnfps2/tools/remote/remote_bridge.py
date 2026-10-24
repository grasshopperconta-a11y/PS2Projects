#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ponte de comando remoto para o PS2 do projeto FNF PS2.

Divide-se em DOIS lados, com seguranca diferente de proposito:

  lado do CLIENTE (o PC do usuario)
      escuta numa URL publica, precisa do TOKEN_CLIENTE.
      Pode enfileirar comandos? NAO. So receber trabalho e devolver resultado.
      Um invasor que descubra a URL nao consegue injetar comando nenhum --
      para isso precisaria do TOKEN_CLIENTE, que so o programa do usuario tem.

  lado do OPERADOR (eu)
      so responde em 127.0.0.1/::1 E exige TOKEN_OPERADOR.
      Duas barreiras independentes. E por aqui que eu mando os comandos.

Nada aqui fala com o PS2: eh so um canal de execucao no PC do usuario.

Uso:
    python3 remote_bridge.py --port 8791
"""

import argparse
import base64
import json
import os
import secrets
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

# --------------------------------------------------------------------------
# configuracao
# --------------------------------------------------------------------------

DIRETORIO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "estado")
ARQ_JOBS = os.path.join(DIRETORIO, "jobs.jsonl")
ARQ_RESULTADOS = os.path.join(DIRETORIO, "resultados.jsonl")
ARQ_UPLOADS = os.path.join(DIRETORIO, "uploads")

# teto de saida aceita de um comando, em bytes. Acima disso o cliente e
# orientado a gravar em arquivo e subir em pedacos (ver /chunk).
TETO_SAIDA = 8 * 1024 * 1024

# quanto tempo um job pode ficar na fila sem ser pego. Nao expira trabalho,
# so evita fila infinita se o cliente nunca voltar.
TETO_FILA = 500


def _carregar_ou_gerar(nome, comprimento=32):
    """Token: se existir em disco, usa; senao gera e guarda.

    Guardar em disco faz o token sobreviver a um restart do servidor, que eh
    importante porque o cliente do usuario fica rodando por horas.
    """
    os.makedirs(DIRETORIO, exist_ok=True)
    arq = os.path.join(DIRETORIO, nome)
    if os.path.exists(arq):
        with open(arq, "r", encoding="utf-8") as f:
            t = f.read().strip()
        if t:
            return t
    t = secrets.token_hex(comprimento)
    with open(arq, "w", encoding="utf-8") as f:
        f.write(t + "\n")
    os.chmod(arq, 0o600)
    return t


TOKEN_CLIENTE = None
TOKEN_OPERADOR = None

LOCK = threading.RLock()
JOBS = []            # jobs ainda nao entregues
RESULTADOS = {}      # id -> resultado
ENTREGUES = set()    # ids ja pegos pelo cliente
CONTADOR = [0]
UPLOADS = {}         # id de upload -> caminho do arquivo temporario


def _proximo_id():
    with LOCK:
        CONTADOR[0] += 1
        return CONTADOR[0]


def _persistir_resultado(reg):
    """Resultado tambem vai para disco: se o servidor reiniciar no meio de um
    comando longo, eu nao perco a resposta que jah tinha chegado."""
    try:
        with open(ARQ_RESULTADOS, "a", encoding="utf-8") as f:
            f.write(json.dumps(reg, ensure_ascii=False) + "\n")
    except Exception:
        pass


def _persistir_job(job):
    try:
        with open(ARQ_JOBS, "a", encoding="utf-8") as f:
            f.write(json.dumps(job, ensure_ascii=False) + "\n")
    except Exception:
        pass


# --------------------------------------------------------------------------
# servidor HTTP
# --------------------------------------------------------------------------

class Ponte(BaseHTTPRequestHandler):
    server_version = "FNF-Remote/1.0"
    protocol_version = "HTTP/1.1"

    # silenciar o log padrao: com poll a cada 2s ele encheria a tela
    def log_message(self, fmt, *args):
        pass

    # ---------- utilidades ----------

    def _json(self, obj, codigo=200):
        corpo = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corpo)

    def _texto(self, msg, codigo=200):
        corpo = msg.encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile(corpo) if False else self.wfile.write(corpo)

    def _corpo(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0:
            return b""
        return self.rfile.read(n)

    def _json_corpo(self):
        try:
            return json.loads(self._corpo().decode("utf-8"))
        except Exception:
            return None

    def _eh_local(self):
        """So o operador passa por aqui, e so vindo da propria maquina."""
        host = self.client_address[0] if self.client_address else ""
        return host in ("127.0.0.1", "::1", "::ffff:127.0.0.1", "localhost")

    def _token_header(self, nome):
        return self.headers.get(nome) or ""

    # ---------- rotas ----------

    def do_GET(self):
        rota = urlparse(self.path).path
        if rota == "/health":
            return self._json({
                "ok": True,
                "fila": len(JOBS),
                "resultados": len(RESULTADOS),
                "servidor": "FNF-Remote/1.0",
            })
        try:
            if rota == "/op/resultado":
                return self._op_resultado()
            if rota == "/op/arquivo":
                return self._op_arquivo()
        except _Barrado:
            return None
        except Exception as e:
            return self._json({"erro": "%s: %s" % (type(e).__name__, e)}, 500)
        return self._json({"erro": "rota inexistente"}, 404)

    def do_POST(self):
        rota = urlparse(self.path).path
        try:
            if rota == "/poll":
                return self._poll()
            if rota == "/done":
                return self._done()
            if rota == "/chunk/start":
                return self._chunk_start()
            if rota == "/chunk":
                return self._chunk_append()
            if rota == "/chunk/finish":
                return self._chunk_finish()
            # operador: so enfileirar comando. Leitura de resultado e de
            # arquivo eh GET (ver do_GET) -- leitura nao deve ser POST.
            if rota == "/op/job":
                return self._op_job()
        except _Barrado:
            return None
        except Exception as e:  # nunca derrubar o servidor por um erro de rota
            return self._json({"erro": "%s: %s" % (type(e).__name__, e)}, 500)
        return self._json({"erro": "rota inexistente"}, 404)

    # ---------- cliente ----------

    def _poll(self):
        """O cliente pede trabalho. Sem o token certo, nao leva nada."""
        if not self._autenticado_cliente():
            return self._json({"erro": "token invalido"}, 403)
        with LOCK:
            if not JOBS:
                return self._json({"cmd": None})
            job = JOBS.pop(0)
            ENTREGUES.add(job["id"])
            return self._json({"cmd": job["cmd"], "id": job["id"],
                               "tempo_limite": job.get("tempo_limite", 120)})

    def _done(self):
        if not self._autenticado_cliente():
            return self._json({"erro": "token invalido"}, 403)
        dados = self._json_corpo()
        if not isinstance(dados, dict) or "id" not in dados:
            return self._json({"erro": "corpo invalido"}, 400)
        reg = {
            "id": dados["id"],
            "rc": dados.get("rc"),
            "out": dados.get("out", ""),
            "err": dados.get("err", ""),
            "quando": time.time(),
        }
        with LOCK:
            RESULTADOS[reg["id"]] = reg
        _persistir_resultado(reg)
        return self._json({"ok": True})

    # ---------- upload em pedacos (saida grande) ----------

    def _chunk_start(self):
        if not self._autenticado_cliente():
            return self._json({"erro": "token invalido"}, 403)
        dados = self._json_corpo() or {}
        nome = os.path.basename(str(dados.get("nome", "saida.bin")))[:120] or "saida.bin"
        uid = secrets.token_hex(8)
        os.makedirs(ARQ_UPLOADS, exist_ok=True)
        caminho = os.path.join(ARQ_UPLOADS, uid + "_" + nome)
        with LOCK:
            UPLOADS[uid] = caminho
        open(caminho, "wb").close()
        return self._json({"upload": uid, "caminho": caminho})

    def _chunk_append(self):
        if not self._autenticado_cliente():
            return self._json({"erro": "token invalido"}, 403)
        dados = self._json_corpo()
        if not isinstance(dados, dict):
            return self._json({"erro": "corpo invalido"}, 400)
        uid = str(dados.get("upload", ""))
        with LOCK:
            caminho = UPLOADS.get(uid)
        if not caminho:
            return self._json({"erro": "upload desconhecido"}, 404)
        b64 = dados.get("dados", "")
        try:
            bloco = base64.b64decode(b64)
        except Exception:
            return self._json({"erro": "base64 invalido"}, 400)
        with open(caminho, "ab") as f:
            f.write(bloco)
        return self._json({"ok": True, "bytes": os.path.getsize(caminho)})

    def _chunk_finish(self):
        if not self._autenticado_cliente():
            return self._json({"erro": "token invalido"}, 403)
        dados = self._json_corpo() or {}
        uid = str(dados.get("upload", ""))
        with LOCK:
            caminho = UPLOADS.pop(uid, None)
        if not caminho or not os.path.exists(caminho):
            return self._json({"erro": "upload desconhecido"}, 404)
        return self._json({"ok": True, "caminho": caminho,
                           "bytes": os.path.getsize(caminho)})

    def _autenticado_cliente(self):
        t = self._token_header("X-Token")
        return bool(t) and secrets.compare_digest(t, TOKEN_CLIENTE)

    # ---------- operador (so eu) ----------

    def _op_job(self):
        self._exigir_operador()
        dados = self._json_corpo()
        if not isinstance(dados, dict) or not str(dados.get("cmd", "")).strip():
            return self._json({"erro": "cmd vazio"}, 400)
        with LOCK:
            if len(JOBS) >= TETO_FILA:
                return self._json({"erro": "fila cheia"}, 429)
            job = {
                "id": _proximo_id(),
                "cmd": str(dados["cmd"]),
                "tempo_limite": int(dados.get("tempo_limite", 120)),
                "criado": time.time(),
            }
            JOBS.append(job)
        _persistir_job(job)
        return self._json({"ok": True, "id": job["id"]})

    def _op_resultado(self):
        self._exigir_operador()
        q = parse_qs(urlparse(self.path).query)
        with LOCK:
            if "id" in q:
                i = int(q["id"][0])
                r = RESULTADOS.get(i)
                if r is None:
                    return self._json({"pronto": False, "id": i})
                return self._json({"pronto": True, "resultado": r})
            return self._json({"resultados": sorted(
                RESULTADOS.values(), key=lambda r: r["id"])})

    def _op_arquivo(self):
        """Eu leio um arquivo que estah no MEU servidor (ex.: upload do
        cliente). Caminho preso ao diretorio de uploads -- nao ah como escapar
        dele e ler arquivo arbitrario do sandbox."""
        self._exigir_operador()
        q = parse_qs(urlparse(self.path).query)
        nome = os.path.basename(q.get("nome", [""])[0])
        if not nome:
            return self._json({"erro": "nome vazio"}, 400)
        caminho = os.path.join(ARQ_UPLOADS, nome)
        if not os.path.isfile(caminho):
            return self._json({"erro": "nao encontrado"}, 404)
        with open(caminho, "rb") as f:
            dados = f.read()
        return self._json({
            "nome": nome,
            "bytes": len(dados),
            "b64": base64.b64encode(dados).decode("ascii"),
        })

    def _exigir_operador(self):
        if not self._eh_local():
            self._json({"erro": "operador so pela maquina local"}, 403)
            raise _Barrado()
        if not secrets.compare_digest(self._token_header("X-Op"), TOKEN_OPERADOR):
            self._json({"erro": "token de operador invalido"}, 403)
            raise _Barrado()


class _Barrado(Exception):
    pass


def main():
    global TOKEN_CLIENTE, TOKEN_OPERADOR

    ap = argparse.ArgumentParser()
    ap.add_argument("--porta", type=int, default=8791)
    ap.add_argument("--token-cliente", default=None)
    ap.add_argument("--token-operador", default=None)
    ap.add_argument("--mostrar-tokens", action="store_true")
    args = ap.parse_args()

    TOKEN_CLIENTE = args.token_cliente or _carregar_ou_gerar("token_cliente")
    TOKEN_OPERADOR = args.token_operador or _carregar_ou_gerar("token_operador")

    srv = ThreadingHTTPServer(("0.0.0.0", args.porta), Ponte)
    srv.daemon_threads = True

    print("ponte FNF no ar na porta %d" % args.porta)
    print("  cliente : POST /poll, /done, /chunk/*")
    print("  operador: POST /op/* (so 127.0.0.1)")
    if args.mostrar_tokens:
        print("  TOKEN_CLIENTE   = %s" % TOKEN_CLIENTE)
        print("  TOKEN_OPERADOR  = %s" % TOKEN_OPERADOR)
    sys.stdout.flush()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
