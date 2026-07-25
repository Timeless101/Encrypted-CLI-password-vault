import src.login_logic as login_logic
import src.validator as validator
import src.cli as cli
import src.crypto as crypto
import pytest
import src.errors as errors

def test_email_checker(monkeypatch):
    def fake_cli_menu():
        return ("diego@outlook.com", "password", "password")
    
    def fake_email_checker(email):
        return False
    
    monkeypatch.setattr(cli, "register_screen", fake_cli_menu)
    monkeypatch.setattr(validator, "email_checker", fake_email_checker)

    with pytest.raises(errors.EmailMismatchError):
        login_logic.get_input_and_validate_it()

def test_password_match(monkeypatch):
    def fake_cli_menu():
        return ("diego@outlook.com", "password", "password")

    def fake_email_checker(email):
        return True

    def fake_password_match_checker(password1, password2):
        return False
    
    monkeypatch.setattr(cli, "register_screen", fake_cli_menu)
    monkeypatch.setattr(validator, "email_checker", fake_email_checker)
    monkeypatch.setattr(validator, "password_match_checker", fake_password_match_checker)

    with pytest.raises(errors.PasswordMismatchError):
        login_logic.get_input_and_validate_it()


def test_email_is_available(monkeypatch):
    def fake_cli_menu():
        return ("diego@outlook.com", "password", "password")

    def fake_email_checker(email):
        return True
    
    def fake_email_search(email):
        return None

    def fake_password_match_checker(password1, password2):
        return True

    def fake_email_is_available(new_email, database_email):
        return False

    monkeypatch.setattr(cli, "register_screen", fake_cli_menu)
    monkeypatch.setattr(validator, "email_is_available", fake_email_is_available)
    monkeypatch.setattr(validator, "email_checker", fake_email_checker)
    monkeypatch.setattr(validator, "password_match_checker", fake_password_match_checker)
    monkeypatch.setattr(login_logic, "email_search", fake_email_search)

    with pytest.raises(errors.DuplicationError):
        login_logic.get_input_and_validate_it()

def test_happy_get_valid_input(monkeypatch):
    def fake_cli_menu():
        return ("fake@fake.com", "password", "password")

    def fake_email_checker(email):
        return True

    def fake_password_match_checker(password1, password2):
        return True
    
    def fake_email_search(email):
        return None

    def fake_email_is_available(new_email, database_email):
        return True
    
    def fake_hash_password(password, salt):
        return "password" b"salt"

    monkeypatch.setattr(cli, "register_screen", fake_cli_menu)
    monkeypatch.setattr(validator, "email_is_available", fake_email_is_available)
    monkeypatch.setattr(validator, "email_checker", fake_email_checker)
    monkeypatch.setattr(validator, "password_match_checker", fake_password_match_checker)
    monkeypatch.setattr(crypto, "hash_password", fake_hash_password)
    monkeypatch.setattr(login_logic, "email_search", fake_email_search)

    assert login_logic.get_input_and_validate_it() == ("fake@fake.com" , b"password", b"salt")