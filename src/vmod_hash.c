#include "bin/varnishd/cache.h"

int
init_function(struct vmod_priv *priv, const struct VCL_conf *conf)
{
    return (0);
}

const char *
vmod_get_req_hash(struct sess *sp)
{
    int u          = WS_Reserve(sp->wrk->ws, 0);
    char *req_hash = (char *) sp->wrk->ws->f;

    for (int i = 0; i < DIGEST_LEN; i++) {
        sprintf(req_hash + 2 * i, "%02x", sp->digest[i]);
    }

    WS_Release(sp->wrk->ws, DIGEST_LEN * 2 + 1);

    return (req_hash);
}
