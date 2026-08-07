import src.vault_logic as vault_logic
import src.storage_logic as storage_logic
import src.interface.vault_interface as vault_interface

def test_start_flow_happy_test(monkeypatch):

    def fake_get_five_rows_out_database(userid):
        return ["test", "test", "test", "test", "test"]

    def fake_get_all_items_in_database(userid):
        return 5

    def fake_option_handler(choice, userid, encryption_key, total_cred):
        return "a"

    def fake_vault_screen(email: str, total_cred: int, rows: list, showed_items: int):
        return "a"

    monkeypatch.setattr(vault_logic, "clear_screen", lambda: None)
    monkeypatch.setattr(vault_logic, "get_five_rows_out_database", fake_get_five_rows_out_database)
    monkeypatch.setattr(storage_logic, "get_all_items_in_database", fake_get_all_items_in_database)
    monkeypatch.setattr(vault_logic, "option_handler", fake_option_handler)
    monkeypatch.setattr(vault_interface, "vault_screen", fake_vault_screen)

    assert vault_logic.start_flow("test@test.com", 1, b"encryption_key") == "a"

def test_start_flow_five_rows_return_none(monkeypatch):

    received = {}

    def fake_get_five_rows_out_database(userid):
        return None

    def fake_get_all_items_in_database(userid):
        return 0

    def fake_option_handler(choice, userid, encryption_key, total_cred):
        received["choice"] = choice
        return "a"

    def fake_vault_screen(email: str, total_cred: int, rows: list, showed_items: int):
        received["email"] = email
        received["total_cred"] = total_cred
        received["rows"] = rows
        received["showed_items"] = showed_items
        return "a"

    monkeypatch.setattr(vault_logic, "clear_screen", lambda: None)
    monkeypatch.setattr(vault_logic, "get_five_rows_out_database", fake_get_five_rows_out_database)
    monkeypatch.setattr(vault_logic.storage_logic, "get_all_items_in_database", fake_get_all_items_in_database)
    monkeypatch.setattr(vault_logic, "option_handler", fake_option_handler)
    monkeypatch.setattr(vault_logic.vault_interface, "vault_screen", fake_vault_screen)

    vault_logic.start_flow("test@test.com", 1, b"encryption_key")

    assert received["email"] == "test@test.com"
    assert received["total_cred"] == 0
    assert received["showed_items"] == 0
    assert received["rows"] is None
    assert received["choice"] == "a"



def test_start_flow_get_all_return_none(monkeypatch):

    received = {}

    def fake_get_five_rows_out_database(userid):
        return ["test", "test", "test", "test", "test"]
    def fake_get_all_items_in_database(userid):
        return None

    def fake_option_handler(choice, userid, encryption_key, total_cred):
        received["choice"] = choice
        return "a"

    def fake_vault_screen(email: str, total_cred: int, rows: list, showed_items: int):
        received["email"] = email
        received["total_cred"] = total_cred
        received["rows"] = rows
        received["showed_items"] = showed_items
        return "a"

    monkeypatch.setattr(vault_logic, "clear_screen", lambda: None)
    monkeypatch.setattr(vault_logic, "get_five_rows_out_database", fake_get_five_rows_out_database)
    monkeypatch.setattr(vault_logic.storage_logic, "get_all_items_in_database", fake_get_all_items_in_database)
    monkeypatch.setattr(vault_logic, "option_handler", fake_option_handler)
    monkeypatch.setattr(vault_logic.vault_interface, "vault_screen", fake_vault_screen)

    vault_logic.start_flow("test@test.com", 1, b"encryption_key")

    assert received["email"] == "test@test.com"
    assert received["total_cred"] == 0
    assert received["showed_items"] == 5
    assert received["rows"] == ["test", "test", "test", "test", "test"]
    assert received["choice"] == "a"


def test_start_flow_successs_none(monkeypatch):

    received = {"internal_error_called": False}

    def fake_get_five_rows_out_database(userid):
        return None
    
    def fake_get_all_items_in_database(userid):
        return 0

    def fake_option_handler(choice, userid, encryption_key, total_cred):
        return None

    def fake_vault_screen(email: str, total_cred: int, rows: list, showed_items: int):
        return "a"

    def fake_print_internal_error():
        received["internal_error_called"] = True

    monkeypatch.setattr(vault_logic, "clear_screen", lambda: None)
    monkeypatch.setattr(vault_logic, "get_five_rows_out_database", fake_get_five_rows_out_database)
    monkeypatch.setattr(vault_logic.storage_logic, "get_all_items_in_database", fake_get_all_items_in_database)
    monkeypatch.setattr(vault_logic, "option_handler", fake_option_handler)
    monkeypatch.setattr(vault_logic.vault_interface, "vault_screen", fake_vault_screen)
    monkeypatch.setattr(vault_logic.error_messages, "print_internal_error", fake_print_internal_error)

    result = vault_logic.start_flow("test@test.com", 1, b"encryption_key")

    assert received["internal_error_called"] is True
    assert result is None
