import src.vault_logic as vault_logic
import pytest

def test_get_five_rows_out_database_happy_test(monkeypatch):
    def fake_search(table, column, userid, amount_of_items):
        return ["test", "test", "test", "test", "test"]
    
    monkeypatch.setattr(vault_logic.storage_logic, "search_limited_amount_of_items_in_database", fake_search)

    result = vault_logic.get_five_rows_out_database(1)
    assert len(result) == 5

def test_get_five_rows_out_database_to_much_results(monkeypatch):
    def fake_search(table, column, userid, amount_of_items):
        return ["test", "test", "test", "test", "test", "test"]
    
    monkeypatch.setattr(vault_logic.storage_logic, "search_limited_amount_of_items_in_database", fake_search)

    with pytest.raises(ValueError):
        vault_logic.get_five_rows_out_database(1)


def test_get_five_rows_out_database_none_result(monkeypatch):
    def fake_search(table, column, userid, amount_of_items):
        return None
    
    monkeypatch.setattr(vault_logic.storage_logic, "search_limited_amount_of_items_in_database", fake_search)

    assert vault_logic.get_five_rows_out_database(1) is None


def test_get_five_rows_out_database_return_type_list(monkeypatch):
    def fake_search(table, column, userid, amount_of_items):
        return ["test", "test", "test", "test", "test"]
    
    monkeypatch.setattr(vault_logic.storage_logic, "search_limited_amount_of_items_in_database", fake_search)

    result = vault_logic.get_five_rows_out_database(1)
    assert type(result) is list