import base64
import hashlib
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encryptItem(masterKey, item):
    f = Fernet(masterKey)
    token = f.encrypt(item.encode())
    return token

def decryptItem(masterKey, item):
    f = Fernet(masterKey)
    token = f.decrypt(item)
    return token.decode()

def createMasterKey(masterPW, deviceSecret):
    password = masterPW.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=deviceSecret,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key
def athorize(enteredPW, hashedMP):
    hashedEntered = hashlib.sha256(enteredPW.encode()).hexdigest()
    return hashedEntered == hashedMP