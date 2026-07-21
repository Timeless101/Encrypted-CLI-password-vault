import src.login_logic as login_logic
import src.storage_logic as storage_logic
import src.cli as cli
import pytest
import src.error as error


def test_sign_up_flow_happy_test(monkeypatch):

    def fake_get_input_and_validate_it():
        return "email@email.com", b"password"
    
    def fake_insert_sign_up_data(table_name: str, column_name: list, data: list):
        return True
    
    def fake_get_userid(email):
        return "1"
    
    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(storage_logic, "insert_data", fake_insert_sign_up_data)
    monkeypatch.setattr(login_logic, "get_input_and_validate_it", fake_get_input_and_validate_it)
    monkeypatch.setattr(login_logic, "get_userid", fake_get_userid)

    assert login_logic.sign_up_flow() == ("email@email.com", "1")

def test_sign_up_flow_database_insert_False(monkeypatch):

    count = 0

    def fake_get_input_and_validate_it():
        return "email@email.com", b"password"
    
    def fake_insert_sign_up_data(table_name: str, column_name: list, data: list):
        nonlocal count

        if count == 0:
            count += 1
            return False
        
        return True
    
    def fake_get_userid(email):
        return "1"
    
    monkeypatch.setattr(storage_logic, "insert_data", fake_insert_sign_up_data)
    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(cli, "print_error_database", lambda: None)
    monkeypatch.setattr(login_logic, "get_input_and_validate_it", fake_get_input_and_validate_it)
    monkeypatch.setattr(login_logic, "get_userid", fake_get_userid)

    assert login_logic.sign_up_flow() == ("email@email.com", "1")


def test_sign_up_flow_email_mismatch_error(monkeypatch):

    count = 0

    def fake_get_input_and_validate_it():

        nonlocal count

        if count == 0:
            count += 1
            raise error.EmailMismatchError()

        return "email@email.com", b"password"
    
    def fake_insert_sign_up_data(table_name: str, column_name: list, data: list):
        return True
    
    def fake_get_userid(email):
        return "1"
    
    monkeypatch.setattr(storage_logic, "insert_data", fake_insert_sign_up_data)
    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(login_logic, "sleep", lambda _: None)
    monkeypatch.setattr(login_logic, "get_input_and_validate_it", fake_get_input_and_validate_it)
    monkeypatch.setattr(login_logic, "get_userid", fake_get_userid)

    assert login_logic.sign_up_flow() == ("email@email.com", "1")

def test_sign_up_flow_password_mismatch_error(monkeypatch):

    count = 0

    def fake_get_input_and_validate_it():

        nonlocal count

        if count == 0:
            count += 1
            raise error.PasswordMismatchError()

        return "email@email.com", b"password"
    
    def fake_insert_sign_up_data(table_name: str, column_name: list, data: list):
        return True
    
    def fake_get_userid(email):
        return "1"
    
    monkeypatch.setattr(storage_logic, "insert_data", fake_insert_sign_up_data)
    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(login_logic, "sleep", lambda _: None)
    monkeypatch.setattr(login_logic, "get_input_and_validate_it", fake_get_input_and_validate_it)
    monkeypatch.setattr(login_logic, "get_userid", fake_get_userid)

    assert login_logic.sign_up_flow() == ("email@email.com", "1")


def test_sign_up_flow_duplication_error(monkeypatch):

    count = 0

    def fake_get_input_and_validate_it():

        nonlocal count

        if count == 0:
            count += 1
            raise error.DuplicationError()

        return "email@email.com", b"password"
    
    def fake_insert_sign_up_data(table_name: str, column_name: list, data: list):
        return True
    
    def fake_create_vault_storage(table_name: str, columns: dict):
        return True
    
    def fake_get_userid(email):
        return "1"
    
    monkeypatch.setattr(storage_logic, "insert_data", fake_insert_sign_up_data)
    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(login_logic, "sleep", lambda _: None)
    monkeypatch.setattr(login_logic, "get_input_and_validate_it", fake_get_input_and_validate_it)
    monkeypatch.setattr(storage_logic, "table_creator", fake_create_vault_storage)
    monkeypatch.setattr(login_logic, "get_userid", fake_get_userid)

    assert login_logic.sign_up_flow() == ("email@email.com", "1")