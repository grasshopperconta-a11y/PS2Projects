#!/usr/bin/env bash
# ============================================================
#  FNF REMOTE - iniciar (WSL / Ubuntu)
# ============================================================
#  Rode:  bash iniciar-fnf-remote.sh
#
#  Ele:
#    1. confere que python3 existe
#    2. aponta para o canal de comandos
#    3. abre o cliente
#    4. se o cliente fechar ou der erro, ESPERA 3s e ABRE DE NOVO
#
#  Fechar e reabrir volta a funcionar EXATAMENTE igual, e NAO repete os
#  comandos que ja rodaram: o ultimo id fica guardado em estado.id.
#
#  NAO PRECISA DE SENHA. O canal eh um arquivo publico do GitHub:
#  qualquer pessoa pode LE-lo, so eu posso escrever.
# ============================================================

set -u

FNF_CANAL="@@CANAL@@"

# ------------------------------------------------------------
#  Validacao: o endereco tem de comecar com http.
# ------------------------------------------------------------
case "$FNF_CANAL" in
    http*)
        ;;
    *)
        echo "ERRO: endereco do canal nao parece valido: $FNF_CANAL"
        echo "Peca um novo iniciar-fnf-remote.sh -- este nao foi gerado direito."
        exit 2
        ;;
esac

# ------------------------------------------------------------
#  python3 eh o unico requisito. Ja vem no Ubuntu do WSL.
# ------------------------------------------------------------
if ! command -v python3 >/dev/null 2>&1; then
    echo "ERRO: python3 nao encontrado."
    echo "Instale com:  sudo apt update && sudo apt install -y python3"
    exit 3
fi

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo
echo "  FNF REMOTE (WSL) iniciando..."
echo "  canal: $FNF_CANAL"
echo "  pasta: $AQUI"
echo
echo "  Deixe esta janela ABERTA. Feche-a so quando quiser parar."
echo "  Se o cliente fechar sozinho, ele reabre em 3 segundos."
echo "  Nao precisa de senha: o canal eh publico para leitura."
echo

# ------------------------------------------------------------
#  Laco de reabertura. Se o cliente morrer, volta em 3s.
# ------------------------------------------------------------
while true; do
    python3 "$AQUI/fnf-remote-wsl.py" --canal "$FNF_CANAL" --dir "$AQUI"
    echo
    echo "  [$(date +%H:%M:%S)] cliente encerrou. reabrindo em 3 segundos..."
    sleep 3
done
