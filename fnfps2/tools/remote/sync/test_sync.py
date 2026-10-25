#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teste da ponte sincrona. Prova a ida e a volta, aqui, antes de entregar.

O que este teste existe para pegar:

1. A ponte realmente completa um comando? (ida -> execucao -> volta)
2. O /dev/null passa? -- a licao do outro cliente: sem tirar o sumidouro,
   `2>/dev/null` era recusado e o comando morria antes de rodar.
3. Area protegida CONTINUA bloqueada? Afrouxar a trava para consertar o
   falso positivo seria trocar um defeito por outro.
4. O agente sobrevive a rede oscilando e a comando que estoura o tempo?

    python3 test_sync.py
"""

import json
import os
import subprocess
import sys
import time
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
PORTA = 8791
BASE = "http://127.0.0.1:%d" % PORTA
FALHOU = []


def ok(cond, msg):
    print(("  OK    " if cond else "  FALHA ") + msg)
    if not cond:
        FALHOU.append(msg)


def pedir(caminho, dados=None, tempo=30):
    if dados is None:
        req = urllib.request.Request(BASE + caminho, method="GET")
    else:
        corpo = json.dumps(dados).encode("utf-8")
        req = urllib.request.Request(BASE + caminho, data=corpo, method="POST")
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=tempo) as r:
        return json.loads(r.read().decode("utf-8"))


def esperar(cid, segundos=30):
    """Poleia o resultado. Eh EXATAMENTE o que eu faco no turno real."""
    fim = time.time() + segundos
    while time.time() < fim:
        r = pedir("/result/%d" % cid)
        if r.get("pronto"):
            return r
        time.sleep(0.2)
    return None


def rodar(cmd, limite=None, segundos=30):
    dados = {"cmd": cmd}
    if limite is not None:
        dados["limite"] = limite
    r = pedir("/enqueue", dados)
    return esperar(r["id"], segundos)


# --------------------------------------------------------------- sobe servidor
print("\n== 1. sobe a ponte ==")
srv = subprocess.Popen([sys.executable, os.path.join(AQUI, "sync_server.py"),
                        "--porta", str(PORTA), "--host", "127.0.0.1"],
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
ag = None
try:
    no_ar = False
    for _ in range(60):
        try:
            pedir("/estado", tempo=3)
            no_ar = True
            break
        except Exception:
            time.sleep(0.2)
    ok(no_ar, "servidor respondeu em /estado")

    print("\n== 2. sobe o agente ==")
    ag = subprocess.Popen([sys.executable, os.path.join(AQUI, "sync_agent.py"),
                           "--servidor", BASE],
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    visto = False
    for _ in range(60):
        try:
            e = pedir("/estado", tempo=3)
            if e.get("agente_visto_ha") is not None:
                visto = True
                break
        except Exception:
            pass
        time.sleep(0.2)
    ok(visto, "agente se anunciou no /ping")

    # A pagina de status eh o que o usuario ve no preview. Meu teste so batia
    # nos endpoints de API e nao pegou que o CSS "width:100%" quebrava a
    # formatacao por % -- quebrou em producao, com ValueError, na cara.
    print("\n== 2b. a pagina de status renderiza ==")
    try:
        with urllib.request.urlopen(BASE + "/", timeout=10) as r:
            html = r.read().decode("utf-8")
        ok(r.status == 200, "GET / devolve 200")
        ok("ponte sincrona" in html, "e tem o titulo")
        ok("width:100%" in html, "e o CSS com % sobreviveu")
    except Exception as e:
        ok(False, "GET / estourou: %s" % e)

    print("\n== 3. a ida e a volta (o que importa) ==")
    t0 = time.time()
    r = rodar("echo 'ola do PC do usuario'; uname -s", segundos=20)
    volta = time.time() - t0
    ok(r is not None, "o resultado voltou")
    if r:
        ok(r["rc"] == 0, "rc=0 (veio %s)" % r["rc"])
        ok("ola do PC do usuario" in r["out"], "a saida do comando chegou")
        ok("Linux" in r["out"], "rodou no bash de verdade, nao em mock")
    print("     latencia da ponte: %.2f s" % volta)

    print("\n== 4. o falso positivo do /dev/null ==")
    # O comando #1 do outro canal morreu exatamente aqui. Sem isto, a ponte
    # parece funcionar no teste comando-a-comando e falha no mundo real.
    r = rodar("git --version 2>/dev/null || echo 'git: AUSENTE'", segundos=20)
    ok(r is not None and r["rc"] == 0, "comando com 2>/dev/null passa")
    if r:
        ok("RECUSADO" not in r["out"], "nao foi recusado pela trava")

    print("\n== 5. area protegida CONTINUA bloqueada ==")
    for mau in ["rm -rf /", "dd if=/dev/zero of=/dev/sda",
                "shutdown -h now", "cat /etc/shadow"]:
        r = rodar(mau, segundos=20)
        ok(r is not None and r["rc"] == 126,
           "recusado: %s" % mau[:40])

    print("\n== 6. o agente nao morre com rede oscilando ==")
    # Mata o servidor, deixa o agente polear no vazio, sobe de novo.
    srv.terminate()
    srv.wait(timeout=10)
    time.sleep(1.5)
    srv = subprocess.Popen([sys.executable, os.path.join(AQUI, "sync_server.py"),
                            "--porta", str(PORTA), "--host", "127.0.0.1"],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ok(ag.poll() is None, "agente continua vivo depois da queda")
    no_ar = False
    for _ in range(60):
        try:
            pedir("/estado", tempo=3)
            no_ar = True
            break
        except Exception:
            time.sleep(0.2)
    ok(no_ar, "servidor voltou")
    r = rodar("echo 'depois da queda'", segundos=20)
    ok(r is not None and "depois da queda" in r["out"],
       "e a ponte funciona de novo")

    print("\n== 7. tempo limite estoura em vez de travar ==")
    r = rodar("sleep 30", limite=3, segundos=25)
    ok(r is not None and r["rc"] == 124, "rc=124 no estouro")
    ok(r is not None and "tempo limite" in r["err"], "e explica o estouro")

finally:
    for p in (ag, srv):
        if p and p.poll() is None:
            p.terminate()
            try:
                p.wait(timeout=5)
            except Exception:
                p.kill()

print()
if FALHOU:
    print("FALHARAM %d de 7 blocos:" % len(FALHOU))
    for f in FALHOU:
        print("  - " + f)
    sys.exit(1)
print("PONTE SINCRONA: todos os blocos passaram")
