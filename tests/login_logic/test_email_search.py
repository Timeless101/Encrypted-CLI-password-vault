import src.login_logic as login_logic
import src.storage_logic as storage_logic
import src.error as error


def test_email_search(monkeypatch):
    def fake_search_data(table_name: str, table_column: str, data_to_be_searched: str):
        return None
    
    monkeypatch.setattr(storage_logic, "search_data", fake_search_data)

    assert login_logic.email_search("fake@fake.com") is None


def test_email_search_wrong_table(monkeypatch):
    def fake_search_data(table_name: str, table_column: str, data_to_be_searched: str):
        raise error.TableError()
    
    monkeypatch.setattr(storage_logic, "search_data", fake_search_data)

    assert login_logic.email_search("fake@fake.com") is False


def test_email_search_happy_test(monkeypatch):
    def fake_search_data(table_name: str, table_column: str, data_to_be_searched: str):
        return [(1,"fake@fake.com", b"fake_hash")]
    
    monkeypatch.setattr(storage_logic, "search_data", fake_search_data)

    assert login_logic.email_search("fake@fake.com") == "fake@fake.com"