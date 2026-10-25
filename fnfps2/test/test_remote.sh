#!/bin/sh
# Testes do FNF REMOTE (canal GitHub).
#
# Defeitos reais que jah aconteceram e estao cobertos aqui:
#
#  1. A trava de System32 tinha 'winssxs' onde a pasta real eh 'WinSxS'
#     (lowercase 'winsxs'). Um comando em WinSxS passava.
#
#  2. O .cmd comparava %FNF_PONTE% com @@PONTE@@. Depois de substituir o
#     endereco real, a comparacao ficou "endereco == endereco" e portanto
#     VERDADEIRA -- o programa dava erro e saida em TODO uso.
#
#  3. A versao anterior usava um servidor meu exposto numa URL publica. O
#     proxy do e2b respondeu "502 Sandbox not found" para o usuario: a URL
#     nao eh alcancavel de fora. O canal agora eh um arquivo PUBLICO do
#     GitHub, que qualquer um le e so eu escrevo -- sem servidor, sem senha.
set -e
cd "$(dirname "$0")/.."

PASS=0; FAIL=0
ok()   { PASS=$((PASS+1)); echo "  PASSA  $1"; }
falha(){ FAIL=$((FAIL+1)); echo "  FALHA  $1"; }

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

echo "== trava de System32 =="
# replica EXATAMENTE a normalizacao de Test-Protegido no .ps1:
#   minusculo, sem espacos, barra normalizada
python3 - <<'PY' || exit 1
import re, sys
ps1 = open("tools/remote/fnf-remote-client.ps1", encoding="utf-8").read()
m = re.search(r"\$Protegido = @\((?P<corpo>.*?)\)", ps1, re.S)
assert m, "nao achei $Protegido no .ps1"
itens = re.findall(r"'([^']+)'", m.group("corpo"))
assert itens, "lista vazia"

def protegido(cmd):
    n = cmd.lower()
    n = "".join(n.split())          # -replace '\s+',''
    n = n.replace("/", "\\")        # -replace '/','\'
    for p in itens:
        if p in n:
            return p
    return None

DEVE_BLOQUEAR = [
    "Remove-Item C:\\Windows\\System32\\drivers\\etc\\hosts",
    "del /f /q c:\\windows\\system32\\notepad.exe",
    "rm -r C:/WINDOWS/SYSTEM32",
    "type C:\\WiNdOwS\\SyStEm32\\cmd.exe",
    "Remove-Item 'C:\\Windows\\System 32\\x.dll'",   # espaco no meio
    "copy x C:\\Windows\\SysWOW64\\y",
    "Get-Content C:\\WINDOWS\\WinSxS\\x",             # a pasta real eh WinSxS
    "Get-Content C:\\WINDOWS\\WINSXS\\manifest",
    "del C:\\boot.ini",
    "del %SystemRoot%\\System32\\calc.exe",
    "takeown /f c:\\windows\\system32",
    "reg save HKLM\\SAM C:\\Windows\\System32\\config\\SAM.bak",
    "Remove-Item D:\\System32\\x",                   # outro drive tambem
    "icacls C:\\Windows\\System32 /reset",
]
DEVE_PASSAR = [
    "Get-ChildItem C:\\Users\\meu\\Desktop",
    "Copy-Item FNF_PS2.ELF E:\\",
    "Get-Content E:\\FNFPS2\\FNF_COLHEITA.txt -Tail 50",
    "Get-Volume",
    "Get-Process fnf",
    "whoami /groups",
    "systeminfo | Select-Object -First 20",
    "Test-Path C:\\Windows",                        # so perguntar
    "Get-ComputerInfo | Select OsName",
    "Get-ChildItem E:\\ -Recurse -Filter *.chart",
    "mkdir C:\\Users\\meu\\fnf-teste",
    "Remove-Item C:\\Users\\meu\\fnf-teste -Recurse",
]

erros = []
for c in DEVE_BLOQUEAR:
    if protegido(c) is None:
        erros.append("DEVERIA BLOQUEAR e passou: " + c)
for c in DEVE_PASSAR:
    if protegido(c) is not None:
        erros.append("DEVERIA PASSAR e bloqueou: " + c)
if erros:
    for e in erros:
        print("    " + e)
    sys.exit(1)
print("  PASSA  trava: %d bloqueios e %d liberacoes corretos"
      % (len(DEVE_BLOQUEAR), len(DEVE_PASSAR)))
PY

echo "== parser do canal (formato <id>|<comando>) =="
python3 - <<'PY' || exit 1
import sys

def parse(texto, ja_rodou=0):
    """Porta EXATA do laco de parse do .ps1."""
    novos = []
    for linha in texto.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        l = linha.strip()
        if l == "" or l.startswith("#"):
            continue
        i = l.find("|")
        if i <= 0:
            continue
        id_txt = l[:i].strip()
        cmd = l[i + 1:].strip()
        if cmd == "":
            continue
        try:
            nid = int(id_txt)
        except ValueError:
            continue
        # igual ao .ps1: id tem de ser >= 1, senao nunca passaria do
        # estado inicial 0 e viraria um comando fantasma.
        if nid < 1:
            continue
        if nid <= ja_rodou:
            continue
        novos.append((nid, cmd))
    return sorted(novos)

# o arquivo REAL do canal, no repo. Ele PODE ter comandos ativos -- isso eh
# normal e ate desejavel. O que nao pode eh o parser engasgar nele.
real = open("../canal/comandos.txt", encoding="utf-8").read()
r = parse(real)
for nid, cmd in r:
    assert nid >= 1, "canal real tem id < 1: %r" % nid
    assert cmd.strip() != "", "canal real tem comando vazio no id %d" % nid
print("  PASSA  canal real: parseia limpo, %d comando(s) ativo(s)" % len(r))

casos = [
    # (texto, ja_rodou, esperado)
    ("1|Get-Volume", 0, [(1, "Get-Volume")]),
    ("2|whoami", 1, [(2, "whoami")]),
    ("1|a\n2|b", 0, [(1, "a"), (2, "b")]),
    ("1|a\n2|b", 1, [(2, "b")]),            # ja rodou o 1
    ("1|a\n2|b", 2, []),                     # ja rodou os dois
    ("3|c\n1|a\n2|b", 0, [(1, "a"), (2, "b"), (3, "c")]),   # ordena por id
    ("# comentario\n\n1|a", 0, [(1, "a")]),  # ignora # e vazias
    ("1|", 0, []),                           # comando vazio
    ("1|   ", 0, []),                        # comando so espaco
    ("|a", 0, []),                           # id vazio
    ("abc|a", 0, []),                        # id nao numerico
    ("1|a|b", 0, [(1, "a|b")]),              # pipe dentro do comando eh do comando
    ("0|zero", 0, []),                       # id 0 NUNCA rodaria: fantasma
    ("-1|neg", 0, []),                       # id negativo idem
    ("1|a\n0|fantasma\n2|b", 0, [(1, "a"), (2, "b")]),  # fantasma nao atrapalha
    ("  1  |  espacado  ", 0, [(1, "espacado")]),
]
erros = []
for texto, ja, esp in casos:
    got = parse(texto, ja)
    if got != esp:
        erros.append("parse(%r, ja=%d) = %r, esperado %r" % (texto, ja, got, esp))
if erros:
    for e in erros:
        print("    " + e)
    sys.exit(1)
print("  PASSA  parser: %d casos corretos (ordenacao, dup, vazio, pipe)" % len(casos))
PY

echo "== gerador do cliente =="
CANAL="https://raw.githubusercontent.com/grasshopperconta-a11y/PS2Projects/arena/4c50659b-ps2projects/canal/comandos.txt"
python3 tools/remote/gerar_cliente.py --canal "$CANAL" \
    --saida "$TMP/pacote" >"$TMP/gen.log" 2>&1 || { cat "$TMP/gen.log"; falha "gerador rodou"; exit 1; }
ok "gerador rodou"

for f in iniciar-fnf-remote.cmd fnf-remote-client.ps1 LEIA-ME.txt; do
    if [ -f "$TMP/pacote/$f" ]; then ok "gerou $f"; else falha "faltou $f"; fi
done

# O defeito 2: a validacao do .cmd nao pode disparar com endereco real.
if grep -q "@@CANAL@@" "$TMP/pacote/iniciar-fnf-remote.cmd"; then
    falha "ainda existe marcador @@CANAL@@ no .cmd gerado"
else
    ok "nenhum marcador sobrou no .cmd"
fi

if grep -qF "FNF_CANAL=$CANAL" "$TMP/pacote/iniciar-fnf-remote.cmd"; then
    ok "endereco real do canal embutido no .cmd"
else
    falha "endereco do canal nao foi embutido"
fi

# a checagem findstr /b http tem de PASSAR com o endereco real
if printf '%s\n' "$CANAL" | grep -q '^http'; then
    ok "validacao do endereco nao dispara com endereco real"
else
    falha "validacao do endereco dispararia"
fi

# e TEM de disparar com um endereco quebrado
if printf '%s\n' "nao-e-url" | grep -q '^http'; then
    falha "validacao deixou passar endereco quebrado"
else
    ok "validacao pega endereco quebrado"
fi

echo "== nada de servidor nem senha =="
# A versao anterior expunha um servidor meu numa URL publica. O proxy do e2b
# respondeu 502 "Sandbox not found" para o usuario. Nada de porta, nada de
# token: se voltar, o teste quebra de proposito.
if grep -qiE "8791|e2b\.app|X-Token|FNF_TOKEN" "$TMP/pacote/fnf-remote-client.ps1" \
   || grep -qiE "8791|e2b\.app|X-Token|FNF_TOKEN" "$TMP/pacote/iniciar-fnf-remote.cmd"; then
    falha "voltou referencia a servidor/porta/senha -- o canal publico nao precisa"
else
    ok "nenhuma referencia a servidor, porta ou senha"
fi

echo "== sintaxe do PowerShell =="
# O cliente foi entregue UMA VEZ com erro de sintaxe, e so descobrimos quando
# o usuario rodou: uma string quebrada em duas linhas com '+', que o parser
# do PowerShell trata como fim de instrucao (MissingEndParenthesis).
#
# Nao tenho PowerShell aqui, entao checa_ps1.py faz uma verificacao
# ESTRUTURAL. O ponto do teste eh duplo: tem de passar no arquivo bom E
# falhar numa copia com o bug original.
python3 -m py_compile tools/remote/gerar_cliente.py && ok "gerar_cliente.py compila"

if python3 tools/remote/checa_ps1.py tools/remote/fnf-remote-client.ps1 >"$TMP/ps1.log" 2>&1; then
    ok "cliente .ps1 passa na verificacao estrutural"
else
    falha "cliente .ps1 tem problema de sintaxe" "$(cat "$TMP/ps1.log")"
fi

# e a verificacao tem de pegar o bug que escapou
cat > "$TMP/quebrado.ps1" <<'PS'
$atingiu = 'system32'
if ($atingiu) {
    $txt = ("RECUSADO: area protegida "
            + "(System32). Nada foi executado." -f $atingiu)
    continue
}
PS
if python3 tools/remote/checa_ps1.py "$TMP/quebrado.ps1" >"$TMP/ps1b.log" 2>&1; then
    falha "a verificacao NAO pegou a quebra de string -- o teste eh inutil" "$(cat "$TMP/ps1b.log")"
else
    if grep -q "MissingEndParenthesis" "$TMP/ps1b.log"; then
        ok "a verificacao pega a quebra de string que escapou"
    else
        falha "pegou algo, mas nao a quebra de string" "$(cat "$TMP/ps1b.log")"
    fi
fi

echo "== robustez: o cliente nao pode travar nem morrer =="
# Dois defeitos reais, os dois entregues ao usuario:
#
#  1. stdout vazia -> Get-Content -Raw devolve $null -> GetByteCount estoura
#     ArgumentNullException. Aconteceu no comando #4 (dir de pasta inexistete:
#     o cmd escreve o erro no stderr e nao escreve nada na stdout).
#
#  2. pior: o marca-como-rodado ficava no FIM do bloco. A excecao estourou
#     antes dele, o .cmd reabriu o cliente, e ele tentou o MESMO comando para
#     sempre. O usuario viu a mesma cachoeira de erro repetindo sem parar e o
#     canal ficou travado de forma permanente.
#
# Nao tenho PowerShell aqui, entao estas sao verificacoes ESTRUTURAIS sobre o
# fonte: a ordem dos comandos e a existencia do try/catch.
python3 - <<'PY' || exit 1
import re, sys
src = open("tools/remote/fnf-remote-client.ps1", encoding="utf-8").read()
erros = []

# (a) Set-JaRodou TEM de aparecer antes do Start-Process, dentro do foreach.
i_foreach = src.find("foreach ($job in $novos)")
i_set = src.find("Set-JaRodou $id", i_foreach)
i_start = src.find("Start-Process", i_foreach)
if i_foreach < 0 or i_set < 0 or i_start < 0:
    erros.append("nao achei foreach / Set-JaRodou / Start-Process")
else:
    if i_set > i_start:
        erros.append("Set-JaRodou vem DEPOIS do Start-Process: uma excecao "
                     "no meio trava o canal para sempre (foi o bug do #4)")
    else:
        print("  PASSA  marca como rodado ANTES de executar (canal nao trava)")

# (b) tem de existir try/catch envolvendo a execucao, e o catch nao pode
#     deixar morrer: ele registra o erro como resultado.
i_try = src.find("try {", i_foreach)
i_catch = src.find("} catch {", i_foreach)
if i_try < 0 or i_catch < 0:
    erros.append("nao achei try/catch dentro do foreach")
else:
    if i_catch < i_start:
        erros.append("o catch vem antes do Start-Process: nao protege a execucao")
    else:
        print("  PASSA  execucao protegida por try/catch (cliente nao morre)")

# (c) a normalizacao de nulo tem de existir. Get-Content -Raw devolve $null
#     em arquivo vazio, e $null quebrou GetByteCount.
if "if ($null -eq $txtOut) { $txtOut = '' }" not in src:
    erros.append("falta normalizar $txtOut para '' -- $null quebra GetByteCount")
else:
    print("  PASSA  saida vazia normalizada (Get-Content -Raw devolve $null)")

# (d) o catch tem de gravar resultado, para eu ver o erro mesmo se explodir
if "erro do cliente" not in src:
    erros.append("o catch nao registra resultado: eu ficaria sem saber do erro")
else:
    print("  PASSA  catch registra o erro como resultado")

if erros:
    for e in erros:
        print("    " + e)
    sys.exit(1)
PY

echo "== o canal committado eh bem formado =="
# ids tem de ser numeros e nao repetidos, senao o cliente pula ou repete
python3 - <<'PY' || exit 1
import re, sys
ids = []
for linha in open("../canal/comandos.txt", encoding="utf-8").read().splitlines():
    l = linha.strip()
    if not l or l.startswith("#"):
        continue
    # diretiva '@volta <url>' nao eh comando: eh configuracao do canal de volta.
    # Ignorada aqui (e tambem pelo cliente, que nao ve '|' na linha).
    if l.startswith("@"):
        continue
    i = l.find("|")
    if i <= 0:
        print("    linha sem '<id>|': %r" % l); sys.exit(1)
    t = l[:i].strip()
    if not re.fullmatch(r"[1-9][0-9]*", t):
        print("    id tem de ser inteiro >= 1: %r" % t); sys.exit(1)
        print("    id nao eh numero: %r" % t); sys.exit(1)
    ids.append(int(t))
if len(ids) != len(set(ids)):
    print("    ids repetidos: %r" % ids); sys.exit(1)
print("  PASSA  canal: %d comando(s), ids unicos e numericos" % len(ids))
PY

echo "== canal de volta: publicacao automatica da saida =="
python3 - <<'PY' || exit 1
import re, sys
src = open("tools/remote/fnf-remote-client.ps1", encoding="utf-8").read()
erros = []

# (e) a funcao de publicar tem de existir e nao pode deixar escapar erro: se o
#     servico estiver fora do ar, o cliente tem de continuar vivo. Um erro de
#     rede nunca pode matar o programa.
i_func = src.find("function Publicar-Volta")
if i_func < 0:
    erros.append("nao existe Publicar-Volta: a saida nao voltaria para mim")
else:
    corpo = src[i_func:src.find("\n}", i_func)]
    if "try {" not in corpo or "catch" not in corpo:
        erros.append("Publicar-Volta nao tem try/catch: falha de rede mataria o cliente")
    else:
        print("  PASSA  Publicar-Volta existe e engole falha de rede")

# (f) a diretiva '@volta' tem de ser lida do canal -- assim o endereco pode ser
#     trocado sem reinstalar o programa.
if "StartsWith('@volta ')" not in src:
    erros.append("o cliente nao le a diretiva '@volta' do canal")
else:
    print("  PASSA  diretiva @volta lida do canal (endereco trocavel sem reinstalar)")

# (g) a publicacao tem de acontecer DEPOIS de gravar o resultado.
i_setcontent = src.find("Set-Content -LiteralPath $arqRel")
i_pub = src.find("Publicar-Volta $Volta $corpo", i_setcontent)
if i_setcontent < 0 or i_pub < 0 or i_pub < i_setcontent:
    erros.append("Publicar-Volta nao eh chamado depois de gravar resultado-<id>.txt")
else:
    print("  PASSA  publica a saida depois de gravar o resultado")

# (h) tem de publicar em TODOS os caminhos: normal, RECUSADO e erro do cliente.
#     Se faltar um, eu fico cego exatamente no caso que preciso ver.
if src.count("Publicar-Volta $Volta") < 3:
    erros.append("Publicar-Volta so eh chamado em alguns caminhos: precisa ser "
                 "no normal, no RECUSADO e no erro do cliente")
else:
    print("  PASSA  publica em todos os caminhos (normal, RECUSADO, erro)")

# (i) o endereco do canal de volta NAO pode estar gravado no cliente. Se
#     estivesse, o nome vazaria dentro do ZIP, que qualquer um pode baixar.
urls = re.findall(r"https?://[^\s'\"]+", src)
if any(("ntfy" in u or "npoint" in u) for u in urls):
    erros.append("endereco do canal de volta estah gravado no cliente: vazaria no ZIP")
else:
    print("  PASSA  endereco do canal de volta nao estah no cliente (vem do canal)")

# (j) o corpo tem de ir como bytes UTF-8 e SEM ContentType. O experimento #52
#     provou as tres variantes com acento de verdade:
#       A1 string, sem ContentType        -> ANEXO (charset=iso-8859-1)
#       A2 bytes UTF-8, sem ContentType   -> MENSAGEM
#       A3 string, ContentType text/plain -> ANEXO (charset=iso-8859-1)
#     Declarar ContentType nao salva: o Invoke-WebRequest manda <string> como
#     ISO-8859-1, o padrao do Windows. So byte[] em UTF-8 chega como texto.
if "GetBytes($corpo)" not in src:
    erros.append("corpo nao eh convertido para bytes UTF-8: resultado com "
                 "acento vira anexo no ntfy e eu nao leio")
else:
    print("  PASSA  corpo convertido para bytes UTF-8 antes de publicar")
if "-ContentType" in src[src.find("function Publicar-Volta"):]:
    erros.append("Publicar-Volta declara ContentType: o experimento #52 provou "
                 "que isso faz o ntfy guardar como ANEXO em vez de mensagem")
else:
    print("  PASSA  publica sem ContentType (experimento #52: A2 era o unico que chegava)")

# (k) modo 'ultimo': so o comando mais novo roda, o resto da fila eh
#     abandonado. Sem isso, um lote publicado de uma vez despeja tudo em
#     cascata e o programa fica em loop.
if "StartsWith('@modo ')" not in src:
    erros.append("o cliente nao le a diretiva '@modo': nao dah para eu "
                 "escolher entre fila e ultimo sem reinstalar")
else:
    print("  PASSA  diretiva @modo lida do canal")
if "Measure-Object -Property id -Maximum" not in src:
    erros.append("modo 'ultimo' nao seleciona o maior id: a fila continuaria "
                 "despejando tudo em cascata")
else:
    print("  PASSA  modo 'ultimo' seleciona so o comando mais novo")

if erros:
    for e in erros:
        print("    " + e)
    sys.exit(1)
PY

echo ""
echo "remote: $PASS passaram, $FAIL falharam"
[ "$FAIL" -eq 0 ]
