#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o pacote do cliente WSL para o usuario: o .sh com o endereco do canal
ja preenchido, mais o LEIA-ME. Nada de marcador para ele ter que editar.

    python3 gerar_cliente_wsl.py --canal https://raw.githubusercontent.com/.../comandos-wsl.txt \
        --saida /tmp/pacote_wsl
"""

import argparse
import os
import shutil
import stat

AQUI = os.path.dirname(os.path.abspath(__file__))

LEIAME = """FNF REMOTE (WSL/Ubuntu) - COMO USAR
=================================

O QUE EH ISTO
-------------
A mesma coisa que o cliente do Windows, so que rodando dentro do WSL, no
Ubuntu. Ele fica aberto no seu PC e me deixa rodar comandos ali, recebendo a
saida de volta.

A diferenca pratica eh grande: aqui eu tenho o bash, o git, o gcc, o make e
(quando instalarmos) o toolchain do PS2. Ou seja: eu consigo COMPILAR o jogo
e RODAR A SUITE no seu PC, durante o meu raciocinamento, sem voce ter que
fazer nada. Quando eu precisar saber se uma mudanca minha compila, eu mando o
comando e leio o resultado na hora.

NAO PRECISA INSTALAR NADA. Python 3 e bash ja vem no Ubuntu do WSL.
NAO PRECISA DE SENHA.

ANTES DE COMECAR - O WSL TEM DE ESTAR INSTALADO
-----------------------------------------------
Se voce ainda nao tem o WSL, abra o PowerShell como ADMINISTRADOR e rode:

    wsl --install -d Ubuntu

Reinicie o PC quando ele pedir. Na primeira vez ele vai pedir um nome de
usuario e uma senha para o Linux -- isso eh so do Ubuntu, invente voce mesmo.

Para conferir se esta tudo certo, no PowerShell:

    wsl -l -v

Tem de aparecer o Ubuntu com versao 2.

COMO LIGAR
----------
1. Descompacte esta pasta em qualquer lugar.
   Os arquivos tem de ficar JUNTOS na mesma pasta:

       iniciar-fnf-remote.sh
       fnf-remote-wsl.py
       LEIA-ME.txt

2. Abra o terminal do Ubuntu (o icone do Ubuntu, no menu Iniciar) e rode:

       bash /caminho/completo/iniciar-fnf-remote.sh

   Dica: se a pasta esta em Downloads do Windows, o caminho no Ubuntu eh
   /mnt/c/Users/SEU_USUARIO/Downloads/...

3. Deixe a janela ABERTA.

COMO EU RECEBO A SAIDA
----------------------
Eu mando o comando, o programa executa, PUBLICA a saida num servico de
mensagens, e eu leio na hora. Voce nao precisa fazer NADA.

O endereco desse servico NAO fica dentro do programa. Ele vem do proprio
canal de comandos, numa linha '@volta <endereco>'. Se um dia vazar, eu troco
a linha no canal e o programa passa a usar o novo sozinho.

E nao ha risco por essa porta: ela eh so de saida. O canal de COMANDOS
continua sendo o arquivo do GitHub, que so eu escrevo. Quem descobrisse o
endereco de volta no maxo conseguiria publicar resultado falso -- nao
consegue escrever comandos.

E UM CANAL SEPARADO DO DO WINDOWS
---------------------------------
De proposito. Este cliente le 'comandos-wsl.txt' e publica num topico proprio;
o cliente do Windows le 'comandos.txt'. Assim um comando meu nunca roda nos
dois lugares ao mesmo tempo, e eu sei de qual maquina veio cada resposta.
Os dois podem ficar ligados juntos sem problema.

O QUE EU NAO CONSIGO FAZER (e a trava fica no SEU PC)
-----------------------------------------------------
Antes de qualquer execucao o programa recusa comandos que mencionem areas
protegidas: System32, SysWOW64, WinSxS, /etc, /boot, /dev, mkfs, dd em
dispositivo, desligar/reiniciar, criar usuario, mudar senha, firewall, e
fork bombs. Nao eh aviso -- ele realmente nao executa, devolve codigo de
recusa e salva o resultado dizendo que foi recusado.

VOCE VE TUDO
------------
Cada comando aparece na tela ANTES de rodar, em verde. Se aparecer algo que
voce nao reconheca, feche a janela na hora e me avise.

ONDE FICAM OS RESULTADOS
------------------------
Em 'resultados/resultado-<id>.txt' dentro da pasta do cliente. La esta a
saida COMPLETA, sem cortes -- o que eu lego eh um resumo, porque o servico de
mensagens nao aceita texto muito grande.

PARA PARAR
----------
Feche a janela do terminal. Pronto.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--canal", required=True)
    ap.add_argument("--saida", required=True)
    args = ap.parse_args()

    os.makedirs(args.saida, exist_ok=True)

    with open(os.path.join(AQUI, "iniciar-fnf-remote.sh"),
              encoding="utf-8") as f:
        tpl = f.read()
    if "@@CANAL@@" not in tpl:
        raise SystemExit("template sem marcador @@CANAL@@")
    sh = tpl.replace("@@CANAL@@", args.canal)
    dst = os.path.join(args.saida, "iniciar-fnf-remote.sh")
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(sh)
    os.chmod(dst, os.stat(dst).st_mode | stat.S_IEXEC)

    shutil.copy2(os.path.join(AQUI, "fnf-remote-wsl.py"),
                 os.path.join(args.saida, "fnf-remote-wsl.py"))
    with open(os.path.join(args.saida, "LEIA-ME.txt"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write(LEIAME)

    print("pacote WSL em %s" % args.saida)
    for n in sorted(os.listdir(args.saida)):
        print("   %-26s %d bytes"
              % (n, os.path.getsize(os.path.join(args.saida, n))))
    print("   canal : %s" % args.canal)


if __name__ == "__main__":
    main()
