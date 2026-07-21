import src.storage_logic as storage_logic
import src.login_logic as login_logic
import src.error as error
import pytest

def test_get_userid_happy_test(monkeypatch):
    def fake_data_row_search(email: str, table_column: str, table_name: str):
        return ["1", "test@test", b"test"]
    
    monkeypatch.setattr(storage_logic, "data_row_search", fake_data_row_search)

    assert login_logic.get_userid("test") == 1

def test_get_userid_happy_test(monkeypatch):
    def fake_data_row_search(email: str, table_column: str, table_name: str):
        return None
    
    monkeypatch.setattr(storage_logic, "data_row_search", fake_data_row_search)

    with pytest.raises(error.AccountError):
        assert login_logic.get_userid("test@test.nl")