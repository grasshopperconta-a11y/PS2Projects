#!/usr/bin/env bash
# ============================================================
#  FNF - AGENTE DA PONTE SINCRONA
# ============================================================
#  Rode:  bash iniciar-ponte.sh
#
#  O que isso muda em relacao ao cliente anterior: aquele era assincrono.
#  Eu publicava um comando, o seu PC poleava, executava, respondia -- e
#  ALGUEM precisava colar a resposta de volta. Nao dava para eu mandar e
#  receber na mesma mensagem.
#
#  Este agente poleia um servidor que eu mantenho de pe. Quando eu mando um
#  comando, ele executa no seu bash e devolve a saida. Eu leio a resposta
#  DENTRO do mesmo turno. A latencia medida da ponte eh de ~0,4 s.
#
#  NAO PRECISA INSTALAR NADA. Python 3 e bash ja vem no Ubuntu do WSL.
#  NAO PRECISA DE SENHA. NAO abre porta no seu PC: quem conecta eh ele.
#
#  Deixe esta janela ABERTA. Feche so quando quiser parar.
# ============================================================

set -u

SERVIDOR="@@SERVIDOR@@"

case "$SERVIDOR" in
    http*)
        ;;
    *)
        echo "ERRO: endereco do servidor nao parece valido: $SERVIDOR"
        echo "Peca um iniciar-ponte.sh novo -- este nao foi gerado direito."
        exit 2
        ;;
esac

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERRO: python3 nao encontrado."
    echo "Instale com:  sudo apt update && sudo apt install -y python3"
    exit 3
fi

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo
echo "  FNF - agente da ponte sincrona"
echo "  servidor: $SERVIDOR"
echo "  pasta   : $AQUI"
echo
echo "  Deixe esta janela ABERTA. Feche-a so quando quiser parar."
echo "  Nao precisa de senha."
echo

# ------------------------------------------------------------
#  Laco de reabertura. Se o agente morrer, volta em 3 s.
#  Rede oscilando nao derruba nada: o proprio agente trata isso.
# ------------------------------------------------------------
while true; do
    python3 "$AQUI/sync_agent.py" --servidor "$SERVIDOR"
    echo
    echo "  agente fechou. reabrindo em 3 s..."
    sleep 3
done
