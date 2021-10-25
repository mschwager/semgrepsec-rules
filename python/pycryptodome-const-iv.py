import os

import Crypto


# ok: pycryptodome-const-iv
cipher = Crypto.Cipher.DES3.new(key, Crypto.Cipher.DES3.MODE_CBC, iv=os.urandom(16))

# ruleid: pycryptodome-const-iv
cipher = Crypto.Cipher.DES3.new(key, Crypto.Cipher.DES3.MODE_CBC, iv=b"aaaaaaaaaaaaaaaa")

# ok: pycryptodome-const-iv
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CTR, nonce=os.urandom(16))

# ruleid: pycryptodome-const-iv
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CTR, nonce=b"aaaaaaaaaaaaaaaa")

# ok: pycryptodome-const-iv
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CFB, iv=os.urandom(16))

# ruleid: pycryptodome-const-iv
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CFB, iv=b"aaaaaaaaaaaaaaaa")

# ok: pycryptodome-const-iv
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_OFB, iv=os.urandom(16))

# ruleid: pycryptodome-const-iv
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_OFB, iv=b"aaaaaaaaaaaaaaaa")

# ok: pycryptodome-const-iv
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_OPENPGP, iv=os.urandom(16))

# ruleid: pycryptodome-const-iv
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_OPENPGP, iv=b"aaaaaaaaaaaaaaaa")
