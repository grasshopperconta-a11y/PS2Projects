/* host_thread_stubs.c -- implementacao das primitivas de thread do shim.
 *
 * So para os testes de host. NAO entra no build do PS2 (o Makefile nao o
 * referencia; ele eh compilado a mao pelos testes).
 */
#include "kernel.h"
#include <string.h>
#include <stdlib.h>

ee_sema_t   *host_semas[HOST_SHIM_MAX];
ee_thread_t *host_threads[HOST_SHIM_MAX];

/* audio_ring.c declara "extern void *_gp" e o passa para CreateThread: eh o
   global pointer do MIPS, que so existe no PS2. No host nao ha -- e sem ele o
   link falha. Um endereco qualquer basta: o shim de thread nao o usa. */
void *_gp = 0;

int CreateSema(ee_sema_t *s)
{
    int i;
    if (!s) return -1;
    for (i = 0; i < HOST_SHIM_MAX; ++i)
        if (!host_semas[i]) break;
    if (i == HOST_SHIM_MAX) return -1;
    /* O kernel do PS2 copia a struct do chamador; audio_ring_start_loop usa
       um ee_sema_t de PILHA, entao guardar &s penduraria assim que a funcao
       retornasse. O shim guarda uma copia propria. */
    pthread_mutex_init(&s->m, NULL);
    s->criado = 1;
    host_semas[i] = malloc(sizeof(ee_sema_t));
    if (!host_semas[i]) return -1;
    *host_semas[i] = *s;
    return i;
}

int DeleteSema(int id)
{
    if (id < 0 || id >= HOST_SHIM_MAX || !host_semas[id]) return -1;
    pthread_mutex_destroy(&host_semas[id]->m);
    free(host_semas[id]);
    host_semas[id] = NULL;
    return 0;
}

int WaitSema(int id)
{
    if (id < 0 || id >= HOST_SHIM_MAX || !host_semas[id]) return -1;
    pthread_mutex_lock(&host_semas[id]->m);
    return 0;
}

int SignalSema(int id)
{
    if (id < 0 || id >= HOST_SHIM_MAX || !host_semas[id]) return -1;
    pthread_mutex_unlock(&host_semas[id]->m);
    return 0;
}

static void *host_trampolim(void *arg)
{
    ee_thread_t *t = (ee_thread_t *)arg;
    t->func(t->arg);
    return NULL;
}

int CreateThread(ee_thread_t *t)
{
    int i;
    if (!t || !t->func) return -1;
    for (i = 0; i < HOST_SHIM_MAX; ++i)
        if (!host_threads[i]) break;
    if (i == HOST_SHIM_MAX) return -1;
    /* Mesma historia do semaforo: copia propria, nao ponteiro para a pilha
       de quem chamou. */
    pthread_attr_init(&t->attr);
    pthread_attr_setdetachstate(&t->attr, PTHREAD_CREATE_JOINABLE);
    host_threads[i] = malloc(sizeof(ee_thread_t));
    if (!host_threads[i]) return -1;
    *host_threads[i] = *t;
    host_threads[i]->lancada = 0;
    return i;
}

int StartThread(int id, void *arg)
{
    ee_thread_t *t;
    if (id < 0 || id >= HOST_SHIM_MAX || !host_threads[id]) return -1;
    t = host_threads[id];
    t->arg = arg;
    if (pthread_create(&t->tid, &t->attr, host_trampolim, t) != 0) return -1;
    t->lancada = 1;
    return 0;
}

int DeleteThread(int id)
{
    ee_thread_t *t;
    if (id < 0 || id >= HOST_SHIM_MAX || !host_threads[id]) return -1;
    t = host_threads[id];
    if (t->lancada) pthread_join(t->tid, NULL);
    pthread_attr_destroy(&t->attr);
    t->lancada = 0;
    free(t);
    host_threads[id] = NULL;
    return 0;
}

void ExitThread(void) { pthread_exit(NULL); }

int TerminateThread(int id)
{
    ee_thread_t *t;
    if (id < 0 || id >= HOST_SHIM_MAX || !host_threads[id]) return -1;
    t = host_threads[id];
    if (t->lancada) {
        pthread_cancel(t->tid);
        pthread_join(t->tid, NULL);
        t->lancada = 0;
    }
    free(t);
    host_threads[id] = NULL;
    return 0;
}
