#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o pacote do cliente para o usuario: o .cmd com endereco e senha ja
preenchidos, mais o LEIA-ME. Nada de marcador para ele ter que editar.

    python3 gerar_cliente.py --ponte https://xxxx.e2b.app --token ABC123 \
        --saida /tmp/pacote_cliente
"""

import argparse
import os
import shutil
import stat

AQUI = os.path.dirname(os.path.abspath(__file__))

LEIAME = """FNF REMOTE - COMO USAR
======================

O QUE EH ISTO
-------------
Um programa que fica aberto no seu PC e me deixa rodar comandos nele,
recebendo a resposta de volta. Serve para eu montar o pendrive, conferir
se os arquivos estao no lugar certo e ler os logs do jogo sem voce ter que
ficar me explicando o que ve na tela.

NAO PRECISA INSTALAR NADA. Usa so o PowerShell que ja vem no Windows.

COMO LIGAR
----------
1. Descompacte esta pasta em qualquer lugar (Documentos, por exemplo).
   Os tres arquivos tem de ficar JUNTOS na mesma pasta:

       iniciar-fnf-remote.cmd
       fnf-remote-client.ps1
       LEIA-ME.txt

2. De DOIS CLIQUES em "iniciar-fnf-remote.cmd".

3. ANTES DE MAIS NADA, teste se o canal esta vivo: abra no seu navegador

       @@PONTE@@/health

   Se aparecer algo como {"ok": true, ...} -- funciona, pode seguir.
   Se der erro de pagina, me avise: eu regero o programa com endereco novo.

4. De DOIS CLIQUES em "iniciar-fnf-remote.cmd".

5. Vai abrir uma janela preta. DEIXE ABERTA. Ela mostra:

       FNF REMOTE - cliente
       ponte : https://...
       trava : System32 / Windows = NUNCA executa

Quando eu mandar um comando, aparece uma linha verde com o comando e,
depois, o resultado. Se nao aparecer nada por minutos, eh normal: eu so
mando comando quando preciso.

SE FECHAR E REABRIR
-------------------
Fecha e da dois cliques de novo. Ele volta a funcionar EXATAMENTE igual --
mesmo endereco, mesma senha. Nao precisa me pedir nada novo.

Para comecar sozinho quando voce ligar o PC (opcional):
   1. aperte a tecla do Windows, digite "Agendador de Tarefas", abra
   2. "Criar Tarefa Basica"
   3. Nome: FNF Remote
   4. Gatilho: "Ao iniciar o computador"
   5. Acao: "Iniciar um programa"
   6. Programa: o caminho COMPLETO do iniciar-fnf-remote.cmd
   7. marque "Executar apenas quando o usuario estiver conectado"

SEGURANCA - LEIA, EH IMPORTANTE
-------------------------------
Este programa abre uma porta para o seu PC. Verdades:

* So funciona com a SENHA, que esta dentro do iniciar-fnf-remote.cmd.
  Sem ela, a ponte nao entrega comando nenhum. Quem tentar entra sem
  senha recebe "token invalido" e nao acontece nada.

* A URL da ponte so existe ENQUANTO EU ESTIVER TRABALHANDO com voce.
  Quando eu encerrar a sessao, ela morre e o programa para de receber
  comandos. Nao eh um acesso permanente, e nao adianta deixar ligado
  de um dia para o outro esperando que eu apareca. Quando eu voltar,
  eu te mando um programa novo com endereco novo -- o anterior fica
  inutilizado sozinho.

* VOCE VE TUDO: cada comando aparece na janela preta, antes de rodar.
  Se aparecer algo que voce nao reconhece, feche a janela na hora.

* A trava de System32 fica no SEU PC, dentro do cliente, antes de qualquer
  coisa. Um comando que tente mexer em System32, SysWOW64 ou na pasta
  Windows NAO executa: ele devolve codigo 99 e me diz que foi recusado.
  Nao eh aviso -- ele realmente nao roda.

* Isso nao substitui antivirus nem cuidado. Se um dia voce nao confiar no
  que esta rodando, feche a janela e me avise.

QUANDO EU USO ISSO
------------------
Montar e conferir o pendrive, ver onde o jogo gravou o log, e ler o log de
volta. Nada alem disso.

PARA PARAR
----------
Feche a janela preta. Pronto. Se criar a tarefa agendada, apague a tarefa
tambem.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ponte", required=True)
    ap.add_argument("--token", required=True)
    ap.add_argument("--saida", required=True)
    args = ap.parse_args()

    os.makedirs(args.saida, exist_ok=True)

    # .cmd com os valores de verdade
    with open(os.path.join(AQUI, "iniciar-fnf-remote.cmd.template"),
              encoding="utf-8") as f:
        tpl = f.read()
    if "@@PONTE@@" not in tpl or "@@TOKEN@@" not in tpl:
        raise SystemExit("template sem marcador")
    cmd = tpl.replace("@@PONTE@@", args.ponte).replace("@@TOKEN@@", args.token)
    dst = os.path.join(args.saida, "iniciar-fnf-remote.cmd")
    with open(dst, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(cmd)
    os.chmod(dst, os.stat(dst).st_mode | stat.S_IEXEC)

    shutil.copy2(os.path.join(AQUI, "fnf-remote-client.ps1"),
                 os.path.join(args.saida, "fnf-remote-client.ps1"))
    with open(os.path.join(args.saida, "LEIA-ME.txt"), "w",
              encoding="utf-8", newline="\r\n") as f:
        f.write(LEIAME)

    print("pacote em %s" % args.saida)
    for n in sorted(os.listdir(args.saida)):
        print("   %-28s %d bytes" % (n, os.path.getsize(os.path.join(args.saida, n))))
    # o token nao pode vazar no log
    print("   ponte : %s" % args.ponte)
    print("   token : (%d caracteres, nao mostrado)" % len(args.token))


if __name__ == "__main__":
    main()
