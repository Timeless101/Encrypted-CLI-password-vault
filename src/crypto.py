from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.fernet import Fernet
import cryptography
import os
from time import sleep


def password_encryption(password: str) -> bool:

    pass


#Hash password.
def hash_password(password: str) -> tuple:

    salt: bytes = os.urandom(16)
    password: bytes = password.encode("utf-8")

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

#Check password to hash.
def verify_password(input_password: str, database_password: bytes, salt: bytes) -> bool:
    
    kdf: bytes = Argon2id(
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