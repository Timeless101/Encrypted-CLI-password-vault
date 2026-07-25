from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.fernet import Fernet
import cryptography
import os


def password_decryption(password):
    pass
    
#Password encryption.
def hash_password(password: str):

    salt = os.urandom(16)
    password = password.encode("utf-8")

    kdf = Argon2id(
            salt=salt,
            length=64,
            iterations=2,
            lanes=4,
            memory_cost=512*1024, #512 MiB RAM
            ad=None,
            secret=None
        )

    return kdf.derive(password), salt

#Check password
def verify_password(input_password: str, database_password: bytes, salt: bytes):
    kdf = Argon2id(
                salt=salt,
                length=64,
                iterations=2,
                lanes=4,
                memory_cost=512*1024, #512 MiB RAM
                ad=None,
                secret=None
            )

    try:
        if kdf.verify(input_password.encode("utf-8"), database_password) is None:
            return True

    except cryptography.exceptions.InvalidKey:
        return False

if __name__ == "__main__":
    ...