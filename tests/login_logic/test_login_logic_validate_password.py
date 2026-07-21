import src.login_logic as login_logic
import src.crypto as crypto

def test_validate_password_happy_test(monkeypatch):
    def fake_verify_Password(input_password, database_password):
        return True
    
    monkeypatch.setattr(crypto, "verify_password", fake_verify_Password)

    assert login_logic.validate_password("password", b"password") is True

def test_validate_password_password_dont_match(monkeypatch):
    def fake_verify_Password(input_password, database_password):
        return False
    
    monkeypatch.setattr(crypto, "verify_password", fake_verify_Password)

    assert login_logic.validate_password("password", b"password") is False