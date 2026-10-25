#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o pacote do cliente para o usuario: o .cmd com o endereco do canal
ja preenchido, mais o LEIA-ME. Nada de marcador para ele ter que editar.

    python3 gerar_cliente.py --canal https://raw.githubusercontent.com/.../comandos.txt \
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
recebendo a saida de volta. Serve para eu montar o pendrive, conferir se os
arquivos estao no lugar certo e ler os logs do jogo sem voce ter que ficar
me explicando o que ve na tela.

NAO PRECISA INSTALAR NADA. Usa so o PowerShell que ja vem no Windows.
NAO PRECISA DE SENHA.

COMO FUNCIONA A SEGURANCA (leia, eh rapido)
-------------------------------------------
O canal de comandos eh um ARQUIVO PUBLICO do GitHub. Isso eh de proposito:

  * qualquer pessoa pode LE-lo -- inclusive voce, inclusive um curioso;
  * so EU posso escrever nele -- o repo eh meu e so eu tenho a chave.

Ou seja: quem descobrir o endereco ve os mesmos comandos que voce ve, e nao
consegue mandar nada. O pior caso possivel eh alguem ler a lista de comandos
que eu te mandei. Nada alem disso.

E a trava de System32 fica no SEU PC, dentro do programa, antes de qualquer
execucao. Um comando que tente mexer em System32, SysWOW64 ou WinSxS NAO
executa: ele devolve codigo 99, salva o resultado dizendo que foi recusado,
e nao roda. Nao eh aviso -- ele realmente nao roda.

COMO LIGAR
----------
1. Descompacte esta pasta em qualquer lugar (Documentos, por exemplo).
   Os arquivos tem de ficar JUNTOS na mesma pasta:

       iniciar-fnf-remote.cmd
       fnf-remote-client.ps1
       LEIA-ME.txt

2. De DOIS CLIQUES em "iniciar-fnf-remote.cmd".

3. Vai abrir uma janela preta. DEIXE ABERTA. Ela mostra:

       FNF REMOTE - cliente (canal GitHub)
       canal : https://raw.githubusercontent.com/...
       trava : System32 / Windows = NUNCA executa
       saida : ...\\resultados

Quando eu mando um comando, aparece uma linha VERDE com o comando e, depois,
o resultado. Se nao aparecer nada por minutos, eh normal: eu so mando comando
quando preciso.

COMO EU RECEBO A SAIDA
----------------------
Cada comando gera um arquivo em `resultados\\`, com este formato:

    resultado-1.txt
    resultado-2.txt
    ...

Dentro vem o comando, a data, o codigo de saida, a saida e os erros.

Para me entregar: ARRASTE A PASTA `resultados` PARA O GOOGLE DRIVE
(pelo navegador, como se fosse subir qualquer arquivo). Eu leio de la.

Se a saida for curta, voce tambem pode so copiar o que apareceu na janela
preta e colar aqui -- as duas formas funcionam.

SE FECHAR E REABRIR
-------------------
Fecha e da dois cliques de novo. Ele volta a funcionar EXATAMENTE igual, e
NAO repete os comandos que ja rodou: o programa guarda o numero do ultimo.
Nao precisa me pedir nada novo.

Para comecar sozinho quando voce ligar o PC (opcional):
   1. aperte a tecla do Windows, digite "Agendador de Tarefas", abra
   2. "Criar Tarefa Basica"
   3. Nome: FNF Remote
   4. Gatilho: "Ao iniciar o computador"
   5. Acao: "Iniciar um programa"
   6. Programa: o caminho COMPLETO do iniciar-fnf-remote.cmd
   7. marque "Executar apenas quando o usuario estiver conectado"

QUANTO TEMPO DEMORA
-------------------
O programa consulta o canal a cada 5 segundos. Porem o GitHub usa uma rede
de cache (CDN) na frente do arquivo, entao as vezes ele pode levar alguns
minutos para ver um comando novissimo. Se eu mandar algo e nao acontecer
nada, espere um pouco -- nao precisa fazer nada.

VOCE VE TUDO
------------
Cada comando aparece na janela preta ANTES de rodar. Se aparecer algo que
voce nao reconhece, feche a janela na hora e me avise.

PARA PARAR
----------
Feche a janela preta. Pronto. Se criou a tarefa agendada, apague a tarefa
tambem.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--canal", required=True)
    ap.add_argument("--saida", required=True)
    args = ap.parse_args()

    os.makedirs(args.saida, exist_ok=True)

    # .cmd com o endereco de verdade
    with open(os.path.join(AQUI, "iniciar-fnf-remote.cmd.template"),
              encoding="utf-8") as f:
        tpl = f.read()
    if "@@CANAL@@" not in tpl:
        raise SystemExit("template sem marcador @@CANAL@@")
    cmd = tpl.replace("@@CANAL@@", args.canal)
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
    print("   canal : %s" % args.canal)


if __name__ == "__main__":
    main()
