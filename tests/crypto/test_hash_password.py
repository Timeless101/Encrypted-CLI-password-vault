import src.crypto as crypto

def test_hash_password_function():
    password_hash, password_salt,encryption_salt = crypto.hash_password("Hello")
    assert isinstance(password_hash, bytes) is True
    assert isinstance(password_salt, bytes) is True
    assert isinstance(encryption_salt, bytes) is True