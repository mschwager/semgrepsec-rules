import os

import cryptography


# ok: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.CBC(os.urandom(16))

# ruleid: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.CBC(b"aaaaaaaaaaaaaaaa")

# ok: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.CTR(os.urandom(16))

# ruleid: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.CTR(b"aaaaaaaaaaaaaaaa")

# ok: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.OFB(os.urandom(16))

# ruleid: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.OFB(b"aaaaaaaaaaaaaaaa")

# ok: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.CFB(os.urandom(16))

# ruleid: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.CFB(b"aaaaaaaaaaaaaaaa")

# ok: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.CFB8(os.urandom(16))

# ruleid: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.CFB8(b"aaaaaaaaaaaaaaaa")

# ok: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.GCM(os.urandom(16))

# ruleid: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.modes.GCM(b"aaaaaaaaaaaaaaaa")

# ok: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.algorithms.ChaCha20(os.urandom(16), os.urandom(16))

# ruleid: cryptography-const-iv
cryptography.hazmat.primitives.ciphers.algorithms.ChaCha20(os.urandom(16), b"aaaaaaaaaaaaaaaa")

# ok: cryptography-const-iv
cryptography.hazmat.primitives.poly1305.Poly1305(os.urandom(16))

# ruleid: cryptography-const-iv
cryptography.hazmat.primitives.poly1305.Poly1305(b"aaaaaaaaaaaaaaaa")

key = cryptography.hazmat.primitives.ciphers.aead.ChaCha20Poly1305.generate_key()

# ok: cryptography-const-iv
chacha_tn = cryptography.hazmat.primitives.ciphers.aead.ChaCha20Poly1305(key)
ct = chacha_tn.encrypt(os.urandom(16), b"a secret message", b"authenticated but unencrypted data")

# ruleid: cryptography-const-iv
chacha_tp = cryptography.hazmat.primitives.ciphers.aead.ChaCha20Poly1305(key)
ct = chacha_tp.encrypt(b"aaaaaaaaaaaaaaaa", b"a secret message", b"authenticated but unencrypted data")

key = cryptography.hazmat.primitives.ciphers.aead.AESGCM.generate_key(bit_length=128)

# ok: cryptography-const-iv
aesgcm_tn = cryptography.hazmat.primitives.ciphers.aead.AESGCM(key)
ct = aesgcm_tn.encrypt(os.urandom(16), b"a secret message", b"authenticated but unencrypted data")

# ruleid: cryptography-const-iv
aesgcm_tp = cryptography.hazmat.primitives.ciphers.aead.AESGCM(key)
ct = aesgcm_tp.encrypt(b"aaaaaaaaaaaaaaaa", b"a secret message", b"authenticated but unencrypted data")

key = cryptography.hazmat.primitives.ciphers.aead.AESCCM.generate_key(bit_length=128)

# ok: cryptography-const-iv
aesccm_tn = cryptography.hazmat.primitives.ciphers.aead.AESCCM(key)
ct = aesccm_tn.encrypt(os.urandom(16), b"a secret message", b"authenticated but unencrypted data")

# ruleid: cryptography-const-iv
aesccm_tp = cryptography.hazmat.primitives.ciphers.aead.AESCCM(key)
ct = aesccm_tp.encrypt(b"aaaaaaaaaaaaaaaa", b"a secret message", b"authenticated but unencrypted data")
