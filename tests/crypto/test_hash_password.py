import src.crypto as crypto

def test_hash_password_function():
    password, salt = crypto.hash_password("Hello")
    assert isinstance(password, bytes) is True
    assert isinstance(salt, bytes) is True