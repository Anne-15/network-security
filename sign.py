import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

#creating private key
def keys():
    length = 1024
    privateKey = RSA.generate(length, Random.new().read)
    publicKey = privateKey.publicKey()
    return privateKey, publicKey

#function for encryption
def encrypt(Rpublic, text):
    cipher = Rpublic.encrypt(text,32)[0]
    b64cipher = base64.b64encode(cipher)
    return text

#
def sign(privateKey, data):
    return base64.b64encode(str((privateKey.sign(data,''))[0]).encode())

def verify(publicKey, data, sign):
    return publicKey.verify(data, (int(base64.b64encode(sign)),))

