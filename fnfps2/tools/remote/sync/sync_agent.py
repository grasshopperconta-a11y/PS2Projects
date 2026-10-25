#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agente da ponte sincrona. Roda no PC DO USUARIO (WSL/Ubuntu).

Fica poleando o servidor. Quando aparece um comando, executa no bash e devolve
a saida. Eu leio a resposta no mesmo turno em que mandei -- a ponte inteira
leva o tempo do poleia (0,5 s) mais a execucao.

    python3 sync_agent.py --servidor https://PORTA-SANDBOX.e2b.app

So stdlib. Nao instala nada, nao precisa de senha, nao abre porta no PC.

Tem a MESMA trava de area protegida do outro cliente, com a licao do /dev/null
ja aplicada: a entrada "/dev/" da lista eh substring de "/dev/null", e sem
tirar o sumidouro antes de comparar, TODO comando com redirecionamento era
recusado. Foi assim que o comando #1 daquele canal morreu.
"""

import argparse
import json
import subprocess
import sys
import time
import urllib.request

TEMPO_LIMITE = 600
POLEIA = 0.5

# ----------------------------------------------------------------- trava
PROTEGIDO = (
    "system32", "syswow64", "winsxs", "/windows/",
    "/etc/", "/boot/", "/dev/", "/sys/", "/proc/",
    "mkfs", "ddif=/dev/", "of=/dev/",
    "shutdown", "poweroff", "reboot", "halt",
    "useradd", "usermod", "userdel", "visudo", "passwd",
    "iptables", "nftables", "ufw",
    ":(){", "forkbomb",
    "rm-rf/", "rm-rf/*", "rm-rf~", "rm-rf$home",
)


def normaliza(cmd):
    """Minusculo, sem espacos, e sem o sumidouro.

    `/dev/null` sai antes de comparar porque `/dev/` -- a entrada que existe
    para barrar `dd if=/dev/sda` -- eh substring dele. Sem isso, `2>/dev/null`,
    que eh o idioma mais comum do shell, era recusado.
    """
    n = cmd.lower()
    for ch in (" ", "\t", "\n", "\r"):
        n = n.replace(ch, "")
    return n.replace("/dev/null", "")


def protegido(cmd):
    n = normaliza(cmd)
    for p in PROTEGIDO:
        if p in n:
            return p
    return None


# ----------------------------------------------------------------- rede
def _pedir(servidor, caminho, dados=None, tempo=30):
    url = servidor.rstrip("/") + caminho
    if dados is None:
        req = urllib.request.Request(url, method="GET")
    else:
        corpo = json.dumps(dados).encode("utf-8")
        req = urllib.request.Request(url, data=corpo, method="POST")
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=tempo) as r:
        return json.loads(r.read().decode("utf-8"))


# ----------------------------------------------------------------- execucao
def executar(cmd, limite):
    """Roda no bash do usuario e devolve (rc, saida, erro, segundos)."""
    t0 = time.time()
    try:
        p = subprocess.run(["bash", "-lc", cmd],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           timeout=limite)
        return (p.returncode,
                p.stdout.decode("utf-8", "replace"),
                p.stderr.decode("utf-8", "replace"),
                round(time.time() - t0, 2))
    except subprocess.TimeoutExpired:
        return (124, "", "estourou o tempo limite de %ds" % limite,
                round(time.time() - t0, 2))
    except Exception as e:
        return (127, "", "falha ao lancar o bash: %s" % e,
                round(time.time() - t0, 2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--servidor", required=True,
                    help="endereco da ponte, ex. https://8780-xxx.e2b.app")
    ap.add_argument("--uma-vez", action="store_true",
                    help="roda um comando e sai (para testar)")
    a = ap.parse_args()

    info = sys.platform
    try:
        with open("/proc/version") as f:
            info = f.read().strip()[:120]
    except Exception:
        pass

    print("agente da ponte sincrona", flush=True)
    print("  servidor: %s" % a.servidor, flush=True)
    print("  maquina : %s" % info, flush=True)
    print("  poleando a cada %.1f s. Deixe esta janela ABERTA." % POLEIA,
          flush=True)
    print(flush=True)

    # Se anunciar falhar, nao adianta continuar: eu ia mandar comando para o
    # nada e concluir que o agente nao funciona.
    try:
        _pedir(a.servidor, "/ping", {"info": info})
        print("  servidor alcancado.", flush=True)
    except Exception as e:
        print("  NAO alcancei o servidor: %s" % e, flush=True)
        print("  Confira o endereco. Nada sera executado.", flush=True)
        return 2

    while True:
        job = None
        try:
            r = _pedir(a.servidor, "/next")
            if r.get("id"):
                job = r
        except Exception:
            # Rede oscilando: poleia de novo. O agente NAO morre por isso.
            time.sleep(POLEIA)
            continue

        if job is None:
            time.sleep(POLEIA)
            continue

        cid = job["id"]
        cmd = job["cmd"]
        print("[%s] comando #%d: %s" % (time.strftime("%H:%M:%S"), cid, cmd[:90]),
              flush=True)

        atingiu = protegido(cmd)
        if atingiu:
            rc, out, err = (126, "",
                            "RECUSADO: o comando menciona '%s', que eh area "
                            "protegida. Nada foi executado." % atingiu)
            seg = 0.0
        else:
            rc, out, err, seg = executar(cmd, int(job.get("limite", TEMPO_LIMITE)))

        print("           rc=%d em %ss" % (rc, seg), flush=True)
        for linha in (out or err or "(sem saida)").splitlines()[:12]:
            print("           " + linha, flush=True)

        try:
            _pedir(a.servidor, "/result",
                   {"id": cid, "rc": rc, "out": out, "err": err,
                    "segundos": seg})
        except Exception as e:
            print("           nao consegui devolver o resultado: %s" % e,
                  flush=True)

        if a.uma_vez:
            return 0


if __name__ == "__main__":
    sys.exit(main())
