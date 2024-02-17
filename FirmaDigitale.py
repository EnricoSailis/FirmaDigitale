# pip install cryptography
# an actual example of sign and verify

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
import cryptography

def rsa_keypair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    return (private_key, private_key.public_key())

def sign(message, private_key):
    padding_instance = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)
    return base64.b64encode(private_key.sign(message, padding_instance, hashes.SHA256()))

def verify(message, signature, public_key):
    sig = base64.b64decode(signature)
    padding_instance = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)
    try:
        public_key.verify(sig, message, padding_instance, hashes.SHA256())
        return True
    except cryptography.exceptions.InvalidSignature:
        return False

pvt1, pub1 = rsa_keypair()
pvt2, _    = rsa_keypair()

msg = b"Hello you!"
sig1 = sign(msg, pvt1) # signed with private key
sig2 = sign(msg, pvt2) # signed with *other* private key

res = verify(msg, sig1, pub1)
print(res)                    # True:  ok...     signed with the private key related to public key pub1
res = verify(msg, sig2, pub1)
print(res)                    # False: no! *not*