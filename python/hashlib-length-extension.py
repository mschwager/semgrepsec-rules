import hashlib
import os


SECRET = os.urandom(16)
application_key_value = SECRET

# ruleid: hashlib-length-extension
h1 = hashlib.sha224(SECRET + b"message")

# ruleid: hashlib-length-extension
h2 = hashlib.sha1()
h2.update(SECRET)
h2.update(b"message")

# ruleid: hashlib-length-extension
h3 = hashlib.new("md5")
h3.update(SECRET)
h3.update(b"message")

# ruleid: hashlib-length-extension
h4 = hashlib.sha1(application_key_value + b"message")

# ok: hashlib-length-extension
h5 = hashlib.sha3_256(SECRET + b"message")
