#!/bin/sh
# Testes da ponte de comando remoto.
#
# Dois defeitos reais jah aconteceram aqui e estao cobertos:
#
#  1. O template do .cmd comparava %FNF_PONTE% com @@PONTE@@. Depois de
#     substituir o endereco real, a comparacao ficou "endereco == endereco"
#     e portanto VERDADEIRA -- o programa dava erro e saida em TODO uso.
#     O teste agora gera o .cmd e confirma que a validacao nao dispara.
#
#  2. A trava de System32 tinha 'winssxs' onde a pasta real eh 'WinSxS'
#     (lowercase 'winsxs'). Um comando em WinSxS passava. O teste cobre.
set -e
cd "$(dirname "$0")/.."

PASS=0; FAIL=0
ok()   { PASS=$((PASS+1)); echo "  PASSA  $1"; }
falha(){ FAIL=$((FAIL+1)); echo "  FALHA  $1"; }
checa(){ if [ "$2" = "$3" ]; then ok "$1"; else falha "$1 (esperado '$3', veio '$2')"; fi; }

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

echo "== trava de System32 =="
# replica EXATAMENTE a normalizacao de Test-Protegido no .ps1:
#   minusculo, sem espacos, barra normalizada
python3 - "$TMP" <<'PY' || exit 1
import sys, re, os
TMP = sys.argv[1]
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

echo "== gerador do cliente =="
PONTE="https://8791-testetestetestetestetestetesteteste.e2b.app"
TOKEN="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
python3 tools/remote/gerar_cliente.py --ponte "$PONTE" --token "$TOKEN" \
    --saida "$TMP/pacote" >"$TMP/gen.log" 2>&1 || { cat "$TMP/gen.log"; falha "gerador rodou"; exit 1; }
ok "gerador rodou"

for f in iniciar-fnf-remote.cmd fnf-remote-client.ps1 LEIA-ME.txt; do
    if [ -f "$TMP/pacote/$f" ]; then ok "gerou $f"; else falha "faltou $f"; fi
done

# O defeito 1: a validacao do .cmd nao pode disparar com endereco real.
if grep -q "@@PONTE@@" "$TMP/pacote/iniciar-fnf-remote.cmd"; then
    falha "ainda existe marcador @@PONTE@@ no .cmd gerado"
else
    ok "nenhum marcador sobrou no .cmd"
fi

if grep -qF "FNF_PONTE=$PONTE" "$TMP/pacote/iniciar-fnf-remote.cmd"; then
    ok "endereco real embutido no .cmd"
else
    falha "endereco nao foi embutido"
fi

# a checagem findstr /b http tem de PASSAR com o endereco real
if printf '%s\n' "$PONTE" | grep -q '^http'; then
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

if grep -q "$TOKEN" "$TMP/pacote/iniciar-fnf-remote.cmd"; then
    ok "senha embutida no .cmd (so o programa do usuario a tem)"
else
    falha "senha nao foi embutida"
fi

echo "== sintaxe =="
python3 -m py_compile tools/remote/remote_bridge.py && ok "remote_bridge.py compila"
python3 -m py_compile tools/remote/gerar_cliente.py  && ok "gerar_cliente.py compila"

echo "== ponte: ciclo completo com autenticacao =="
PORTA=18931
python3 tools/remote/remote_bridge.py --porta $PORTA >"$TMP/ponte.log" 2>&1 &
PID=$!
trap 'kill $PID 2>/dev/null; rm -rf "$TMP"' EXIT
i=0
while [ $i -lt 40 ]; do
    curl -s -m 2 "http://127.0.0.1:$PORTA/health" >/dev/null 2>&1 && break
    i=$((i+1)); sleep 0.25
done
if [ $i -ge 40 ]; then cat "$TMP/ponte.log"; falha "ponte subiu"; else ok "ponte subiu na porta $PORTA"; fi

TC=$(cat tools/remote/estado/token_cliente)
TO=$(cat tools/remote/estado/token_operador)
B="http://127.0.0.1:$PORTA"

r=$(curl -s -X POST $B/poll -H 'Content-Type: application/json' -d '{}')
checa "cliente sem senha recusado" "$r" '{"erro": "token invalido"}'

r=$(curl -s -X POST $B/poll -H 'Content-Type: application/json' -H "X-Token: errada" -d '{}')
checa "cliente com senha errada recusado" "$r" '{"erro": "token invalido"}'

r=$(curl -s -X POST $B/op/job -H 'Content-Type: application/json' -d '{"cmd":"x"}')
checa "operador sem token recusado" "$r" '{"erro": "token de operador invalido"}'

r=$(curl -s -X POST $B/op/job -H 'Content-Type: application/json' -H "X-Op: $TC" -d '{"cmd":"x"}')
checa "operador com token de cliente recusado" "$r" '{"erro": "token de operador invalido"}'

r=$(curl -s -X POST $B/op/job -H 'Content-Type: application/json' -H "X-Op: $TO" -d '{"cmd":"echo teste-remoto","tempo_limite":30}')
case "$r" in *'"ok": true'*) ok "job enfileirado" ;; *) falha "job enfileirado ($r)" ;; esac
JID=$(printf '%s' "$r" | sed -n 's/.*"id": \([0-9]*\).*/\1/p')

r=$(curl -s -X POST $B/poll -H 'Content-Type: application/json' -H "X-Token: $TC" -d '{}')
case "$r" in *echo\ teste-remoto*) ok "cliente recebe o job" ;; *) falha "cliente recebeu '$r'" ;; esac

r=$(curl -s -X POST $B/poll -H 'Content-Type: application/json' -H "X-Token: $TC" -d '{}')
case "$r" in *'"cmd": null'*) ok "fila vazia devolve null" ;; *) falha "fila vazia ($r)" ;; esac

curl -s -X POST $B/done -H 'Content-Type: application/json' -H "X-Token: $TC" \
    -d '{"id":'"$JID"',"rc":0,"out":"teste-remoto\n","err":""}' >/dev/null
r=$(curl -s "$B/op/resultado?id=$JID" -H "X-Op: $TO")
case "$r" in *teste-remoto*) ok "operador le o resultado" ;; *) falha "operador leu '$r'" ;; esac

kill $PID 2>/dev/null || true
wait $PID 2>/dev/null || true
trap 'rm -rf "$TMP"' EXIT

echo ""
echo "remote: $PASS passaram, $FAIL falharam"
[ "$FAIL" -eq 0 ]
