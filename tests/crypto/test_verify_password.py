from src.crypto import verify_password

def test_verify_password_password_match_database():
    assert verify_password(input_password="password", database_password=b"$2b$12$umKAEmrj.MEyz1asstb22uVbeq6QpoCxbT0BgeIkv0Ai3xtZ5KISe") is True

def test_verify_password_password_mismatch():
    assert verify_password(input_password="diego", database_password=b"$2b$12$umKAEmrj.MEyz1asstb22uVbeq6QpoCxbT0BgeIkv0Ai3xtZ5KISe") is False