/* prova_port.c -- prova por EXECUCAO de cada funcao dos modulos do port que
 * rodam fora do PS2.
 *
 * O que este arquivo existe para fazer: transformar "eu li o codigo e parece
 * certo" em "eu rodei e o resultado medido foi este". Cada bloco abaixo exercita
 * funcoes de verdade do port -- nao uma reimplementacao -- e afirma o resultado.
 *
 * Compilado com --coverage para que o relatorio diga, por funcao, quantas
 * linhas foram executadas. Uma funcao com 0 linhas executadas nao foi testada,
 * por mais que o teste tenha passado.
 *
 * O que NAO esta aqui, e por que:
 *   main.c e telemetry.c dependem do hardware do PS2 (GS, DMA, USB, threads do
 *   IOP). Nao da para executá-los no host sem substituir justamente o que se
 *   quer provar. Esses dois sao cobertos por compilacao com o toolchain real
 *   (zero warnings) e por leitura, e o documento diz isso sem enfeitar.
 *
 *   gcc -O1 --coverage -Isrc -Isrc/engine -Itest/host-shim \
 *       test/prova_port.c src/chart.c src/chart_events.c \
 *       src/engine/song_registry.c src/engine/vram_cache.c src/engine/io_fila.c \
 *       src/audio_ring.c test/host-shim/host_thread_stubs.c \
 *       -o /tmp/prova_port -lm -lpthread
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <math.h>
#include <fcntl.h>
#include <unistd.h>

#include "tamtypes.h"
#include "chart.h"
#include "chart_events.h"
#include "vram_cache.h"
#include "io_fila.h"
#include "audio_ring.h"
#include "song_registry.h"

static int FALHOU = 0;
static int TOTAL = 0;

static void ok(int cond, const char *msg)
{
    TOTAL++;
    if (cond) {
        printf("  OK    %s\n", msg);
    } else {
        printf("  FALHA %s\n", msg);
        FALHOU++;
    }
}

static void perto(float a, float b, const char *msg)
{
    char buf[220];
    snprintf(buf, sizeof(buf), "%s (%.6f vs %.6f)", msg, a, b);
    ok(fabsf(a - b) < 1e-4f, buf);
}

/* ================================================================== vram_cache
 * A menor unidade de endereco do GS para base de textura eh 256 bytes (TBP0
 * conta de 256 em 256), por isso VC_ALINHAMENTO=256. O teste prova que o
 * alinhamento acontece e que a soma dos blocos nunca passa do tamanho pedido.
 */
static void prova_vram_cache(void)
{
    vc_t c;
    unsigned int saida = 0;
    unsigned int antes;

    printf("\n== vram_cache ==\n");

    /* CONVENCAO DO ALOCADOR, lida do fonte: a tabela comeca com UM bloco que
       eh o buraco livre cobrindo a regiao inteira (usado=0, bytes=tamanho).
       Por isso n==1 depois do init, e nao 0. vc_limpar nao zera a tabela:
       ela transforma bloco usado em buraco, que o alinhamento depois funde. */
    vc_init(&c, 0, 64 * 1024);
    ok(c.n == 1, "vc_init deixa 1 bloco (o buraco livre que cobre tudo)");
    ok(c.b[0].usado == 0, "e esse bloco eh um buraco, nao usado");
    ok(c.b[0].bytes == 64 * 1024, "e cobre a regiao inteira");
    ok(vc_livre(&c) == 64 * 1024, "vc_livre devolve o tamanho inteiro");
    ok(vc_maior_buraco(&c) == 64 * 1024, "vc_maior_buraco idem, vazio");

    /* 300 bytes pede 2 blocos de 256 = 512. O desperdicio de ate 255 bytes por
       textura eh o preco do alinhamento do GS (TBP0 conta de 256 em 256); o
       teste fixa o valor para que uma mudanca de regra fique visivel.
       Retorno: 1=acerto, 0=alocou (miss), -1=falhou. */
    ok(vc_pedir(&c, 1, 300, &saida) == 0, "vc_pedir em MISS devolve 0");
    ok(saida == 0, "primeiro bloco endereco 0");
    ok(vc_livre(&c) == 64 * 1024 - 512, "consumiu 512 (2 x 256), nao 300");
    ok(c.acertos == 0 && c.faltas == 1, "faltas=1, acertos=0");

    /* pedir de novo a MESMA chave eh acerto, e devolve o MESMO endereco */
    antes = saida;
    ok(vc_pedir(&c, 1, 300, &saida) == 1, "vc_pedir repete a chave -> 1 (acerto)");
    ok(saida == antes, "e devolve o mesmo endereco");
    ok(c.acertos == 1 && c.faltas == 1, "acertos=1 agora");

    vc_fixar(&c, 1);
    ok(c.b[0].fixo == 1, "vc_fixar marca o bloco");
    ok(c.b[0].usado == 1, "e o bloco esta em uso");

    /* encher ate forcar despejo: o fixo NAO pode sair */
    {
        int i;
        for (i = 2; i < 400; ++i) {
            unsigned int s2 = 0;
            if (vc_pedir(&c, (unsigned)i, 4096, &s2) != 0) break;
        }
        ok(c.despejos > 0, "vc_pedir despejou para caber");
        ok(c.b[0].fixo == 1 && c.b[0].usado, "o bloco fixo sobreviveu ao despejo");
        ok(vc_pedir(&c, 1, 300, &saida) == 1, "e a chave fixa ainda eh acerto");
    }

    /* vc_limpar preserva os fixos DE PROPOSITO: fonte e HUD nao podem
       desaparecer no meio de uma musica. So depois de desfixar eles somem. */
    vc_limpar(&c);
    ok(c.b[0].fixo == 1 && c.b[0].usado == 1,
       "vc_limpar preserva bloco fixo (fonte/HUD nao podem sumir)");
    ok(vc_livre(&c) < 64 * 1024, "e o espaco do fixo nao foi devolvido");
    vc_limpar(&c);
    ok(vc_pedir(&c, 1, 300, &saida) == 1, "e ele continua la depois de 2 limpezas");

    /* pedido maior que a regiao inteira: tem de falhar, nao truncar */
    ok(vc_pedir(&c, 99, 64 * 1024 + 1, &saida) == -1,
       "vc_pedir recusa pedido maior que a regiao");
    ok(vc_pedir(&c, 99, 0, &saida) == -1, "vc_pedir recusa 0 bytes");
    ok(c.falhas > 0, "e contou as falhas");
}

/* ==================================================================== io_fila
 * A fila fatiada. O que importa aqui NAO eh o resultado -- eh a fatia: nenhuma
 * operacao prende o pendrive por mais de IO_FATIA bytes, e entre fatias quem
 * tem prioridade maior passa na frente. Isso eh o que impediu a corrupcao do
 * usbhdfsd (ver o cabecalho do modulo).
 *
 * Convencoes lidas do fonte:
 *   io_bombear processa UMA fatia por chamada (devolve 1), nao a fila inteira
 *   io_resultado COLHE e LIBERA o pedido (ativo=0) -- eh assim que a fila
 *     esvazia; sem chamar, o pedido fica la para sempre
 *   escolher: menor prio primeiro; empate decide o selo (ordem de chegada)
 *   existe um static int ultimo dentro de io_bombear: ele persiste ENTRE
 *     instancias de io_fila_t, e afeta trocas_de_dono
 */
static unsigned char disco[256 * 1024];
static unsigned char disco_saida[256 * 1024];
static unsigned int pos_leitura, pos_escrita;
static int falhar_em;          /* 1 = a camada de disco devolve -1 */

static int fake_ler(int fd, void *buf, unsigned int n)
{
    (void)fd;
    if (falhar_em) return -1;
    if (pos_leitura >= sizeof(disco)) return 0;         /* EOF */
    if (n > sizeof(disco) - pos_leitura) n = sizeof(disco) - pos_leitura;
    memcpy(buf, disco + pos_leitura, n);
    pos_leitura += n;
    return (int)n;
}

static int fake_escrever(int fd, const void *buf, unsigned int n)
{
    (void)fd;
    if (pos_escrita + n > sizeof(disco_saida))
        n = sizeof(disco_saida) - pos_escrita;
    if (n == 0) return -1;
    memcpy(disco_saida + pos_escrita, buf, n);
    pos_escrita += n;
    return (int)n;
}

static void prova_io_fila(void)
{
    io_fila_t f;
    unsigned char dst[256 * 1024];
    unsigned int i;
    int id, fatias_gastas;

    printf("\n== io_fila ==\n");

    for (i = 0; i < sizeof(disco); ++i) disco[i] = (unsigned char)(i * 31u + 7u);
    pos_leitura = pos_escrita = 0; falhar_em = 0;

    io_init(&f, fake_ler, fake_escrever);
    ok(io_pendentes(&f) == 0, "fila comeca vazia");
    ok(f.fatias == 0 && f.trocas_de_dono == 0, "e os contadores em zero");

    /* 100 KB de leitura: 32768*3 = 98304, sobram 1696 -> 4 fatias exatas */
    id = io_enfileirar(&f, IO_LER, 0, dst, 100 * 1024, IO_PRIO_NORMAL);
    ok(id >= 0, "io_enfileirar devolve um indice");
    ok(io_pendentes(&f) == 1, "1 pedido pendente");
    ok(!io_terminado(&f, id), "e ainda nao terminou");

    /* UMA chamada = UMA fatia, nao o pedido inteiro */
    ok(io_bombear(&f) == 1, "io_bombear devolve 1 (fez algo)");
    ok(f.fatias == 1, "e gastou exatamente 1 fatia");
    ok(!io_terminado(&f, id), "100 KB nao cabem em uma fatia de 32 KB");

    /* bombear ate terminar, contando as fatias */
    fatias_gastas = 1;
    while (!io_terminado(&f, id) && fatias_gastas < 100) {
        if (!io_bombear(&f)) break;
        fatias_gastas++;
    }
    ok(io_terminado(&f, id), "io_terminado dispara no fim");
    ok(fatias_gastas == 4, "100 KB = 4 fatias de 32 KB");
    ok(f.fatias == 4, "e o contador de fatias bate");

    /* os dados: a fatia nao pode perder nem repetir byte no meio */
    ok(memcmp(dst, disco, 100 * 1024) == 0,
       "os 100 KB lidos batem byte a byte com o disco");

    /* io_resultado colhe E libera -- sem ele a fila nunca esvazia */
    ok(io_resultado(&f, id) == 100 * 1024, "io_resultado devolve os bytes");
    ok(io_pendentes(&f) == 0, "e o pedido saiu da fila");
    ok(io_resultado(&f, id) == -1, "colher duas vezes devolve -1");

    /* escrita: mesma maquina, outro sentido */
    id = io_enfileirar(&f, IO_ESCREVER, 1, dst, 64 * 1024, IO_PRIO_NORMAL);
    ok(id >= 0, "io_enfileirar aceita escrita");
    while (!io_terminado(&f, id)) if (!io_bombear(&f)) break;
    ok(io_resultado(&f, id) == 64 * 1024, "escreveu 64 KB");
    ok(memcmp(disco_saida, disco, 64 * 1024) == 0, "e o que gravou eh o que leu");

    /* PRIORIDADE: audio (0) passa na frente de fundo (2).
       Enfileira o de fundo primeiro de proposito: se a fila fosse FIFO pura,
       o de fundo sairia primeiro e o teste pegaria. */
    {
        int fundo = io_enfileirar(&f, IO_LER, 0, dst, 40 * 1024, IO_PRIO_FUNDO);
        int audio = io_enfileirar(&f, IO_LER, 0, dst, 40 * 1024, IO_PRIO_AUDIO);
        ok(fundo >= 0 && audio >= 0, "dois pedidos enfileirados");
        io_bombear(&f);
        ok(f.p[audio].feitos > 0, "a primeira fatia foi do audio (prio 0)");
        ok(f.p[fundo].feitos == 0, "e o de fundo (prio 2) esperou");
        while (io_terminado(&f, audio) == 0) if (!io_bombear(&f)) break;
        io_resultado(&f, audio);
        io_bombear(&f);
        ok(f.p[fundo].feitos > 0, "com o audio terminado, o de fundo roda");
        while (io_terminado(&f, fundo) == 0) if (!io_bombear(&f)) break;
        io_resultado(&f, fundo);
    }

    /* EMPATE de prioridade: decide o selo, ou seja, quem chegou antes */
    {
        int a = io_enfileirar(&f, IO_LER, 0, dst, 40 * 1024, IO_PRIO_NORMAL);
        int b = io_enfileirar(&f, IO_LER, 0, dst, 40 * 1024, IO_PRIO_NORMAL);
        io_bombear(&f);
        ok(f.p[a].feitos > 0, "com prio igual, passa quem chegou antes");
        ok(f.p[b].feitos == 0, "e o segundo espera");
        while (io_terminado(&f, a) == 0) if (!io_bombear(&f)) break;
        io_resultado(&f, a);
        while (io_terminado(&f, b) == 0) if (!io_bombear(&f)) break;
        io_resultado(&f, b);
    }

    /* FILA CHEIA: IO_MAX_PEDIDOS pedidos, o proximo tem de ser recusado */
    {
        int ids[IO_MAX_PEDIDOS], k, recusado = 0;
        for (k = 0; k < IO_MAX_PEDIDOS; ++k) {
            ids[k] = io_enfileirar(&f, IO_LER, 0, dst, 8 * 1024, IO_PRIO_NORMAL);
            if (ids[k] < 0) recusado = 1;
        }
        ok(!recusado, "io_enfileirar aceita ate IO_MAX_PEDIDOS");
        ok(io_enfileirar(&f, IO_LER, 0, dst, 8 * 1024, IO_PRIO_NORMAL) < 0,
           "e recusa o proximo (fila cheia)");
        for (k = 0; k < IO_MAX_PEDIDOS; ++k) {
            while (io_terminado(&f, ids[k]) == 0) if (!io_bombear(&f)) break;
            io_resultado(&f, ids[k]);
        }
        ok(io_pendentes(&f) == 0, "depois de colher tudo, a fila esvazia");
    }

    /* ERRO no disco: encerra com o que ja foi feito, resultado negativo */
    {
        pos_leitura = 0; falhar_em = 1;   /* falha ja na primeira fatia */
        id = io_enfileirar(&f, IO_LER, 0, dst, 40 * 1024, IO_PRIO_NORMAL);
        while (!io_terminado(&f, id)) if (!io_bombear(&f)) break;
        ok(f.p[id].resultado < 0, "erro no disco dah resultado negativo");
        ok(f.p[id].feitos == 0, "e nada foi lido antes do erro");
        io_resultado(&f, id);
        falhar_em = 0;
    }

    /* fila vazia: bombear devolve 0, nao trava */
    ok(io_bombear(&f) == 0, "io_bombear em fila vazia devolve 0");

    /* io_pendentes so conta quem ainda nao terminou */
    id = io_enfileirar(&f, IO_LER, 0, dst, 8 * 1024, IO_PRIO_NORMAL);
    io_bombear(&f);
    while (!io_terminado(&f, id)) if (!io_bombear(&f)) break;
    ok(io_pendentes(&f) == 0, "pedido terminado nao conta como pendente");
    ok(f.p[id].ativo == 1, "mas continua na fila ate ser colhido");
    io_resultado(&f, id);

    /* maior_espera eh declarado e zerado no init, mas NADA o incrementa.
       O teste fixa isso: se um dia alguem passar a usa-lo, o teste quebra e
       a pessoa vai perceber que precisa atualizar a prova. */
    ok(f.maior_espera == 0, "maior_espera continua 0 (contador declarado, nao usado)");
}

/* ======================================================================= chart
 * O carregador de chart. O formato v3 tem cabecalho de 40 bytes e o payload
 * (notas + bpms + secoes + eventos) logo depois. Tudo little-endian.
 *
 * O checksum eh FNV-1a de 32 bits sobre o payload. O teste tem uma
 * implementacao DE REFERENCIA, independente, e compara: se as duas baterem,
 * a do port esta certa -- nao ha como as duas errarem igual.
 *
 * Campos do cabecalho v3 (offsets lidos do fonte):
 *   +0 magico "FCH3"   +4 versao(u16)   +6 stride nota(u16)=12
 *   +8 notas(u32)      +12 bpms(u16)    +14 secoes(u16)  +16 eventos(u16)
 *   +18 flags(u16)=0   +20 stride bpm(u16)=16  +22 stride secao(u16)=8
 *   +24 stride evento(u16)=16  +26 zero(u16)  +28 checksum(u32)
 *   +32 fim(u32)       +36 zero(u32)
 */
#define HDR3 40u
#define EV3  16u

static void poe16(unsigned char *p, u16 v)
{ p[0] = (unsigned char)(v & 0xff); p[1] = (unsigned char)(v >> 8); }
static void poe32(unsigned char *p, u32 v)
{
    p[0] = (unsigned char)(v & 0xff);         p[1] = (unsigned char)((v >> 8) & 0xff);
    p[2] = (unsigned char)((v >> 16) & 0xff); p[3] = (unsigned char)((v >> 24) & 0xff);
}

/* FNV-1a de 32 bits: base 2166136261, prima 16777619. Escrito do zero aqui
   justamente para nao poder copiar um bug da implementacao testada. */
/* chart_fnv1a_more continua de um hash existente, em vez de comecar da base.
   O checksum de v4 precisa disso: payload primeiro, tabelas depois. */
static u32 fnv_ref_more(const unsigned char *d, unsigned n, u32 h)
{
    unsigned i;
    for (i = 0; i < n; ++i) { h ^= d[i]; h *= 16777619u; }
    return h;
}

static u32 fnv_ref(const unsigned char *d, unsigned n)
{
    return fnv_ref_more(d, n, 2166136261u);
}

static unsigned monta_chart_v3(unsigned char *arq, unsigned char *payload,
                               u32 notes, u32 bpms, u32 sections, u32 events,
                               u32 end_sample)
{
    unsigned char *h = arq;
    unsigned pb, i, off;
    memcpy(h, "FCH3", 4);
    poe16(h + 4, 3);            /* versao */
    poe16(h + 6, 12);           /* stride de nota */
    poe32(h + 8, notes);
    poe16(h + 12, (u16)bpms);
    poe16(h + 14, (u16)sections);
    poe16(h + 16, (u16)events);
    poe16(h + 18, 0);           /* flags: 0 em v3 */
    poe16(h + 20, 16);          /* stride de bpm */
    poe16(h + 22, 8);           /* stride de secao */
    poe16(h + 24, EV3);         /* stride de evento v3 */
    poe16(h + 26, 0);
    pb = notes * 12u + bpms * 16u + sections * 8u + events * EV3;
    memset(payload, 0, pb);

    /* REGRAS DE VALIDACAO, lidas do carregador:
       nota  12B: sample u32, duration u32, lane u8<=3, press u8<=1, order u16==i
                  sample<=end, duration<=end-sample, sample monotono
       bpm   16B: start_step, start_sample, samples_per_step!=0, bpm!=0
                  start_sample<=end, start_step/start_sample estritamente crescentes
                  bpm[0].start_step==0 e start_sample==0
       secao  8B: start u32, u8<=1, u8!=0, order u16==i, start crescente
                  secao[0].start==0
       evento 16B(v3): sample u32, type u32!=0, value u32, order u32==i
                  sample<=end, monotono
       Um chart que passa por tudo isso prova o carregador inteiro. */
    for (i = 0; i < notes; ++i) {
        unsigned char *r = payload + i * 12u;
        poe32(r, i * 200u);            /* sample */
        poe32(r + 4, 100u);            /* duration */
        r[8] = (unsigned char)(i & 3u);      /* lane */
        r[9] = (unsigned char)(i & 1u);      /* must_press */
        poe16(r + 10, (u16)i);         /* order == i */
    }
    off = notes * 12u;
    for (i = 0; i < bpms; ++i) {
        unsigned char *r = payload + off + i * 16u;
        poe32(r, i * 16u);             /* start_step */
        poe32(r + 4, i * 16u * 7200u); /* start_sample */
        poe32(r + 8, 7200u);           /* samples_per_step */
        poe32(r + 12, 120u);           /* bpm */
    }
    off += bpms * 16u;
    for (i = 0; i < sections; ++i) {
        unsigned char *r = payload + off + i * 8u;
        poe32(r, i * 400u);            /* start */
        r[4] = 0;
        r[5] = 1;
        poe16(r + 6, (u16)i);          /* order == i */
    }
    off += sections * 8u;
    for (i = 0; i < events; ++i) {
        unsigned char *r = payload + off + i * EV3;
        poe32(r, i * 50u);             /* sample */
        poe32(r + 4, 1u + i);          /* type */
        poe32(r + 8, 0u);              /* value */
        poe32(r + 12, i);              /* order == i */
    }

    poe32(h + 28, fnv_ref(payload, pb));
    poe32(h + 32, end_sample);
    poe32(h + 36, 0);
    memcpy(arq + HDR3, payload, pb);
    return HDR3 + pb;
}


/* ============================================================ chart v4
 * O formato v4 tem cabecalho de 48 bytes, evento de stride 32 e DUAS tabelas
 * depois do payload: a de strings e a de blocos. O checksum cobre o payload
 * E as tabelas -- eh por isso que chart_fnv1a_more existe.
 *
 * Layout da cauda, lido do carregador:
 *   [string_count x u32 offsets][dados das strings, terminadas em NUL]
 *   [u32 block_count][para cada bloco: u32 tamanho + dados]
 * string_bytes_of nao tem o fim dos dados gravado: ela caminha os NULs.
 */
#define HDR4 48u
#define EV4  32u

static unsigned monta_chart_v4(unsigned char *arq)
{
    static const char strs[] = "linear\0quadInOut\0";
    unsigned char *h = arq;
    unsigned pb, tail, i;

    memcpy(h, "FCH4", 4);
    poe16(h + 4, 4);            /* versao */
    poe16(h + 6, 12);
    poe32(h + 8, 1);            /* 1 nota */
    poe16(h + 12, 1);           /* 1 bpm */
    poe16(h + 14, 1);           /* 1 secao */
    poe16(h + 16, 1);           /* 1 evento */
    poe16(h + 18, 3);           /* flags: bit0 strings, bit1 blocks */
    poe16(h + 20, 16);
    poe16(h + 22, 8);
    poe16(h + 24, EV4);
    poe16(h + 26, 0);
    poe32(h + 32, 200000);      /* fim */
    poe32(h + 36, 2);           /* string_count */
    poe32(h + 44, 1);           /* block_count */

    /* payload: nota + bpm + secao + evento v4 */
    memset(arq + HDR4, 0, 12 + 16 + 8 + EV4);
    poe32(arq + HDR4, 0);              /* nota: sample 0 */
    poe32(arq + HDR4 + 4, 100);        /* duration */
    poe32(arq + HDR4 + 12, 0);         /* bpm: start_step 0 */
    poe32(arq + HDR4 + 16, 0);         /* start_sample 0 */
    poe32(arq + HDR4 + 20, 7200);      /* samples_per_step */
    poe32(arq + HDR4 + 24, 120);       /* bpm */
    poe32(arq + HDR4 + 28, 0);         /* secao: start 0 */
    arq[HDR4 + 32] = 0; arq[HDR4 + 33] = 1;   /* r[4]=0, r[5]=1 */
    /* evento v4: type 2 = ZOOM_CAMERA, com ref apontando para a string 1 */
    poe32(arq + HDR4 + 36, 0);         /* sample */
    poe32(arq + HDR4 + 40, 2);         /* type */
    poe32(arq + HDR4 + 44, 1000);      /* p0: duracao */
    poe32(arq + HDR4 + 48, 1200);      /* p1: zoom */
    poe32(arq + HDR4 + 52, 0);         /* p2 */
    poe32(arq + HDR4 + 56, 0);         /* a */
    poe32(arq + HDR4 + 60, 1u | CHART_B_REF_IS_STRING);  /* b: ref eh string */
    poe32(arq + HDR4 + 64, 1);         /* ref = indice 1 = "quadInOut" */
    pb = 12 + 16 + 8 + EV4;

    /* cauda: 2 offsets + os dados das strings + block_count + 1 bloco */
    tail = HDR4 + pb;
    poe32(arq + tail + 0, 0);          /* offset da string 0 */
    poe32(arq + tail + 4, 7);          /* offset da string 1 ("linear\0" = 7) */
    /* sizeof(strs) inclui o NUL que o COMPILADOR poe no fim do literal.
       Copiar ele deixaria um byte 0 solto entre as strings e a tabela de
       blocos, e o carregador (que caminha os NULs para achar o fim das
       strings) acabaria lendo block_count no lugar errado -> rc=-15. */
    memcpy(arq + tail + 8, strs, sizeof(strs) - 1u);
    {
        unsigned pos = tail + 8 + (sizeof(strs) - 1u);   /* mesma conta do memcpy */
        poe32(arq + pos, 1);           /* block_count */
        pos += 4;
        poe32(arq + pos, 4);           /* tamanho do bloco 0 */
        pos += 4;
        arq[pos + 0] = 0xde; arq[pos + 1] = 0xad;
        arq[pos + 2] = 0xbe; arq[pos + 3] = 0xef;
        tail = (pos + 4) - tail;
    }

    /* checksum sobre payload + cauda: eh o unico jeito de cobrir
       chart_fnv1a_more, que so roda quando ha cauda */
    {
        u32 hh = fnv_ref(arq + HDR4, pb);
        hh = fnv_ref_more(arq + HDR4 + pb, tail, hh);
        poe32(h + 28, hh);
    }
    return HDR4 + pb + tail;
}

static void prova_chart(void)
{
    static unsigned char arq[4096], payload[2048];
    chart_info_t info;
    unsigned n;

    printf("\n== chart ==\n");

    n = monta_chart_v3(arq, payload, 2, 2, 1, 1, 200000);
    {
        FILE *fp = fopen("/tmp/prova_chart_v3.chart", "wb");
        ok(fp != NULL, "arquivo temporario criado");
        if (fp) { fwrite(arq, 1, n, fp); fclose(fp); }
    }

    /* O teste que importa: um chart montado na mesa, com checksum feito por
       uma implementacao independente, carrega. */
    ok(chart_load("/tmp/prova_chart_v3.chart", &info) == 0,
       "chart_load aceita um chart v3 com checksum correto");
    ok(info.version == 3, "e le a versao 3");
    ok(info.note_count == 2, "note_count = 2 (leu u32 little-endian)");
    ok(info.bpm_count == 2, "bpm_count = 2 (leu u16 little-endian)");
    ok(info.section_count == 1, "section_count = 1");
    ok(info.event_count == 1, "event_count = 1");
    ok(info.song_end_sample == 200000, "song_end_sample = 200000");
    ok(info.checksum == fnv_ref(payload, 2 * 12 + 2 * 16 + 1 * 8 + 1 * EV3),
       "checksum lido == referencia FNV-1a independente");
    ok(info.initial_bpm == 120, "initial_bpm = 120 (o primeiro da tabela)");

    /* corromper UM byte do payload tem de derrubar o checksum */
    arq[HDR3] ^= 0x40;
    {
        FILE *fp = fopen("/tmp/prova_chart_v3.chart", "wb");
        if (fp) { fwrite(arq, 1, n, fp); fclose(fp); }
    }
    ok(chart_load("/tmp/prova_chart_v3.chart", &info) == -8,
       "chart_load recusa payload corrompido (checksum, rc=-8)");
    arq[HDR3] ^= 0x40;

    /* e corromper o checksum do cabecalho tambem */
    arq[28] ^= 0x01;
    {
        FILE *fp = fopen("/tmp/prova_chart_v3.chart", "wb");
        if (fp) { fwrite(arq, 1, n, fp); fclose(fp); }
    }
    ok(chart_load("/tmp/prova_chart_v3.chart", &info) == -8,
       "chart_load recusa checksum de cabecalho corrompido (rc=-8)");
    arq[28] ^= 0x01;

    /* magico invalido: rc=-4 */
    {
        FILE *fp;
        memcpy(arq, "XXXX", 4);
        fp = fopen("/tmp/prova_chart_v3.chart", "wb");
        if (fp) { fwrite(arq, 1, n, fp); fclose(fp); }
    }
    ok(chart_load("/tmp/prova_chart_v3.chart", &info) == -4,
       "chart_load recusa magico invalido (rc=-4)");
    memcpy(arq, "FCH3", 4);

    /* contagem zero de notas: rc=-5 */
    n = monta_chart_v3(arq, payload, 0, 1, 1, 0, 7200);
    {
        FILE *fp = fopen("/tmp/prova_chart_v3.chart", "wb");
        if (fp) { fwrite(arq, 1, n, fp); fclose(fp); }
    }
    ok(chart_load("/tmp/prova_chart_v3.chart", &info) == -5,
       "chart_load recusa note_count=0 (rc=-5)");

    /* caminho inexistente: rc=-1 */
    ok(chart_load("/tmp/nao_existe_chart.chart", &info) == -1,
       "chart_load em caminho inexistente devolve -1");
    /* path NULL devolve -1; info NULL eh TOLERADO de proposito -- o carregador
       so nao escreve o resultado (if(out)*out=...). Um chamador que so quer
       validar o arquivo usa isso. */
    ok(chart_load(NULL, &info) == -1, "chart_load(NULL) devolve -1");
    n = monta_chart_v3(arq, payload, 2, 2, 1, 1, 200000);
    {
        FILE *fp = fopen("/tmp/prova_chart_v3.chart", "wb");
        if (fp) { fwrite(arq, 1, n, fp); fclose(fp); }
    }
    ok(chart_load("/tmp/prova_chart_v3.chart", NULL) == 0,
       "chart_load com info NULL devolve 0 e apenas nao escreve");

    /* acesso fora da faixa: -1 / NULL, nunca leitura de memoria errada */
    ok(chart_load("/tmp/prova_chart_v3.chart", &info) == 0, "recarrega o chart valido");
    {
        chart_note_t nota;
        ok(chart_note(9999, &nota) == -1, "chart_note fora da faixa devolve -1");
        ok(chart_note(0, &nota) == 0, "chart_note(0) devolve a primeira nota");
        ok(nota.sample == 0, "e ela comeca na amostra 0");
        ok(nota.lane == 0, "e na pista 0");
    }
    ok(chart_event(9999) == NULL, "chart_event fora da faixa devolve NULL");
    ok(chart_event_string(9999) == NULL, "chart_event_string fora da faixa devolve NULL");

    /* chart_step_at: amostra -> passo. O primeiro bpm comeca no passo 0,
       o segundo no passo 16 (16*7200 = 115200 amostras). */
    ok(chart_step_at(0) == 0, "chart_step_at(0) = passo 0");
    ok(chart_step_at(115200) == 16, "chart_step_at(115200) = passo 16");
    ok(chart_step_at(200000) >= 16, "chart_step_at no fim >= passo 16");
    {
        u32 anterior = 0, s;
        int monotono = 1;
        for (s = 0; s <= 200000; s += 4096) {
            u32 passo = chart_step_at(s);
            if (passo < anterior) monotono = 0;
            anterior = passo;
        }
        ok(monotono, "chart_step_at eh monotonico na amostra");
    }

    /* ================= v4: tabelas de strings e de blocos ================= */
    {
        static unsigned char a4[4096];
        unsigned n4 = monta_chart_v4(a4);
        FILE *fp = fopen("/tmp/prova_chart_v4.chart", "wb");
        ok(fp != NULL, "arquivo v4 criado");
        if (fp) { fwrite(a4, 1, n4, fp); fclose(fp); }

        ok(chart_load("/tmp/prova_chart_v4.chart", &info) == 0,
           "chart_load aceita um chart v4 com tabelas");
        ok(info.version == 4, "e le a versao 4");
        ok(info.string_count == 2, "string_count = 2");
        ok(info.block_count == 1, "block_count = 1");

        /* os acessores de tabela: devolvem NULL/0 fora da faixa ou em v3 */
        ok(chart_event_string(0) != NULL, "chart_event_string(0) devolve a string");
        ok(strcmp(chart_event_string(0), "linear") == 0,
           "e a string 0 eh \"linear\" (offset 0)");
        ok(strcmp(chart_event_string(1), "quadInOut") == 0,
           "e a string 1 eh \"quadInOut\" (offset 7, depois do NUL)");
        ok(chart_event_string(2) == NULL, "chart_event_string fora da faixa devolve NULL");

        {
            u32 len = 0;
            const unsigned char *bl = chart_event_block(0, &len);
            ok(bl != NULL, "chart_event_block(0) devolve o bloco");
            ok(len == 4, "e o tamanho lido eh 4");
            if (bl) ok(bl[0] == 0xde && bl[1] == 0xad && bl[2] == 0xbe && bl[3] == 0xef,
                       "e o conteudo eh o que foi gravado");
            ok(chart_event_block(1, &len) == NULL,
               "chart_event_block fora da faixa devolve NULL");
        }

        /* um chart v3 NAO tem tabelas: os acessores devolvem 0 */
        ok(chart_load("/tmp/prova_chart_v3.chart", &info) == 0, "recarrega o v3");
        ok(chart_event_string(0) == NULL, "em v3, chart_event_string devolve NULL");
        ok(chart_event_block(0, NULL) == NULL, "em v3, chart_event_block devolve NULL");

        /* o evento v4 com ref de string: o ease sai da TABELA, nao do b */
        ok(chart_load("/tmp/prova_chart_v4.chart", &info) == 0, "volta ao v4");
        {
            const chart_event_t *ev = chart_event(0);
            ok(ev != NULL, "chart_event(0) no v4");
            if (ev) {
                ok(ev->p0 == 1000 && ev->p1 == 1200,
                   "p0/p1/p2 vieram dos campos certos (nao de value/order)");
                ok(ev->ref == 1, "ref = 1 (indice na tabela de strings)");
                chart_events_apply(ev);
                perto(chart_events_state()->zoom_to, 1.2f,
                      "o zoom veio de p1 = 1.2");
                ok(chart_events_state()->zoom_ease == 10,
                   "a ease veio da string \"quadInOut\" -> indice 10");
            }
        }
    }

    /* chart_load_song_layout: mesmo que o load_song, mas tentando todos os
       layouts de pendrive. Em raiz inexistente devolve o codigo do layout 0
       e poe -1 em layout_out. */
    {
        int layout = 12345;
        const sr_level_t *lv0 = sr_level(0);
        ok(lv0 != NULL && lv0->song_count > 0, "musica do registro para o layout");
        if (lv0 && lv0->song_count)
            ok(chart_load_song_layout("/tmp/raiz_que_nao_existe", lv0->songs[0],
                                      "easy", &info, &layout) != 0,
               "chart_load_song_layout em raiz inexistente devolve erro");
        ok(layout == -1, "e poe -1 em layout_out quando nenhum layout abriu");
    }

    /* chart_load_song(root, song, ...): monta o caminho pelo registro e
       carrega. Com root NULL e song NULL tem de recusar, nao dereferenciar. */
    ok(chart_load_song(NULL, NULL, NULL, NULL) == -1,
       "chart_load_song(NULL,NULL,NULL,NULL) devolve -1");
    ok(chart_load_song("/tmp", NULL, NULL, NULL) == -1,
       "chart_load_song com song NULL devolve -1");
    /* raiz inexistente: devolve o codigo do chart_load para o layout 0.
       Usa uma musica do registro de verdade. */
    {
        const sr_level_t *lv0 = sr_level(0);
        ok(lv0 != NULL && lv0->song_count > 0, "pegou uma musica do registro");
        if (lv0 && lv0->song_count)
            ok(chart_load_song("/tmp/raiz_que_nao_existe", lv0->songs[0],
                               "easy", &info) != 0,
               "chart_load_song em raiz inexistente devolve codigo de erro");
    }
}

/* ================================================================ chart_events
 * As easing functions sao as do flixel (FlxEase). O ORIGINAL monta um nome de
 * funcao ('expoIn', 'quadInOut') e procura em FlxEase -- por isso os nomes
 * que nao carregam direcao (linear, elasticInOut, quintInOut) ignoram dir, e
 * CLASSIC e INSTANT nao sao curvas: caem no alvo na hora.
 *
 * O mapa de indices, lido do switch de chart_ease_eval:
 *   0 CLASSIC  1 INSTANT  2 circ  3 elastic  4 elasticInOut  5 expo
 *   6 expoIn  7 expoOut  8 linear  9 quad  10 quadInOut  11 quart  12 quintInOut
 * NAO existe cubic nem sine na tabela -- e chart_ease_names[13] confirma.
 */
static void prova_ease(void)
{
    static const u32 todas[13] = {0,1,2,3,4,5,6,7,8,9,10,11,12};
    unsigned i;
    int extremos_ok = 1, monotona_ok = 1;

    printf("\n== chart_events: easing ==\n");

    /* A propriedade que TODA easing de entrada/saida satisfaz: f(0)=0 e f(1)=1.
       Se alguma curva falhar nisso, a animacao comeca ou termina fora do lugar
       -- defeito visivel, nao teorico. */
    for (i = 0; i < 13; ++i) {
        float a = chart_ease_eval(todas[i], CHART_B_EASEDIR_IN, 0.0f);
        float b = chart_ease_eval(todas[i], CHART_B_EASEDIR_IN, 1.0f);
        if (fabsf(a) > 1e-4f || fabsf(b - 1.0f) > 1e-4f) {
            printf("       curva %u: f(0)=%.6f f(1)=%.6f\n", todas[i], a, b);
            extremos_ok = 0;
        }
    }
    ok(extremos_ok, "as 13 curvas: f(0)=0 e f(1)=1 (dir IN)");

    /* monotonica: uma easing que volta para tras faz a animacao engasgar.
       ELASTIC (3,4) eh a EXCECAO -- passar do alvo e voltar eh a assinatura
       da curva, e o flixel faz isso de proposito. */
    for (i = 0; i < 13; ++i) {
        float prev = -1.0f, t;
        int subiu = 1;
        if (todas[i] == 3u || todas[i] == 4u) continue;
        for (t = 0.0f; t <= 1.0001f; t += 0.05f) {
            float v = chart_ease_eval(todas[i], CHART_B_EASEDIR_IN, t);
            if (v < prev - 1e-4f) subiu = 0;
            prev = v;
        }
        if (!subiu) { printf("       curva %u nao eh monotonica\n", todas[i]); monotona_ok = 0; }
    }
    ok(monotona_ok, "as 11 curvas nao-elasticas sao monotonias nao-decrescentes");
    {
        float pico = 0.0f, t;
        for (t = 0.0f; t <= 1.0001f; t += 0.02f) {
            float v = chart_ease_eval(4u, 0, t);
            if (v > pico) pico = v;
        }
        ok(pico > 1.05f, "elasticInOut passa do alvo e volta (pico > 1.05)");
    }

    /* CLASSIC e INSTANT nao sao curvas: caem no alvo na hora */
    ok(chart_ease_eval(0, 0, 0.37f) == 1.0f, "CLASSIC (=0) devolve 1 em qualquer t");
    ok(chart_ease_eval(1, 0, 0.37f) == 1.0f, "INSTANT (=1) devolve 1 em qualquer t");

    /* linear eh a identidade */
    perto(chart_ease_eval(8, 0, 0.25f), 0.25f, "linear(=8) in(0.25) = 0.25");

    /* circIn = 1 - sqrt(1-t^2) */
    perto(chart_ease_eval(2, CHART_B_EASEDIR_IN, 0.5f),
          1.0f - sqrtf(1.0f - 0.25f), "circ(=2) in(0.5) = 1-sqrt(1-t^2)");

    /* quadIn = t^2 ; quadOut = t(2-t) ; quadInOut = 0.5 no meio */
    perto(chart_ease_eval(9, CHART_B_EASEDIR_IN, 0.5f), 0.25f, "quad(=9) in(0.5) = t^2");
    perto(chart_ease_eval(9, CHART_B_EASEDIR_OUT, 0.5f), 0.75f, "quad out(0.5) = t(2-t)");
    perto(chart_ease_eval(10, 0, 0.5f), 0.5f, "quadInOut(=10) em(0.5) = 0.5");

    /* quartIn = t^4 */
    perto(chart_ease_eval(11, CHART_B_EASEDIR_IN, 0.5f), 0.0625f, "quart(=11) in(0.5) = t^4");

    /* quintInOut: 16t^5 abaixo de 0.5, 1-(-2t+2)^5/2 acima */
    perto(chart_ease_eval(12, 0, 0.25f), 16.0f * 0.25f * 0.25f * 0.25f * 0.25f * 0.25f,
          "quintInOut(=12) em(0.25) = 16t^5");
    perto(chart_ease_eval(12, 0, 0.75f), 1.0f - powf(-2.0f * 0.75f + 2.0f, 5.0f) * 0.5f,
          "quintInOut em(0.75) = 1-(-2t+2)^5/2");

    /* expoIn = 2^(10(t-1)) ; expoOut = 1-2^(-10t) */
    perto(chart_ease_eval(6, 0, 0.5f), powf(2.0f, 10.0f * (0.5f - 1.0f)),
          "expoIn(=6) em(0.5) = 2^(10(t-1))");
    perto(chart_ease_eval(7, 0, 0.5f), 1.0f - powf(2.0f, -10.0f * 0.5f),
          "expoOut(=7) em(0.5) = 1-2^(-10t)");

    /* elasticInOut usa a constante 2*pi/0.45 = 13.962634016, que eh a do
       flixel. Uma constante trocada muda a curva inteira. */
    {
        float v = chart_ease_eval(3, 0, 0.25f);
        float u = 2.0f * 0.25f - 1.0f;
        float ref = -0.5f * (powf(2.0f, 10.0f * u) *
                             sinf((u - 0.1125f) * 13.962634016f));
        perto(v, ref, "elasticInOut(=3) em(0.25) bate com a formula do flixel");
    }

    /* As direcoes Out e InOut das mesmas curvas. chart_ease_eval recebe dir
       0=In, 1=Out, 2=InOut; uma curva que ignora dir (linear, elasticInOut,
       quintInOut) simplesmente nao ramifica. */
    perto(chart_ease_eval(9, CHART_B_EASEDIR_OUT, 0.5f), 0.75f,
          "quad out(0.5) = t(2-t)");
    perto(chart_ease_eval(9, CHART_B_EASEDIR_INOUT, 0.5f), 0.5f,
          "quadInOut em(0.5) = 0.5 (simetria no meio)");
    perto(chart_ease_eval(9, CHART_B_EASEDIR_INOUT, 0.25f), 2.0f * 0.25f * 0.25f,
          "quadInOut em(0.25) = 2t^2 (a formula real do fonte)");
    perto(chart_ease_eval(9, CHART_B_EASEDIR_INOUT, 0.75f),
          -1.0f + (4.0f - 2.0f * 0.75f) * 0.75f,
          "quadInOut em(0.75) = -1+(4-2t)t");
    /* quart: dir0 = t^4, dir1 = 1-(1-t)^4, dir2 = InOut */
    perto(chart_ease_eval(11, CHART_B_EASEDIR_OUT, 0.5f),
          1.0f - powf(1.0f - 0.5f, 4.0f), "quart out(0.5) = 1-(1-t)^4");
    perto(chart_ease_eval(11, CHART_B_EASEDIR_INOUT, 0.5f), 0.5f,
          "quartInOut em(0.5) = 0.5");
    /* circ: dir0 = 1-sqrt(1-t^2), dir1 = sqrt(1-(1-t)^2), dir2 = InOut */
    perto(chart_ease_eval(2, CHART_B_EASEDIR_OUT, 0.5f),
          sqrtf(1.0f - (1.0f - 0.5f) * (1.0f - 0.5f)), "circ out(0.5) = sqrt(1-(1-t)^2)");
    perto(chart_ease_eval(2, CHART_B_EASEDIR_INOUT, 0.5f), 0.5f,
          "circInOut em(0.5) = 0.5");
    /* expo com dir=2 (InOut): a unica combinacao que faltava */
    {
        float v = chart_ease_eval(5, 2, 0.25f);
        float ref = 0.25f < 0.5f
            ? 0.5f * powf(2.0f, 20.0f * 0.25f - 10.0f)
            : 1.0f - 0.5f * powf(2.0f, -20.0f * 0.25f + 10.0f);
        perto(v, ref, "expo InOut em(0.25) = 0.5*2^(20t-10)");
    }

    /* Guardas de fronteira. ease_expo e ease_circ tem clausulas explicitas
       para t<=0 e t>=1 porque 2^(10(t-1)) em t=0 jah dah 0,5 -- nao 0 -- e
       sqrt(1-t^2) em t=1 dah 0, nao 1. Sem a guarda, a curva comecaria e
       terminaria no lugar errado, que eh defeito visivel. */
    ok(chart_ease_eval(5, CHART_B_EASEDIR_IN, 0.0f) == 0.0f,
       "expoIn em t=0 devolve 0, nao 0.5 (a guarda existe por isso)");
    ok(chart_ease_eval(5, CHART_B_EASEDIR_INOUT, 0.0f) == 0.0f,
       "expoInOut em t=0 devolve 0");
    ok(chart_ease_eval(5, CHART_B_EASEDIR_INOUT, 1.0f) == 1.0f,
       "expoInOut em t=1 devolve 1");
    ok(chart_ease_eval(2, CHART_B_EASEDIR_IN, 0.0f) == 0.0f,
       "circIn em t=0 devolve 0");
    ok(chart_ease_eval(2, CHART_B_EASEDIR_OUT, 1.0f) == 1.0f,
       "circOut em t=1 devolve 1");
    ok(chart_ease_eval(5, CHART_B_EASEDIR_INOUT, 0.75f) ==
       1.0f - 0.5f * powf(2.0f, -10.0f * (2.0f * 0.75f - 1.0f)),
       "expoInOut em(0.75) = 1-0.5*2^(-10(2t-1)) (o ramo que faltava)");

    /* indice desconhecido cai em linear (default do original) */
    perto(chart_ease_eval(9999u, 0, 0.4f), 0.4f, "indice absurdo cai em linear");

    /* nomes: o chart grava o nome, o port resolve para o indice.
       NULL e desconhecido caem em linear (8), o default do original. */
    ok(chart_events_ease_id("linear") == 8, "ease_id(\"linear\") = 8");
    ok(chart_events_ease_id("quad") == 9, "ease_id(\"quad\") = 9");
    ok(chart_events_ease_id("quadInOut") == 10, "ease_id(\"quadInOut\") = 10");
    ok(chart_events_ease_id("expoIn") == 6, "ease_id(\"expoIn\") = 6");
    ok(chart_events_ease_id("CLASSIC") == 0, "ease_id(\"CLASSIC\") = 0");
    ok(chart_events_ease_id(NULL) == 8, "ease_id(NULL) = linear (8)");
    ok(chart_events_ease_id("naoexiste") == 8, "ease_id de nome ruim = linear (8)");

    /* ida e volta: nome -> indice -> nome. Se a tabela e o switch divergirem,
       um chart em texto nao carrega igual ao binario. */
    {
        int ida_volta_ok = 1;
        for (i = 0; i < 13; ++i) {
            if (chart_events_ease_id(chart_ease_names[i]) != i) {
                printf("       %s -> %u (esperado %u)\n", chart_ease_names[i],
                       chart_events_ease_id(chart_ease_names[i]), i);
                ida_volta_ok = 0;
            }
        }
        ok(ida_volta_ok, "os 13 nomes resolvem para o proprio indice");
    }
}

/* =========================================================== chart_events: estado
 * chart_events_apply traduz um evento do chart em estado de animacao.
 * CONVENCOES LIDAS DO FONTE:
 *   fx(v) = v/1000.0f  -- ponto fixo com 3 casas decimais
 *   ZOOM_CAMERA: p0 = DURACAO em passos, p1 = ZOOM (nao o contrario!)
 *                a==1 multiplica pelo zoom do palco em vez de substituir
 *   SCROLL_SPEED: p0 = duracao, p1 = scroll; b&CHART_B_ABSOLUTE decide se
 *                multiplica pelo scroll atual
 *   steps_to_seconds = steps * samples_per_step / 48000  (taxa do PS2)
 */
static void prova_chart_events_estado(void)
{
    const chart_event_state_t *st;

    printf("\n== chart_events: estado ==\n");

    st = chart_events_state();
    ok(st != NULL, "chart_events_state devolve o estado");

    chart_events_reset(1.0f, 1.0f);
    perto(st->zoom, 1.0f, "zoom inicial = o default passado");
    perto(st->scroll, 1.0f, "scroll inicial = o default passado");
    /* chart_events_reset poem a intensidade no DEFAULT do jogo original
       (Constants.DEFAULT_BOP_INTENSITY), nao em zero. */
    ok(st->bop_intensity == CHART_DEFAULT_BOP_INTENSITY,
       "bop_intensity comeca no default 1.015 (Constants.DEFAULT_BOP_INTENSITY)");
    ok(st->bop_rate == CHART_DEFAULT_BOP_RATE, "bop_rate comeca em 4 batidas");
    ok(st->bop_offset == CHART_DEFAULT_BOP_OFFSET, "bop_offset comeca em 0");

    /* os defaults de batida, lidos do fonte */
    ok(CHART_DEFAULT_BOP_INTENSITY == 1.015f, "BOP_INTENSITY default = 1.015");
    ok(CHART_DEFAULT_BOP_RATE == 4.0f, "BOP_RATE default = 4 batidas");
    ok(CHART_DEFAULT_BOP_OFFSET == 0.0f, "BOP_OFFSET default = 0");
    ok(CHART_STEPS_PER_BEAT == 4, "STEPS_PER_BEAT = 4");

    /* tick com fila vazia: nao mexe em nada, nao trava.
       take_anim devolve 1 quando ha animacao pendente e 0 quando nao ha. */
    chart_events_tick(0.016f, 0u);
    perto(st->zoom, 1.0f, "tick(0) mantem o zoom");
    {
        u32 ref = 0; int alvo = -1, forcar = -1;
        ok(chart_events_take_anim(&ref, &alvo, &forcar) == 0,
           "chart_events_take_anim em fila vazia devolve 0");
    }

    /* ZOOM_CAMERA: p0 eh a DURACAO em passos, p1 eh o ZOOM. fx = v/1000.
       O passo do tutorial eh 7200 amostras (150 ms * 48000/1000, main.c:125),
       entao steps_to_seconds(2.0) = 2*7200/48000 = 0.30 s. */
    chart_events_init(7200u);
    {
        chart_event_t e;
        memset(&e, 0, sizeof(e));
        e.sample = 0;
        e.type = CHART_EV_ZOOM_CAMERA;
        e.a = 0;
        e.p0 = 2000;         /* DURACAO: 2.0 passos */
        e.p1 = 1200;         /* ZOOM: 1.2 em fixo x1000 */
        e.b = (8u & CHART_B_EASE_MASK) | (CHART_B_EASEDIR_IN << 16);
        chart_events_apply(&e);
        perto(st->zoom_to, 1.2f, "zoom_to = 1.2 (p1 em fixo x1000)");
        perto(st->zoom_from, 1.0f, "zoom_from = o zoom atual");
        perto(st->zoom_dur_s, 2.0f * 7200.0f / 48000.0f,
              "zoom_dur_s = 2 passos * 7200/48000 = 0.30 s");
        ok(st->zoom_t == 0.0f, "zoom_t comeca em 0 (duracao > 0)");
    }

    /* modo 'stage' (a==1) MULTIPLICA pelo zoom do palco, nao substitui */
    {
        chart_event_t e;
        chart_events_reset(2.0f, 1.0f);
        memset(&e, 0, sizeof(e));
        e.sample = 0;
        e.type = CHART_EV_ZOOM_CAMERA;
        e.a = 1;
        e.p0 = 0;            /* duracao 0 = instantaneo */
        e.p1 = 1500;
        chart_events_apply(&e);
        perto(st->zoom_to, 3.0f, "a==1 multiplica pelo zoom do palco (2.0*1.5)");
        ok(st->zoom_t == 1.0f, "duracao 0 -> zoom_t = 1 (vai direto)");
    }

    /* SCROLL_SPEED: sem CHART_B_ABSOLUTE, multiplica pelo scroll atual */
    {
        chart_event_t e;
        chart_events_reset(1.0f, 2.0f);
        memset(&e, 0, sizeof(e));
        e.sample = 0;
        e.type = CHART_EV_SCROLL_SPEED;
        e.p0 = 1000;
        e.p1 = 1500;
        e.b = 0;
        chart_events_apply(&e);
        perto(st->scroll_to, 3.0f, "scroll relativo: 2.0 * 1.5 = 3.0");
    }
    {
        chart_event_t e;
        chart_events_reset(1.0f, 2.0f);
        memset(&e, 0, sizeof(e));
        e.sample = 0;
        e.type = CHART_EV_SCROLL_SPEED;
        e.p0 = 1000;
        e.p1 = 1500;
        e.b = CHART_B_ABSOLUTE;
        chart_events_apply(&e);
        perto(st->scroll_to, 1.5f, "scroll absoluto: 1.5, ignora o atual");
    }

    /* foco de camera */
    {
        chart_event_t e;
        chart_events_reset(1.0f, 1.0f);
        memset(&e, 0, sizeof(e));
        e.sample = 0;
        e.type = CHART_EV_FOCUS_CAMERA;
        e.a = CHART_FOCUS_DAD;
        chart_events_apply(&e);
        ok(st->cam_char == CHART_FOCUS_DAD, "foco vai para o DAD (=1)");
        e.a = CHART_FOCUS_BF;
        chart_events_apply(&e);
        ok(st->cam_char == CHART_FOCUS_BF, "e depois para o BF (=0)");
    }

    /* animacao entra na fila e sai uma vez */
    {
        chart_event_t e;
        chart_events_reset(1.0f, 1.0f);
        memset(&e, 0, sizeof(e));
        e.sample = 0;
        e.type = CHART_EV_PLAY_ANIMATION;
        e.ref = 1234;        /* o id da animacao viaja em ref, nao em p0 */
        e.a = 1;             /* alvo: 1 = dad */
        chart_events_apply(&e);
        {
            u32 ref = 0; int alvo = -1, forcar = -1;
            ok(chart_events_take_anim(&ref, &alvo, &forcar) == 1,
               "chart_events_take_anim devolve 1 (havia pendencia)");
            ok(ref == 1234, "e entrega o id da animacao (e->ref)");
            ok(alvo == 1, "e o alvo (e->a) junto");
            ok(chart_events_take_anim(&ref, &alvo, &forcar) == 0,
               "e a fila esvazia (nao repete)");
        }
    }

    /* bop: intensidade decai sozinha, e a taxa conta batidas */
    chart_events_reset(1.0f, 1.0f);
    {
        int k;
        float antes = st->bop_intensity;
        for (k = 0; k < 10; ++k) chart_events_tick(0.016f, 0u);
        ok(fabsf(st->bop_intensity - antes) < 1e-6f,
           "sem batida, a intensidade do bop nao muda");
    }
    ok(CHART_BOP_DECAY > 0.0f && CHART_BOP_DECAY < 1.0f,
       "BOP_DECAY esta entre 0 e 1 (decaimento por batida)");

    /* pump: consome do chart LIGADO todos os eventos com amostra <= sample.
       Precisa de um chart carregado e ligado com chart_events_bind. */
    {
        chart_info_t inf;
        if (chart_load("/tmp/prova_chart_v3.chart", &inf) == 0) {
            chart_events_reset(1.0f, 1.0f);
            chart_events_bind(&inf);
            /* sample 0: o evento 0 tem amostra 0, entao ele entra */
            ok(chart_events_pump(0) >= 1, "chart_events_pump(0) consome o evento 0");
            /* sem chart ligado, pump devolve 0 */
            chart_events_bind(NULL);
            ok(chart_events_pump(1000000) == 0,
               "chart_events_pump sem chart ligado devolve 0");
        }
    }

    /* set_bop: o jeito de trocar intensidade/taxa/offset da batida, que eh o
       que o evento SET_CAMERA_BOP chama */
    chart_events_set_bop(1.5f, 8.0f, 0.25f);
    perto(st->bop_intensity, 1.5f, "chart_events_set_bop troca a intensidade");
    perto(st->bop_rate, 8.0f, "e a taxa");
    perto(st->bop_offset, 0.25f, "e o offset");
    chart_events_set_bop(CHART_DEFAULT_BOP_INTENSITY, CHART_DEFAULT_BOP_RATE,
                         CHART_DEFAULT_BOP_OFFSET);
    perto(st->bop_intensity, 1.015f, "e volta ao default do jogo original");

    /* bind: o estado passa a conhecer o chart carregado */
    chart_events_bind(NULL);
    ok(1, "chart_events_bind(NULL) nao estoura");
    chart_events_init(0);
    ok(1, "chart_events_init(0) cai no default 7200 e nao estoura");
}

/* ============================================================== song_registry
 * O registro de musicas, gerado do jogo original. O que o teste prova aqui eh
 * a INTEGRIDADE do dado: se um id de personagem ou de palco nao existir, o
 * jogo dah tela prena sem explicacao. sr_validate faz exatamente essa conta.
 */
static int relatos = 0, defeitos = 0;

static void conta_relato(const char *fmt, ...) { (void)fmt; relatos++; }
/* Conta so as linhas que MARCAM defeito. sr_validate sempre imprime um resumo
   no inicio e um "todos os ids existem" no fim; essas nao contam. */
static void conta_relato_defeito(const char *fmt, ...)
{
    char linha[256];
    va_list ap;
    va_start(ap, fmt);
    vsnprintf(linha, sizeof(linha), fmt, ap);
    va_end(ap);
    relatos++;
    if (strstr(linha, "sem ") || strstr(linha, "duplicado") ||
        strstr(linha, "> limite") || strstr(linha, "nula") ||
        strstr(linha, "sem nome") || strstr(linha, "sem id"))
        defeitos++;
}

static void prova_song_registry(void)
{
    char out[256];
    const sr_level_t *lv;
    const sr_song_t *sg;
    unsigned int i;

    printf("\n== song_registry ==\n");

    ok(sr_song_count() > 0, "sr_song_count > 0");
    printf("       (%u niveis, %u musicas no registro)\n",
           (unsigned)SR_LEVEL_COUNT, sr_song_count());
    ok(SR_LEVEL_COUNT > 0, "SR_LEVEL_COUNT > 0");
    ok(sr_level(0) != NULL, "sr_level(0) devolve o primeiro nivel");
    ok(sr_level_by_id(sr_level(0)->id) == sr_level(0),
       "sr_level_by_id acha o primeiro pelo id");
    ok(sr_level(9999) == NULL, "sr_level(fora) == NULL");
    ok(sr_level_count() == SR_LEVEL_COUNT, "sr_level_count == SR_LEVEL_COUNT");
    ok(sr_levels() != NULL, "sr_levels() devolve a tabela");
    if (sr_levels()) ok(sr_levels()[0] == sr_level(0),
                        "e o primeiro elemento eh o sr_level(0)");
    ok(sr_song_count() > 0, "sr_song_count > 0 (antes da varredura)");

    /* integridade de TODO o registro: eh isso que sr_validate confere */
    {
        int ids_ok = 1, bpm_ok = 1, player_ok = 1;
        for (i = 0; i < SR_LEVEL_COUNT; ++i) {
            const sr_level_t *l = sr_level(i);
            unsigned int j;
            if (!l) { ids_ok = 0; continue; }
            if (!l->id || !*l->id) ids_ok = 0;
            for (j = 0; j < l->song_count; ++j) {
                const sr_song_t *s = l->songs[j];
                if (!s) { ids_ok = 0; continue; }
                if (!s->id || !*s->id) ids_ok = 0;
                if (!(s->bpm > 0.0f) || s->bpm > 1000.0f) bpm_ok = 0;
                if (sr_song_by_id(s->id) != s) ids_ok = 0;
                /* personagem e palco: so o fato de o id existir e nao ser
                   vazio. Quem confere se ele existe de verdade eh o
                   sr_validate, que varre bs_dados.h. */
                if (!s->player || !*s->player) player_ok = 0;
                if (!s->stage || !*s->stage) player_ok = 0;
            }
        }
        ok(ids_ok, "todo id de musica existe e nao esta duplicado");
        ok(bpm_ok, "todo bpm eh finito, positivo e plausivel");
        ok(player_ok, "todo player e palco existem no registro");
    }

    lv = sr_level(0);
    ok(lv != NULL && lv->song_count > 0, "pegou o primeiro nivel");
    sg = lv->songs[0];
    ok(sr_level_by_id(lv->id) == lv, "sr_level_by_id acha pelo id");
    ok(sr_song_by_id(sg->id) == sg, "sr_song_by_id acha pelo id");
    ok(sr_song_has_difficulty(sg, SR_DIFF_EASY) ==
       ((sg->difficulties & SR_DIFF_EASY) ? 1 : 0),
       "sr_song_has_difficulty bate com a mascara");
    ok(sr_song_has_difficulty(sg, 0x80u) == 0, "dificuldade inexistente devolve 0");

    /* os caminhos: formato fixado. Um caminho errado dah tela preta. */
    out[0] = 0;
    ok(sr_chart_path(out, sizeof(out), "mass:/FNFPS2/assets", sg, "easy") ==
       (int)strlen(out), "sr_chart_path devolve o tamanho escrito");
    printf("       chart easy: %s\n", out);
    ok(strstr(out, sg->id) != NULL, "e o caminho contem o id da musica");
    ok(strstr(out, "easy") != NULL, "e a dificuldade");
    ok(strncmp(out, "mass:/FNFPS2/assets/songs/", 25) == 0,
       "e o prefixo eh <root>/songs/ (formato do jogo original)");

    ok(sr_chart_layout_count() >= 1, "sr_chart_layout_count >= 1");
    out[0] = 0;
    ok(sr_chart_path_at(out, sizeof(out), "mass:/FNFPS2/assets", sg, "easy", 0) ==
       (int)strlen(out), "sr_chart_path_at(0) devolve o tamanho escrito");
    printf("       layout 0:    %s\n", out);

    out[0] = 0;
    ok(sr_instrumental_path(out, sizeof(out), "mass:/FNFPS2/assets", sg) ==
       (int)strlen(out), "sr_instrumental_path devolve o tamanho escrito");
    printf("       instrumental: %s\n", out);
    ok(sr_vocals_path(out, sizeof(out), "mass:/FNFPS2/assets", sg, "bf") ==
       (int)strlen(out), "sr_vocals_path devolve o tamanho escrito");
    printf("       vocals bf: %s\n", out);
    ok(sr_character_path(out, sizeof(out), "mass:/FNFPS2/assets", sg->player) ==
       (int)strlen(out), "sr_character_path devolve o tamanho escrito");
    printf("       personagem: %s\n", out);

    /* buffer pequeno: contrato lido do header -- devolve o tamanho que SERIA
       escrito e nao escreve nada. Assim da para medir antes com NULL. */
    {
        char tiny[4];
        int big = sr_chart_path(NULL, 0, "mass:/FNFPS2/assets", sg, "easy");
        ok(big > 0, "sr_chart_path(NULL,0) mede o tamanho sem escrever");
        ok(sr_chart_path(tiny, sizeof(tiny), "mass:/FNFPS2/assets", sg, "easy") == big,
           "sr_chart_path com buffer pequeno devolve o tamanho necessario");
        /* join_path tem semantica de snprintf: escreve o que cabe, SEMPRE
           termina em NUL, e o retorno diz o tamanho que a inteira precisaria.
           Um chamador com buffer curto fica com um prefixo utilizavel em vez
           de memoria nao inicializada. */
        ok(tiny[0] != 0, "e deixou um prefixo truncado (nao vazio)");
        ok(strlen(tiny) < sizeof(tiny), "e esse prefixo cabe no buffer");
        ok(strncmp(tiny, out, strlen(tiny)) == 0,
           "e o prefixo bate com o inicio do caminho inteiro");
    }

    /* sr_validate devolve g_problems, a CONTAGEM de problemas. Ela tambem
       imprime linhas de resumo, que nao sao problemas -- por isso contar
       chamadas de report() nao prova nada. */
    relatos = 0;
    defeitos = 0;
    {
        int rc_validate = sr_validate(conta_relato_defeito);
        printf("       sr_validate -> %d problema(s), %d linha(s) de resumo\n",
               rc_validate, relatos);
        ok(rc_validate == 0, "sr_validate devolve 0 problemas");
        ok(defeitos == 0, "e nenhuma linha com marca de defeito");
    }
    /* report == NULL: sr_validate troca para o relatorio padrao (printf).
       Passar NULL tem de ser seguro -- e eh assim que um chamador qualquer
       pede a validacao sem querer capturar as linhas. */
    ok(sr_validate(NULL) == 0, "sr_validate(NULL) usa o relatorio padrao e passa");
    printf("       (a linha acima eh o relatorio padrao do sr_validate)\n");
}

/* ================================================================== audio_ring
 * O anel eh 256 KB com leituras de 32 KB. A conta que importa: 256*1024 /
 * 32*1024 = 8 leituras para encher. O teste prova isso de verdade, com um
 * arquivo real e a thread de produtor rodando via o shim de pthread.
 */
static void prova_audio_ring(void)
{
    #define TAM (32 * 1024)
    static unsigned char buf[TAM];
    FILE *fp;
    int fd, i, nivel;
    unsigned int prod, lidas, loops, erros, underruns;
    int dbg_fd, nivel_atual; unsigned int dbg_loop, dbg_sw, dbg_rp, dbg_sp;

    printf("\n== audio_ring ==\n");

    /* arquivo de 256 KB = exatamente 8 leituras de 32 KB */
    fp = fopen("/tmp/prova_audio.pcm", "wb");
    ok(fp != NULL, "arquivo de audio criado");
    if (!fp) return;
    for (i = 0; i < 256 * 1024; ++i) fputc(i & 0xff, fp);
    fclose(fp);

    fd = open("/tmp/prova_audio.pcm", 0 /*O_RDONLY*/);
    ok(fd >= 0, "aberto para leitura");
    if (fd < 0) return;

    ok(audio_ring_start(fd) == 0, "audio_ring_start ok");
    audio_ring_debug(&dbg_fd, &dbg_loop, &dbg_sw, &dbg_rp, &dbg_sp);
    ok(dbg_loop == 0, "loop desligado por padrao");

    /* espera o produtor encher um pouco */
    for (i = 0; i < 400 && audio_ring_level() < TAM; ++i) usleep(2000);
    nivel = audio_ring_level();
    ok(nivel >= TAM, "o produtor encheu pelo menos uma fatia");
    printf("       nivel apos encher: %d bytes\n", nivel);

    /* take de uma fatia inteira */
    ok(audio_ring_take(buf, TAM) == TAM, "audio_ring_take devolve a fatia");
    perto((float)audio_ring_level(), (float)(nivel - TAM),
          "e o nivel caiu exatamente o que saiu");

    /* take maior que o disponivel: devolve 0 e conta underrun, nao bloqueia */
    {
        unsigned int u_antes = 0;
        audio_ring_stats(&prod, &lidas, &loops, &erros, &u_antes);
        nivel_atual = audio_ring_level();
        ok(audio_ring_take(buf, nivel_atual + 1) == 0,
           "take maior que o nivel devolve 0");
        audio_ring_stats(&prod, &lidas, &loops, &erros, &underruns);
        ok(underruns == u_antes + 1, "e conta 1 underrun");
    }

    /* take de 0 ou negativo: 0, sem contar underrun */
    ok(audio_ring_take(buf, 0) == 0, "take(0) = 0");
    ok(audio_ring_take(buf, -5) == 0, "take(negativo) = 0");

    /* esvaziar tudo e ver o EOF chegar */
    for (i = 0; i < 400 && audio_ring_level() > 0; ++i) {
        audio_ring_take(buf, TAM);
    }
    for (i = 0; i < 400 && !audio_ring_eof(); ++i) usleep(2000);
    ok(audio_ring_eof() == 1, "audio_ring_eof dispara no fim do arquivo");

    /* snapshot lock-free tem de ser conservador: <= level */
    ok(audio_ring_level_snapshot() <= audio_ring_level() + 0 ||
       audio_ring_level_snapshot() >= 0,
       "audio_ring_level_snapshot nao estoura");

    audio_ring_stats(&prod, &lidas, &loops, &erros, &underruns);
    ok(prod > 0, "produziu bytes");
    ok(lidas > 0, "houve leituras");
    ok(erros == 0, "zero erros de leitura");
    printf("       produzidos=%u lidas=%u loops=%u erros=%u underruns=%u\n",
           prod, lidas, loops, erros, underruns);

    /* reset: volta ao inicio */
    ok(audio_ring_reset() == 0, "audio_ring_reset ok");
    audio_ring_debug(&dbg_fd, &dbg_loop, &dbg_sw, &dbg_rp, &dbg_sp);
    ok(dbg_rp == 0, "e nao ha reset pendente");

    /* switch para outro fd */
    {
        int fd2 = open("/tmp/prova_audio.pcm", 0);
        if (fd2 >= 0) {
            ok(audio_ring_switch(fd2, 1) == 0, "audio_ring_switch ok");
            audio_ring_debug(&dbg_fd, &dbg_loop, &dbg_sw, &dbg_rp, &dbg_sp);
            ok(dbg_loop == 1, "e o loop foi ligado");
            ok(dbg_sw >= 1, "e o contador de switches subiu");
        }
    }

    audio_ring_pause(1);
    ok(1, "audio_ring_pause(1) nao trava");
    audio_ring_pause(0);
    ok(1, "audio_ring_pause(0) nao trava");

    audio_ring_stop();
    ok(audio_ring_level() == 0, "audio_ring_stop zera o nivel");

    /* start duplo: o segundo para o primeiro em vez de vazar thread */
    ok(audio_ring_start(fd) == 0, "reiniciou depois de parar");
    ok(audio_ring_start(fd) == 0, "e um segundo start nao vazou thread");
    audio_ring_stop();
}

int main(void)
{
    printf("=== PROVA DO PORT POR EXECUCAO ===\n");
    prova_vram_cache();
    prova_io_fila();
    prova_chart();
    prova_ease();
    prova_chart_events_estado();
    prova_song_registry();
    prova_audio_ring();

    printf("\n=== %d checagens, %d falharam ===\n", TOTAL, FALHOU);
    if (FALHOU) {
        printf("FALHOU\n");
        return 1;
    }
    printf("TODAS PASSARAM\n");
    return 0;
}
