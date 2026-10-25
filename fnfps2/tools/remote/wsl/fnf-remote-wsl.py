#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FNF REMOTE -- cliente para WSL / Ubuntu.

Mesma ideia do cliente PowerShell (``fnf-remote-client.ps1``): fica aberto,
le um canal de comandos PUBLICO do GitHub, executa o que eu mandar e publica a
saida de volta para eu ler. A diferenca eh que aqui o que roda eh o bash do
Ubuntu, dentro do WSL -- entao eu consigo COMPILAR e TESTAR de verdade, na
maquina do usuario, durante o meu raciocinamento.

    python3 fnf-remote-wsl.py --canal <url> [--dir <pasta>] [--intervalo 5]

NAO PRECISA INSTALAR NADA: Python 3 e bash ja vem no Ubuntu do WSL.
NAO PRECISA DE SENHA.

--------------------------------------------------------------------------
AS TRES LICOES QUE ESTAO EMBUTIDAS AQUI (custaram tempo para aprender)
--------------------------------------------------------------------------

1. O CANAL DE VOLTA SO ACEITA byte[] EM UTF-8, SEM ContentType.
   O cliente PowerShell descobriu isso por experimento controlado (canal #52):
   tres variantes, todas com acento de verdade, publicadas no ntfy:

       A1 <string>, sem ContentType        -> virou ANEXO (charset=iso-8859-1)
       A2 byte[]  , sem ContentType        -> virou MENSAGEM   <-- esta
       A3 <string>, ContentType text/plain -> virou ANEXO (charset=iso-8859-1)

   Ou seja: mandar texto como str faz o ntfy gravar charset iso-8859-1 e
   transformar o corpo em arquivo anexo -- e a saida fica ilegivel do meu
   lado. Aqui eh a mesma regra, e ha um teste que falha se alguem voltar
   atras. NUNCA declarar Content-Type no PUT.

2. A LEITURA DO CANAL PRECISA DE CACHE-BUSTER.
   O GitHub poe um CDN na frente do raw. Sem um ``?cb=<numero>`` novo a cada
   tentativa, o cliente fica lendo a copia velha por minutos e eu concluo,
   errado, que o comando nao rodou.

3. MARCAR COMO RODADO ANTES DE EXECUTAR.
   A primeira versao do cliente PowerShell marcava no fim. Quando um comando
   estourou no meio, a marca nunca aconteceu, o laco reabriu e ele tentou o
   MESMO comando para sempre: o canal travou sem saida. Marcando antes, o
   pior caso eh um resultado faltando (eu mando de novo com id novo), que eh
   recuperavel. O outro nao era.
"""

import argparse
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request

# ------------------------------------------------------------------ config
TAMANHO_PEDACO = 2000      # ntfy rejeita corpo grande; fatio neste tamanho
MAX_PEDACOS = 40           # um log de build inteiro nao cabe: corto no meio
TEMPO_LIMITE = 180         # segundos por comando
INTERVALO = 5              # segundos entre consultas ao canal

# Areas que NUNCA podem ser tocadas. A comparacao eh feita na string
# normalizada (minusculo, sem espacos), como no cliente PowerShell, para
# "S Y S T E M 3 2" nao passar por um espaco.
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


# ------------------------------------------------------------------ cor
class C:
    """Cor de console. Desliga sozinho quando nao eh um terminal."""
    ligado = sys.stdout.isatty()

    @classmethod
    def pinta(cls, txt, cor):
        if not cls.ligado:
            return txt
        return "\033[%sm%s\033[0m" % (cor, txt)

    @classmethod
    def verde(cls, t):
        return cls.pinta(t, "32")

    @classmethod
    def cinza(cls, t):
        return cls.pinta(t, "90")

    @classmethod
    def amarelo(cls, t):
        return cls.pinta(t, "93")

    @classmethod
    def vermelho(cls, t):
        return cls.pinta(t, "91")

    @classmethod
    def ciano(cls, t):
        return cls.pinta(t, "96")


def log(txt, cor=None):
    linha = "[%s] %s" % (time.strftime("%H:%M:%S"), txt)
    print(C.pinta(linha, cor) if cor else linha, flush=True)


# ------------------------------------------------------------------ canal
def busca_canal(url):
    """Le o canal. O ?cb= fura o cache do CDN do GitHub (licao 2)."""
    sep = "&" if "?" in url else "?"
    alvo = "%s%scb=%d" % (url, sep, int(time.time() * 1000))
    req = urllib.request.Request(alvo, headers={"User-Agent": "fnf-remote-wsl/1"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return None


def normaliza(cmd):
    """Minusculo, sem espacos: a trava de seguranca compara assim."""
    n = cmd.lower()
    for ch in (" ", "\t", "\n", "\r"):
        n = n.replace(ch, "")
    # `2>/dev/null` e `>/dev/null` sao o idioma MAIS COMUM do shell -- e a trava
    # bloqueava a substring "/dev/", que esta dentro de "/dev/null". Resultado:
    # todo comando que silenciasse uma saida era recusado, e o comando #1 do
    # canal morreu exatamente assim. O alvo da regra eh dispositivo de bloco
    # (/dev/sda, /dev/nvme, /dev/zero), nunca o sumidouro. Tirar o sumidouro
    # antes de comparar resolve o falso positivo sem afrouxar o resto: "dd
    # if=/dev/zero" continua recusado, porque la o "/dev/" que sobra eh de um
    # dispositivo de verdade.
    n = n.replace("/dev/null", "")
    return n


def protegido(cmd):
    """Devolve o trecho proibido, ou None. Roda ANTES de qualquer execucao."""
    n = normaliza(cmd)
    for p in PROTEGIDO:
        if p in n:
            return p
    return None


def parse(texto, ja_rodou, modo):
    """Devolve (volta, modo, [jobs]). Mesma semantica do cliente PowerShell."""
    volta = None
    novo_modo = modo
    novos = []
    for linha in texto.splitlines():
        l = linha.strip()
        if l == "" or l.startswith("#"):
            continue

        if l.startswith("@volta "):
            nv = l[6:].strip()
            if nv:
                volta = nv
            continue

        if l.startswith("@modo "):
            nm = l[6:].strip().lower()
            if nm in ("ultimo", "fila"):
                novo_modo = nm
            continue

        i = l.find("|")
        if i <= 0:
            continue
        id_txt = l[:i].strip()
        cmd = l[i + 1:].strip()
        if cmd == "":
            continue
        try:
            cid = int(id_txt)
        except ValueError:
            continue
        # id >= 1: o estado inicial eh 0 e a comparacao eh "<=" -- um id 0
        # nunca passaria e eu ia achar que o comando tinha sumido.
        if cid < 1:
            continue
        if cid <= ja_rodou:
            continue
        novos.append({"id": cid, "cmd": cmd})
    return volta, novo_modo, novos


# ------------------------------------------------------------------ volta
def _put_cru(url, dados):
    """PUT por socket cru, com os cabecalhos EXATOS que eu quero.

    Por que nao urllib: o urllib, quando recebe `data=`, INJETA sozinho
    `Content-Type: application/x-www-form-urlencoded` se nenhum for
    declarado. Foi justamente isso que quebrou a primeira versao deste
    cliente -- e eh a mesma classe de defeito que o experimento #52 pegou no
    cliente PowerShell.

    O que o experimento #52 mediu, com acento de verdade, no ntfy real:

        A1 <string>, sem Content-Type        -> ANEXO (charset=iso-8859-1)
        A2 byte[]  , sem Content-Type        -> MENSAGEM   <-- esta forma
        A3 <string>, ContentType text/plain  -> ANEXO (charset=iso-8859-1)

    E o proprio documento do ntfy confirma: o exemplo HTTP cru de publicacao
    (docs.ntfy.sh/publish) eh

        PUT /mytopic HTTP/1.1
        Host: ntfy.sh

        texto

    -- ou seja, `Host:` e NENHUM Content-Type. Aqui eu mando exatamente isso.
    """
    import socket
    import ssl
    from urllib.parse import urlsplit

    p = urlsplit(url)
    host = p.hostname or "ntfy.sh"
    padrao = (443 if p.scheme != "http" else 80)
    porta = p.port or padrao
    # Host precisa levar a porta quando ela nao eh a padrao do esquema
    # (HTTP/1.1 exige). Sem isso um endereco em porta estranha quebraria.
    host_hdr = host if porta == padrao else "%s:%d" % (host, porta)
    caminho = (p.path or "/") + (("?" + p.query) if p.query else "")
    if not caminho.startswith("/"):
        caminho = "/" + caminho

    cab = ("PUT %s HTTP/1.1\r\nHost: %s\r\nContent-Length: %d\r\n"
           "Connection: close\r\n\r\n"
           % (caminho, host_hdr, len(dados))).encode("ascii")

    if p.scheme == "http":
        s = socket.create_connection((host, porta), timeout=30)
    else:
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.create_connection((host, porta), timeout=30),
                            server_hostname=host)
    try:
        s.sendall(cab + dados)
        buf = b""
        while True:
            try:
                b = s.recv(65536)
            except Exception:
                break
            if not b:
                break
            buf += b
    finally:
        try:
            s.close()
        except Exception:
            pass
    if not buf:
        raise IOError("resposta vazia do servidor")
    return buf.split(b"\r\n", 1)[0].decode("latin-1", "replace")


def _put_curl(url, dados, arq):
    """Plano B: curl com o Content-Type REMOVIDO.

    `-H 'Content-Type:'` (dois-pontos e nada depois) eh o jeito documentado do
    curl de nao enviar aquele cabecalho. Sem isso o `--data-binary` mandaria
    `application/x-www-form-urlencoded`.
    """
    import subprocess
    r = subprocess.run(
        ["curl", "-s", "-X", "PUT", "-H", "Content-Type:",
         "--data-binary", "@" + arq, url],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    if r.returncode != 0:
        raise IOError("curl rc=%d: %s"
                      % (r.returncode, r.stderr.decode("utf-8", "replace")))
    return "curl ok"


def publicar(url, texto):
    """Publica a saida. Falhar aqui NAO derruba o cliente.

    Licao 1: bytes UTF-8 e NENHUM Content-Type. Ver A1/A2/A3 em _put_cru.
    """
    if not url:
        return False
    if texto is None:
        texto = ""

    pedacos = []
    if len(texto) == 0:
        pedacos.append("")
    else:
        i = 0
        while i < len(texto):
            pedacos.append(texto[i:i + TAMANHO_PEDACO])
            i += TAMANHO_PEDACO

    # Um log de build inteiro nao cabe. Guardo cabeca e cauda, que eh onde
    # estao o que comecou e o que quebrou; o meio vira um marcador.
    if len(pedacos) > MAX_PEDACOS:
        cabeca = pedacos[:MAX_PEDACOS - 5]
        cauda = pedacos[-4:]
        meio = len(pedacos) - len(cabeca) - len(cauda)
        pedacos = cabeca + [
            "[... %d pedacos omitidos no meio (%d bytes); o arquivo "
            "completo ficou em resultados/resultado-<id>.txt ...]"
            % (meio, meio * TAMANHO_PEDACO)
        ] + cauda

    ok = True
    for p, corpo in enumerate(pedacos):
        if len(pedacos) > 1:
            corpo = "[parte %d/%d]\n%s" % (p + 1, len(pedacos), corpo)
        dados = corpo.encode("utf-8")
        try:
            _put_cru(url, dados)
        except Exception:
            # plano B: curl sem o cabecalho. Se os dois falharem, o resultado
            # completo continua no arquivo -- so eu nao leio aquele.
            try:
                import tempfile
                with tempfile.NamedTemporaryFile("wb", delete=False,
                                                 suffix=".ntfy") as f:
                    f.write(dados)
                    arq = f.name
                try:
                    _put_curl(url, dados, arq)
                finally:
                    try:
                        os.unlink(arq)
                    except Exception:
                        pass
            except Exception:
                ok = False
    return ok


# ------------------------------------------------------------------ estado
def ler_ja_rodou(arq):
    try:
        with open(arq, "r", encoding="utf-8") as f:
            v = f.read().strip()
        return int(v) if v.isdigit() else 0
    except Exception:
        return 0


def gravar_ja_rodou(arq, cid):
    try:
        with open(arq, "w", encoding="utf-8") as f:
            f.write(str(cid))
    except Exception:
        pass


# ------------------------------------------------------------------ exec
def executar(cmd, pasta, arq_env):
    """Roda o comando no bash do WSL e devolve (rc, saida, erro)."""
    # Prefixos aceitos, para eu poder colar comandos do canal do Windows:
    #   SH:  -> bash (o caso normal aqui)
    #   PS:  -> tambem bash (compatibilidade; o WSL nao tem PowerShell)
    #   CMD: -> tambem bash (idem)
    for pref in ("SH:", "PS:", "CMD:"):
        if cmd.startswith(pref):
            cmd = cmd[len(pref):].lstrip()
            break

    # Se existir um env.sh ao lado do cliente, ele eh carregado antes. Eh por
    # ele que o toolchain do ps2dev entra no caminho: eu o escrevo por comando
    # remoto quando instalar, e nao preciso reinstalar o cliente depois.
    pre = ""
    if arq_env and os.path.isfile(arq_env):
        pre = ". %s 2>/dev/null; " % arq_env

    alvo = pasta if (pasta and os.path.isdir(pasta)) else os.getcwd()
    # bash -lc carrega o perfil de login (onde o ps2dev costuma se instalar).
    script = "%scd %s 2>/dev/null; %s" % (pre, shell_q(alvo), cmd)

    try:
        p = subprocess.run(
            ["bash", "-lc", script],
            cwd=alvo, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=TEMPO_LIMITE)
        return (p.returncode,
                p.stdout.decode("utf-8", "replace"),
                p.stderr.decode("utf-8", "replace"))
    except subprocess.TimeoutExpired:
        return (124, "", "estourou o tempo limite de %ds" % TEMPO_LIMITE)
    except Exception as e:
        return (127, "", "falha ao lancar o bash: %s" % e)


def shell_q(s):
    """Aspas simples seguras para embutir um caminho no script."""
    return "'" + s.replace("'", "'\\''") + "'"


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description="FNF REMOTE - cliente WSL/Ubuntu")
    ap.add_argument("--canal", required=True, help="URL do canal de comandos")
    ap.add_argument("--dir", default=os.getcwd(),
                    help="pasta onde os comandos rodam")
    ap.add_argument("--intervalo", type=int, default=INTERVALO)
    ap.add_argument("--estado", default=None,
                    help="arquivo do ultimo id rodado (padrao: ./estado.id)")
    ap.add_argument("--resultados", default=None,
                    help="pasta dos resultados (padrao: ./resultados)")
    args = ap.parse_args()

    aqui = os.path.dirname(os.path.abspath(__file__))
    arq_estado = args.estado or os.path.join(aqui, "estado.id")
    pasta_res = args.resultados or os.path.join(aqui, "resultados")
    arq_env = os.path.join(aqui, "env.sh")
    os.makedirs(pasta_res, exist_ok=True)

    volta = ""
    modo = "fila"
    falhas = 0

    print(C.ciano("FNF REMOTE - cliente WSL/Ubuntu"))
    print("  canal    : %s" % args.canal)
    print("  pasta    : %s" % args.dir)
    print("  volta    : a saida eh publicada para eu ler (endereco vem do canal)")
    print("  estado   : %s" % arq_estado)
    print("  saida    : %s" % pasta_res)
    print("  fechar   : so feche esta janela se quiser parar")
    print()

    ja_rodou = ler_ja_rodou(arq_estado)
    if ja_rodou > 0:
        print(C.cinza("  voltando de onde parou: ultimo comando rodado foi o #%d"
                      % ja_rodou))
        print()

    while True:
        texto = busca_canal(args.canal)

        if texto is None:
            falhas += 1
            if falhas % 12 == 1:
                log("nao consegui ler o canal (tentativa %d)" % falhas,
                    C.amarelo.__name__ and "93")
            time.sleep(args.intervalo)
            continue
        falhas = 0

        nova_volta, novo_modo, novos = parse(texto, ja_rodou, modo)

        if nova_volta and nova_volta != volta:
            volta = nova_volta
            log("canal de volta: %s" % volta, "96")
        if novo_modo != modo:
            modo = novo_modo
            log("modo de execucao: %s" % modo, "96")

        if not novos:
            time.sleep(args.intervalo)
            continue

        # modo 'ultimo': de proposito, SO o comando mais novo roda. Os mais
        # antigos sao marcados como rodados e abandonados -- assim um lote meu
        # nao despeja tudo em cascata.
        if modo == "ultimo" and len(novos) > 1:
            maior = max(j["id"] for j in novos)
            for j in novos:
                if j["id"] < maior:
                    ja_rodou = j["id"]
                    gravar_ja_rodou(arq_estado, j["id"])
                    log("#%d deixado para tras: existe um mais novo (#%d)"
                        % (j["id"], maior), "90")
            novos = [j for j in novos if j["id"] == maior]

        novos.sort(key=lambda j: j["id"])

        for job in novos:
            cid, cmd = job["id"], job["cmd"]
            log("comando #%d: %s" % (cid, cmd), "32")

            # MARCA ANTES DE EXECUTAR (licao 3).
            ja_rodou = cid
            gravar_ja_rodou(arq_estado, cid)

            atingiu = protegido(cmd)
            if atingiu:
                log("           RECUSADO: mexe em area protegida", "91")
                txt = ("RECUSADO PELO CLIENTE: o comando menciona '%s', que eh "
                       "area protegida. Nada foi executado no seu PC."
                       % atingiu)
                destino = os.path.join(pasta_res, "resultado-%d.txt" % cid)
                with open(destino, "w", encoding="utf-8") as f:
                    f.write(txt + "\n")
                publicar(volta, txt)
                continue

            rc, out, err = executar(cmd, args.dir, arq_env)

            corpo = ("comando #%d\nrodado em: %s\ncomando : %s\ncodigo : %d\n"
                     "-------- saida --------\n%s"
                     % (cid, time.strftime("%Y-%m-%d %H:%M:%S"), cmd, rc, out))
            if err.strip():
                corpo += "\n-------- erro --------\n" + err

            destino = os.path.join(pasta_res, "resultado-%d.txt" % cid)
            try:
                with open(destino, "w", encoding="utf-8") as f:
                    f.write(corpo)
            except Exception:
                pass

            resumo = out if out.strip() else (err.strip() or "(sem saida)")
            linhas = resumo.splitlines()
            if len(linhas) > 12:
                resumo = "\n".join(linhas[:12]) + \
                    "\n           ... +%d linhas (veja o arquivo)" % (len(linhas) - 12)
            log("           rc=%d, %d bytes -> %s"
                % (rc, len(corpo), os.path.basename(destino)), "90")
            for l in resumo.splitlines():
                print("           " + l, flush=True)

            publicar(volta, corpo)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nencerrado.")
