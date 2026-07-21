import src.crypto as crypto

def test_hash_password_function():
    assert isinstance(crypto.hash_password("Hello"), bytes) is True