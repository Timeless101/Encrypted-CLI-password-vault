import pytest
import src.error as error
import src.login_logic as login_logic
import src.storage_logic as storage_logic

#test if it raises the error when e-mail is put in worng.
def test_sign_in_function_email_wrong_email_format():
    with pytest.raises(error.EmailMismatchError):
        login_logic.sign_in_function("diego@.com", "password")

#test if it works correctly when e-mail is valid.
def test_sign_in_function_happy_test(monkeypatch):
    def fake_database(email: str, table_column: str, table_name: str):
        return (1, "diego@outlook.com", b"fake_hash")
    
    def fake_validate_password(input_password, database_password):
        return True
    
    monkeypatch.setattr(storage_logic, "data_row_search", fake_database)
    monkeypatch.setattr(login_logic, "validate_password", fake_validate_password)

    assert login_logic.sign_in_function(email="diego@outlook.com", password="fake_hash") is True

#Test wanneer het account niet bestaat in de database
def test_sign_in_function_account_none_account_found(monkeypatch):
    def fake_database(email: str, table_column: str, table_name: str):
        return None
    
    monkeypatch.setattr(storage_logic, "data_row_search", fake_database)

    with pytest.raises(error.AccountError):
        login_logic.sign_in_function("lol@outlook.com", b"fake_hash")


#Check what happens when worng password is enterd.
def test_sign_in_function_password_invalid(monkeypatch):
    def fake_database(email: str, table_column: str, table_name: str):
        return (1, "diego@outlook.com", b"fake_hash")
    
    def fake_validate_password(input_password, database_password):
        return False
    
    monkeypatch.setattr(storage_logic, "data_row_search", fake_database)
    monkeypatch.setattr(login_logic, "validate_password", fake_validate_password)

    with pytest.raises(error.InvalidPasswordError):
        login_logic.sign_in_function("diego@outlook.com", "password")