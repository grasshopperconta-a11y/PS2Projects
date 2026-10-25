# PASSAGEM DE BASTÃO — FNF PS2

**Para a IA que for continuar este projeto. Leia nesta ordem:**

1. **`REGRAS.md`** — as regras do projeto. A regra 1 é inegociável.
2. **`CONHECIMENTO.md`** — tudo que foi medido e decidido, com fonte. **Isto é
   meses de trabalho. Não redescubra.**
3. **Este arquivo** — estado, problemas, próximos passos.
4. **`PROXIMOS_PASSOS.md`** — detalhamento do que falta, com o que já se sabe.
5. **`docs/FNF_PS2_PORT_PLAN.md`** — o plano original do porte.

---

## 1. O que é este projeto

Porte do **Friday Night Funkin'** (web/Lime/OpenFL) para **PlayStation 2**, em
C, com o ps2sdk. Compilado para MIPS R5900 (EE), rodando em console real
(SCPH-90006) a partir de pendrive.

**Repositório:** `grasshopperconta-a11y/PS2Projects`
**Branch:** `arena/4c50659b-ps2projects` — **fixa, não renomeie, não troque.**
**Commit:** `00fe473`

---

## 2. Estado atual, honestamente

### O que funciona

- Build compila **sem nenhum warning**, suite inteira passa (1401 quadros,
  ASan+UBSan limpos, os dois testes negativos disparam).
- Faixa visível 4:3 correta no console: 112 linhas pretas, conteúdo apenas nas
  linhas 56..391 de 640×448.
- O log funciona e é analisável — ver §5.
- O fundo do menu **não estica mais**.

### O que não funciona ainda

Consulte `CONHECIMENTO.md` §5 para a lista completa com sintomas. Resumo:

| # | Problema | Estado |
|---|---|---|
| 1 | Linha estranha abaixo dos botões do menu | **Descoberta:** cada item é desenhado 2× por quadro. **Não corrigido.** |
| 2 | Itens quebrados ao voltar do modo história | Não corrigido |
| 3 | Fundo esticando | ✅ corrigido |
| 4 | Travamento ao entrar do modo história | Não reproduzido no harness |
| 5 | Tutorial sem notas/barra/animação | Código escrito, não confirmado |
| 6 | Log com 0 bytes | ✅ corrigido (0.2.111), **não confirmado em hardware ainda** |

### ⚠️ Três builds quebradas — leia antes de fazer qualquer coisa

As builds 0.2.108, 0.2.109 e 0.2.110 **não abriram no console**. Cada uma foi
enviada com uma causa afirmada com convicção, e **nenhuma era a real quando foi
dita**. A 0.2.111 finalmente coletou o dado que explicou tudo.

**A regra que nasceu disso:** quando não há dado que distinga as causas, a
próxima build serve para **coletar dado**, nunca para tentar um conserto. E o
harness local **não prova nada** sobre I/O, tempo ou sincronização — ele finge
`write()` e `fsync()` como instantâneos.

---

## 3. Como compilar, testar e entregar

```sh
# COMPILAR (o toolchain precisa estar em /home/user/PS2Projects/google_drive/)
sh tools/with_toolchain.sh make -j4 FNF_VERSION=0.2.112-sua-versao \
    EE_BIN=build/FNF_PS2.ELF

# TESTAR
sh test/run_tests.sh

# ANALISAR O LOG
python3 tools/analisa_log.py

# MONTAR O PENDRIVE
sh tools/build_pendrive.sh      # gera build/pendrive com LEIA-ME.txt na raiz
```

**O toolchain e os 16 assets de runtime estão no Google Drive** — ids em
`CONHECIMENTO.md` §2. Baixe antes de compilar; sem eles nada funciona.

### Ordem obrigatória antes de entregar uma build

1. compilar **sem warnings**;
2. rodar a suite inteira;
3. **provar a correção específica** (o número, a linha de log, a medição);
4. reconstruir do código commitado e confirmar binário **idêntico**;
5. só então subir para o Drive.

Se a correção é sobre I/O, tempo ou sincronização, o passo 3 **não pode** ser o
harness. Tem de ser o console.

---

## 4. Layout do pendrive

```
mass:/FNF_PS2.ELF             <- na RAIZ, com este nome EXATO
mass:/FNFPS2/assets/...       <- na RAIZ do pendrive, obrigatoriamente
mass:/FNFPS2/FNF_COLHEITA.txt <- criado pelo jogo
mass:/FNFPS2/BOOT.txt         <- criado pelo jogo
```

**O ELF fica na RAIZ e chama `FNF_PS2.ELF` — não `FNF_PS2_0.2.112.ELF`.** O
`build_pendrive.sh` (linha 124) faz `cp build/FNF_PS2.ELF "$OUT/FNF_PS2.ELF"`, e
o `LEIA-ME.txt` manda rodar `FNF_PS2.ELF` pelo lançador. Um nome diferente
(como `FNF_PS2_0.2.112.ELF`, que foi o que o canal #50 acabou colocando em
`F:\`) faz o lançador não achar o executável: o jogo nunca sobe e
`FNF_COLHEITA.txt`/`BOOT.txt` nunca aparecem.

Se a pasta `FNFPS2` não estiver na raiz, o jogo dorme para sempre em
`SleepThread()` e o log aparece no lugar errado. O ZIP de entrega já traz
`LEIA-ME.txt` na raiz explicando isso — não retire.

---

## 5. O log — seu principal instrumento

`mass:/FNFPS2/FNF_COLHEITA.txt`, acumulativo. Formato completo em
`CONHECIMENTO.md` §6. O essencial:

- `P,fase,linha,cod` — marco de fase, escrito e **sincronizado na hora**
- `S,` — estado da máquina de estados, um por quadro
- `D,quadro,i,estado,x,y,w,h,u,v,uw,vh,alfa,vy0,vy1,vy_span,gsx0,gsy0,gsx1,gsy1`
  — **um sprite por linha**, com a geometria já recortada
- `BOOT.txt` — último passo do boot completado, e um marco por quadro nos
  primeiros 300 quadros

**`python3 tools/analisa_log.py <log>` responde sozinho** os quatro defeitos que
o usuário reportou, sem ele precisar descrever nada. Use sempre.

---

## 6. Próximos passos, em ordem

1. **Compilar a build nova no PC do usuário (WSL) e rodar no console.** A
   hipótese "assets do título ausentes" foi **refutada por medição** (canal
   #58: todos os 16 assets existem no pendrive com o tamanho exato que o código
   exige). O que se sabe agora, com fonte no código: o jogo congela **dentro do
   quadro 0**, logo depois de `F0_FRAMEBUFFER_SET` — que é o último marco que o
   `BOOT.txt` conseguiu escrever.

   **E havia um defeito independente, já corrigido no commit `00fe473`:** o
   `usb_ready` só era ligado dentro do `telemetry_init()`, e só quando a
   *primeira* tentativa de abrir o log dava certo. A "segunda chance" (uma vez
   por quadro, para o caso de o pendrive montar depois) abria o descritor mas
   nunca ligava a bandeira — então o arquivo era truncado para 0 bytes pelo
   `O_TRUNC` e **nunca mais recebia um byte**. É por isso que o
   `FNF_COLHEITA.txt` vinha vazio enquanto o `BOOT.txt`, que abre o descritor
   próprio, funcionava. Detalhe em
   `fnfps2/docs/BUG_usb_ready_abertura_tardia.md`.

   Ou seja: **a colheita vazia não era sintoma do travamento.** Os dois
   escritores falhavam por motivos diferentes, e eu estava lendo um como
   sintoma do outro.

   A build nova tem marcadores cobrindo o resto do quadro 0. A ordem depois de
   `F0_FRAMEBUFFER_SET` é: `F0_DL_DUMP_BEGIN`, `F0_DL_DUMP_DONE`,
   `F0_TEL_FRAME_BEGIN`, `F0_TEL_FRAME_DONE`, `F0_TEL_STATE_DONE`,
   `F0_TELEMETRY_FLUSH_DONE`, `F0_FRAME0_FIM`. Onde o `BOOT.txt` parar diz
   exatamente em qual chamada o jogo pendurou.

   ⚠️ **Cuidado que já me custou retrabalho:** `telemetry_frame(frame_no++,...)`
   incrementa o contador, então os marcadores *depois* dessa chamada têm de
   testar `frame_no==1`, não `==0`. Com `==0` eles nunca disparavam e a build
   não coletava nada.
2. **Investigar os itens quebrados ao voltar do modo história.** Localmente o
   menu volta idêntico (2 visitas, mesmas 4 posições), então o sintoma do
   usuário não é reproduzível no harness. **Perguntar o que exatamente está
   bugado antes de mexer no código** — ver `PROXIMOS_PASSOS.md` P2.
3. **Investigar a linha estranha abaixo dos botões.** Sem dado que a explique.
   Nas capturas da 0.2.106 o único fora-da-faixa eram 3 pixels na linha 6, no
   topo. Não concluir nada sem evidência nova.
4. **Reproduzir o travamento do modo história.** O harness atravessa o jogo
   inteiro 12× sem travar. Se o console travar, o `BOOT.txt` com marca por
   quadro diz em qual quadro.
5. **Tutorial.** Câmera travada no BF, sem notas, sem barra de acerto,
   personagens não animando, música toca.
6. **Otimização** — objetivo declarado do usuário. Ver `PROXIMOS_PASSOS.md` P5.

### ⚠️ Três "descobertas" minhas que eram FALSAS — não repetir

- **"O menu desenha cada item duas vezes."** Falso. Vinha de ler um log com
  quatro execuções acumuladas. Um quadro do estado 6 tem 5 sprites: 1 fundo e 4
  itens. Corrigido e documentado em `PROXIMOS_PASSOS.md` P1.
- **"O menu volta com cara diferente depois do roteiro."** Falso. A contagem por
  quadro varia por causa do piscar do confirmar (16 piscadas). Comparando o
  conjunto de posições por visita, as 2 visitas são idênticas. P2.
- **"Os assets do título estão ausentes ou corrompidos."** Falso, e refutado por
  medição: o canal #58 auditou o pendrive e todos os 16 assets existem, 12 com o
  tamanho **exato** que o código exige. Era um palpite apresentado como
  hipótese, e a medição o matou. **Não insistir nela.**

A lição das duas: **o log tem de ser lido por rodada, e a contagem por quadro
não é medida de nada.** `tools/analisa_log.py` agora faz as duas coisas certo, e
`test/run_tests.sh` tem um teste que falha se voltar atrás.
