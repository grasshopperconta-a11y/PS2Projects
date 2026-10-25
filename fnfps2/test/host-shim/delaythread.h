/* delaythread.h -- shim de host. DelayThread(us) -> usleep. */
#ifndef HOST_SHIM_DELAYTHREAD_H
#define HOST_SHIM_DELAYTHREAD_H
#include <unistd.h>
static inline void DelayThread(int us) { if (us > 0) usleep((unsigned)us); }
#endif
