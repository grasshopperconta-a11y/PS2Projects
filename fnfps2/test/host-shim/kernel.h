/* kernel.h -- shim de HOST.
 *
 * Existe para uma coisa so: compilar e RODAR os modulos do port fora do PS2,
 * para que os testes provem o comportamento por execucao em vez de por
 * leitura. Nao implementa o PS2: implementa o bastante das primitivas que o
 * port usa, com a semantica que o port depende.
 *
 * A semantica importa. CreateSema/WaitSema/SignalSema viram um mutex de
 * pthread porque o port os usa EXATAMENTE como um mutex (contagem 1, max 1,
 * option 0). CreateThread/StartThread viram pthread_create. DelayThread(us)
 * vira usleep. ExitThread vira pthread_exit.
 *
 * Se um dia o port usar semaforo como contador, este shim mente -- e o teste
 * que depende disso passa a valer menos que nenhum. Esta anotado para que
 * quem estender saiba o que esta assumindo.
 */
#ifndef HOST_SHIM_KERNEL_H
#define HOST_SHIM_KERNEL_H

#include <tamtypes.h>
#include <pthread.h>

typedef struct {
    int init_count;
    int max_count;
    int option;
    /* estado real do shim, fora do que o PS2 teria */
    pthread_mutex_t m;
    int criado;
} ee_sema_t;

typedef struct {
    void (*func)(void *);
    void *stack;
    int stack_size;
    void *gp_reg;
    int initial_priority;
    /* estado real do shim */
    pthread_t tid;
    pthread_attr_t attr;
    void *arg;
    int lancada;
} ee_thread_t;

int  CreateSema(ee_sema_t *s);
int  DeleteSema(int id);
int  WaitSema(int id);
int  SignalSema(int id);
int  CreateThread(ee_thread_t *t);
int  StartThread(int id, void *arg);
int  DeleteThread(int id);
void ExitThread(void);
int  TerminateThread(int id);

/* O port guarda o id do semaforo/thread em um int. Como o shim precisa do
   objeto de verdade, devolve um indireto: o id negativo-signalizado. A
   convencao aqui eh que CreateSema devolve o INDICE no vetor abaixo, e o
   port o trata como opaco -- que eh tudo que ele faz. */
#define HOST_SHIM_MAX 8
extern ee_sema_t  *host_semas[HOST_SHIM_MAX];
extern ee_thread_t *host_threads[HOST_SHIM_MAX];

#endif
