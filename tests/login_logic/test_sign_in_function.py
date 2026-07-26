import pytest
import src.errors as errors
import src.login_logic as login_logic
import src.storage_logic as storage_logic


#test if it works correctly when e-mail is valid.
def test_sign_in_function_happy_test(monkeypatch):

    def fake_email_checker(email):
        return True

    def fake_data_row_search(email: str, table_column: str, table_name: str):
        return (1, "diego@outlook.com", b"password_hash", b"password_salt", b"encryption_salt")
    
    def fake_validate_password(input_password, database_password, salt):
        return True

    monkeypatch.setattr(login_logic.validator, "email_checker", fake_email_checker)
    monkeypatch.setattr(login_logic.storage_logic, "data_row_search", fake_data_row_search)
    monkeypatch.setattr(login_logic, "validate_password", fake_validate_password)

    result = login_logic.sign_in_function(email="diego@outlook.com", password="fake_hash")
    assert isinstance(result, bytes) is True

#test if it raises the error when e-mail is put in worng.
def test_sign_in_function_email_wrong_email_format():
    with pytest.raises(errors.EmailMismatchError):
        assert login_logic.sign_in_function("diego@.com", "password")


#Test wanneer het account niet bestaat in de database
def test_sign_in_function_account_none_account_found(monkeypatch):


    def fake_data_row_search(email: str, table_column: str, table_name: str):
        return None
    
    monkeypatch.setattr(storage_logic, "data_row_search", fake_data_row_search)

    with pytest.raises(errors.AccountError):
        login_logic.sign_in_function("lol@outlook.com", b"fake_hash")


#Check what happens when wrong password is enterd.
def test_sign_in_function_password_invalid(monkeypatch):
    def fake_data_row_search(email: str, table_column: str, table_name: str):
        return (1, "diego@outlook.com", b"password_hash", b"password_salt", b"encryption_salt")
    
    def fake_validate_password(input_password, database_password, salt):
        return False
    
    monkeypatch.setattr(storage_logic, "data_row_search", fake_data_row_search)
    monkeypatch.setattr(login_logic, "validate_password", fake_validate_password)

    with pytest.raises(errors.InvalidPasswordError):
        login_logic.sign_in_function("diego@outlook.com", "password")