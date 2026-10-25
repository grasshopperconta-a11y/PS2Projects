#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teste do cliente WSL. Roda sozinho, sem rede de verdade.

    python3 test_wsl.py

O que ele prova, e POR QUE cada coisa estah aqui:

  1. PARSE — ids validos, `@volta`, `@modo`, e a recusa de id 0. O id 0 eh um
     comando fantasma: o estado inicial eh 0 e a comparacao eh "<=", entao um
     id 0 nunca passaria e eu ia achar que o comando tinha sumido.

  2. TRAVA — o que eh area protegida tem de ser recusado, e o que eh comando
     normal tem de PASSAR. `rm -r f` (apagar a pasta "f") precisa passar: uma
     trava que recusa comando legitimo eh pior que nenhuma trava, porque
     impossibilita o trabalho.

  3. PUBLICACAO — o PUT tem de sair com os cabecalhos EXATOS
     `Connection, Content-Length, Host` e NENHUM Content-Type.

     Esta eh a parte mais importante do teste, e o motivo eh historico: o
     cliente PowerShell jah quebrou DUAS vezes por causa de Content-Type. O
     experimento controlado (canal #52) mediou tres variantes no ntfy real,
     todas com acento de verdade:

         A1 <string>, sem Content-Type        -> ANEXO (charset=iso-8859-1)
         A2 byte[]  , sem Content-Type        -> MENSAGEM   <-- esta forma
         A3 <string>, ContentType text/plain  -> ANEXO (charset=iso-8859-1)

     E a primeira versao DESTE cliente repetiu o erro por outro caminho: o
     `urllib`, quando recebe `data=`, INJETA sozinho
     `Content-Type: application/x-www-form-urlencoded`. O teste pega isso
     inspecionando os cabecalhos que realmente saem no socket -- nao o que o
     codigo pede, o que sai.

  4. O `Host` precisa levar a porta quando ela nao eh a padrao do esquema.
  5. Fatiamento: log de build estoura o limite, e o meio tem de ser cortado
     com um marcador dizendo quantos pedacos se perderam.
  6. Robustez: endereco vazio, texto None e host inalcancavel NAO podem
     estourar. Um erro de publicacao nao deve derrubar o cliente.
"""

import importlib.util
import os
import socketserver
import sys
import threading
import http.server

AQUI = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(AQUI, "fnf-remote-wsl.py")

spec = importlib.util.spec_from_file_location("fnfremotewsl", ARQ)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

FALHAS = []


def ok(cond, msg):
    print(("  OK    " if cond else "  FALHA ") + msg)
    if not cond:
        FALHAS.append(msg)


# ------------------------------------------------------------- servidor local
class Receptor(http.server.BaseHTTPRequestHandler):
    """Imita o ntfy: aceita PUT e GRAVA o que recebeu, cabecalhos inclusos."""

    recebido = []

    def log_message(self, *a):
        pass

    def do_PUT(self):
        n = int(self.headers.get("Content-Length") or 0)
        self.recebido.append({
            "path": self.path,
            "ct": self.headers.get("Content-Type"),
            "host": self.headers.get("Host"),
            "corpo": self.rfile.read(n),
            "hdrs": dict(self.headers.items()),
        })
        self.send_response(200)
        self.send_header("Content-Length", "2")
        self.end_headers()
        self.wfile.write(b"{}")


class Srv(socketserver.ThreadingTCPServer):
    allow_reuse_address = True


def sobe_servidor(porta):
    srv = Srv(("127.0.0.1", porta), Receptor)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


# ------------------------------------------------------------------- 1. parse
print("\n== 1. parse do canal ==")
TEXTO = """# comentario
@volta https://ntfy.sh/topico-teste
@modo ultimo

1|SH: echo oi
2|PS: Get-Item F:\\
3|
0|SH: fantasma
abc|SH: nao eh id
4|SH: echo quatro
"""
volta, modo, novos = c.parse(TEXTO, 0, "fila")
ok(volta == "https://ntfy.sh/topico-teste", "pega @volta")
ok(modo == "ultimo", "pega @modo")
ok([j["id"] for j in novos] == [1, 2, 4],
   "ids validos, sem 0/vazio/nao-numerico: %s" % [j["id"] for j in novos])
ok(novos[0]["cmd"] == "SH: echo oi", "guarda o comando")
_, _, n2 = c.parse(TEXTO, 2, "fila")
ok([j["id"] for j in n2] == [4], "pula os que ja rodaram")
ok(c.parse("", 0, "fila")[2] == [], "canal vazio nao estoura")

# ------------------------------------------------------------------- 2. trava
print("\n== 2. trava de seguranca ==")
for bom in ["rm -rf /", "dd if=/dev/zero of=/dev/sda", "sudo mkfs.ext4 /dev/sdb1",
            "shutdown -h now", "echo x > /etc/passwd", "visudo",
            ":(){ :|:& };:", "useradd hacker", "iptables -F",
            "del /f /s /q C:\\Windows\\System32", "R M - R F /"]:
    ok(c.protegido(bom) is not None, "recusa: %s" % bom[:42])
for seguro in ["ls -la", "make -j4", "cat file.txt", "git status",
               "python3 tools/test.py", "grep -rn foo src/",
               "apt list --installed", "rm -r f"]:
    ok(c.protegido(seguro) is None, "deixa passar: %s" % seguro)
# `rm -r f` apaga a pasta "f": comando legitimo. Uma trava que recusasse
# isso impossibilitaria o trabalho -- e trava assim eh pior que trava nenhuma.

# ---------------------------------------------------------- 2b. o falso positivo
# O idioma mais comum do shell eh silenciar uma saida com 2>/dev/null. A trava
# bloqueava a substring "/dev/", que esta DENTRO de "/dev/null": com isso, todo
# comando com redirecionamento era recusado, e o #1 do canal WSL morreu assim.
# Regressao medida, nao hipotetica: o comando de prova de vida do canal foi
# recusado three vezes antes de alguem ler a lista de padrões.
print("\n== 2b. /dev/null NAO pode ser area protegida ==")
for comum in ["git --version 2>/dev/null || echo 'git: AUSENTE'",
              "ls -d /opt/ps2dev 2>/dev/null || echo 'ps2dev: AUSENTE'",
              "which gcc make 2>/dev/null",
              "echo oi > /dev/null",
              "make -j4 > /dev/null 2>&1",
              "curl -sL -o /tmp/x URL > /dev/null",
              "tar -xJf a.tar.xz -C ~/ps2dev 2>/dev/null"]:
    ok(c.protegido(comum) is None, "deixa passar: %s" % comum[:44])
# E o que a regra existe para impedir CONTINUA impedido:
for bloqueado in ["dd if=/dev/zero of=/dev/sda", "dd if=/dev/sda of=/tmp/img",
                  "mkfs.ext4 /dev/sdb1", "cat /dev/sda > /tmp/copia",
                  "echo x > /dev/sda"]:
    ok(c.protegido(bloqueado) is not None, "recusa: %s" % bloqueado[:44])

# -------------------------------------------------------------- 3. publicacao
print("\n== 3. publicacao (a licao do #52) ==")
PORTA = 8801
srv = sobe_servidor(PORTA)
try:
    Receptor.recebido = []
    c.publicar("http://127.0.0.1:%d/topico-teste" % PORTA,
               "com acento: \u00e1\u00e3\u00e9")
    ok(len(Receptor.recebido) == 1, "uma publicacao")
    v = Receptor.recebido[0]
    ok(v["path"] == "/topico-teste", "caminho certo: %s" % v["path"])
    ok(v["ct"] is None,
       "NENHUM Content-Type (era ele que virava anexo): %r" % v["ct"])
    ok(sorted(v["hdrs"]) == ["Connection", "Content-Length", "Host"],
       "cabecalhos exatos: %s" % sorted(v["hdrs"]))
    ok(v["corpo"] == "com acento: \u00e1\u00e3\u00e9".encode("utf-8"),
       "corpo eh byte[] UTF-8 de verdade")
    ok(v["host"] == "127.0.0.1:%d" % PORTA,
       "Host com porta nao-padrao: %s" % v["host"])

    # texto vazio
    Receptor.recebido = []
    c.publicar("http://127.0.0.1:%d/t" % PORTA, "")
    ok(len(Receptor.recebido) == 1 and Receptor.recebido[0]["corpo"] == b"",
       "texto vazio publica um corpo vazio, sem estourar")

    # ---------------------------------------------------------- 4. fatiamento
    print("\n== 4. fatiamento de log grande ==")
    Receptor.recebido = []
    grande = ("linha %d com acento \u00e1\u00e3\n" * 6000) % tuple(range(6000))
    c.publicar("http://127.0.0.1:%d/t" % PORTA, grande)
    ok(len(Receptor.recebido) == c.MAX_PEDACOS,
       "cortado em %d pedacos (o limite)" % c.MAX_PEDACOS)
    ok(Receptor.recebido[0]["corpo"].startswith(
        b"[parte 1/%d]" % c.MAX_PEDACOS), "numera as partes")
    ok(b"omitidos no meio" in Receptor.recebido[c.MAX_PEDACOS - 5]["corpo"],
       "marca quantos pedacos se perderam no meio")
    total = sum(x["len"] if "len" in x else len(x["corpo"])
                for x in Receptor.recebido)
    ok(total < len(grande.encode()),
       "publicou %d de %d bytes (cortou de proposito)" % (total, len(grande.encode())))

    # --------------------------------------------------------- 5. robustez
    print("\n== 5. robustez ==")
    ok(c.publicar("", "x") is False, "sem endereco devolve False sem estourar")
    try:
        c.publicar("http://127.0.0.1:%d/t" % PORTA, None)
        ok(True, "texto None nao estoura")
    except Exception as e:
        ok(False, "texto None ESTOUROU: %s" % e)
    try:
        c.publicar("http://127.0.0.1:1/x", "y")
        ok(True, "host inalcancavel nao estoura")
    except Exception as e:
        ok(False, "host inalcancavel ESTOUROU: %s" % e)
finally:
    srv.shutdown()

# --------------------------------------------------------------- 6. execucao
print("\n== 6. execucao no bash ==")
rc, out, err = c.executar("echo ola", AQUI, None)
ok(rc == 0 and out.strip() == "ola", "roda comando simples: rc=%d out=%r" % (rc, out.strip()))
rc, out, err = c.executar("SH: echo comprefixo", AQUI, None)
ok(rc == 0 and out.strip() == "comprefixo", "prefixo SH: eh removido")
rc, out, err = c.executar("echo $HOME", AQUI, None)
ok(rc == 0 and out.strip() != "", "ve variaveis de ambiente")
rc, out, err = c.executar("exit 3", AQUI, None)
ok(rc == 3, "propaga o codigo de saida: %d" % rc)
rc, out, err = c.executar("echo erro >&2; exit 0", AQUI, None)
ok("erro" in err, "captura o stderr")

# O timeout: baixo o limite so aqui, senao o teste levaria 3 minutos. `sleep 30`
# sozinho NAO estoura o limite de 180s -- cuidado: um teste que espera o
# estouro errado passa por acidente e nao prova nada.
limite_real = c.TEMPO_LIMITE
c.TEMPO_LIMITE = 3
try:
    rc, out, err = c.executar("sleep 30", AQUI, None)
    ok(rc == 124 and "tempo limite" in err,
       "estoura o tempo limite em vez de travar: rc=%d err=%r" % (rc, err.strip()))
finally:
    c.TEMPO_LIMITE = limite_real

# ---------------------------------------------------------------------- fim
print()
if FALHAS:
    print("FALHOU: %d teste(s)" % len(FALHAS))
    for f in FALHAS:
        print("   - " + f)
    sys.exit(1)
print("TODOS OS TESTES PASSARAM")
