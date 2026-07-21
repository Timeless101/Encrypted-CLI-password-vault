import src.login_logic as login_logic
import src.storage_logic as storage_logic
import src.cli as cli
import src.error as error
import pytest

def test_login_flow_happy_test(monkeypatch):

    def fake_login_screen():
        return "test@test.com", "password"

    def fake_sign_in_function(email, password):
        return True

    def fake_get_userid(input_email):
        return "1"

    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(cli, "login_screen", fake_login_screen)
    monkeypatch.setattr(login_logic, "sign_in_function", fake_sign_in_function)
    monkeypatch.setattr(login_logic, "get_userid", fake_get_userid)

    assert login_logic.login_flow() == ("test@test.com", "1")

def test_login_flow_email_error(monkeypatch):

    count = 0

    def fake_login_screen():
        return "test@test.com", "password"

    def fake_sign_in_function(email, password):
        nonlocal count

        if count == 0:
            count += 1
            raise error.EmailMismatchError()
        return True

    def fake_get_userid(input_email):
        return "1"

    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(cli, "login_screen", fake_login_screen)
    monkeypatch.setattr(login_logic, "sleep", lambda _: None)
    monkeypatch.setattr(login_logic, "sign_in_function", fake_sign_in_function)
    monkeypatch.setattr(login_logic, "get_userid", fake_get_userid)

    assert login_logic.login_flow() == ("test@test.com", "1")
    assert count == 1

def test_login_flow_account_error(monkeypatch):

    count = 0

    def fake_login_screen():
        return "test@test.com", "password"

    def fake_sign_in_function(email, password):
        nonlocal count

        if count == 0:
            count += 1
            raise error.AccountError()
        return True

    def fake_get_userid(input_email):
        return "1"

    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(cli, "login_screen", fake_login_screen)
    monkeypatch.setattr(login_logic, "sleep", lambda _: None)
    monkeypatch.setattr(login_logic, "sign_in_function", fake_sign_in_function)
    monkeypatch.setattr(login_logic, "get_userid", fake_get_userid)

    assert login_logic.login_flow() == ("test@test.com", "1")
    assert count == 1

def test_login_flow_invalid_password_error(monkeypatch):

    count = 0

    def fake_login_screen():
        return "test@test.com", "password"

    def fake_sign_in_function(email, password):
        nonlocal count

        if count == 0:
            count += 1
            raise error.InvalidPasswordError()
        return True

    def fake_get_userid(input_email):
        return "1"

    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(cli, "login_screen", fake_login_screen)
    monkeypatch.setattr(login_logic, "sleep", lambda _: None)
    monkeypatch.setattr(login_logic, "sign_in_function", fake_sign_in_function)
    monkeypatch.setattr(login_logic, "get_userid", fake_get_userid)

    assert login_logic.login_flow() == ("test@test.com", "1")
    assert count == 1