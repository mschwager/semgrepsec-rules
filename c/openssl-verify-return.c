#include <openssl/x509_vfy.h>

int main () {
    X509_STORE_CTX *ctx = X509_STORE_CTX_new();

    // ruleid: openssl-verify-return
    if (X509_verify_cert(ctx)) {
        return 0;
    }

    // ok: openssl-verify-return
    if (X509_verify_cert(ctx) == 0) {
        return 0;
    }

    // ruleid: openssl-verify-return
    if (X509_STORE_CTX_verify(ctx)) {
        return 0;
    }

    // ok: openssl-verify-return
    if (X509_STORE_CTX_verify(ctx) == 0) {
        return 0;
    }

    return 1;
}
