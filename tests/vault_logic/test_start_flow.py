import src.vault_logic as vault_logic
import src.storage_logic as storage_logic
import src.cli as cli

def test_start_flow_happy_test(monkeypatch):

    def fake_get_five_rows_out_database(userid):
        return ["test", "test", "test", "test", "test"]

    def fake_get_all_items_in_database(userid):
        return 5

    def fake_option_handler(choice):
        return "a"

    def fake_vault_screen(email: str, total_cred: int, rows: list, showed_items: int):
        return "a"

    monkeypatch.setattr(cli, "clear_screen", lambda: None)
    monkeypatch.setattr(vault_logic, "get_five_rows_out_database", fake_get_five_rows_out_database)
    monkeypatch.setattr(storage_logic, "get_all_items_in_database", fake_get_all_items_in_database)
    monkeypatch.setattr(vault_logic, "option_handler", fake_option_handler)
    monkeypatch.setattr(cli, "vault_screen", fake_vault_screen)

    assert vault_logic.start_flow("test@test.com", 1) == "a"

def test_start_flow_five_rows_return_none(monkeypatch):

    recieved = {}

    def fake_get_five_rows_out_database(userid):
        return None

    def fake_get_all_items_in_database(userid):
        return 0

    def fake_option_handler(choice):
        recieved["choice"] = choice
        return "a"

    def fake_vault_screen(email: str, total_cred: int, rows: list, showed_items: int):
        recieved["email"] = email
        recieved["total_cred"] = total_cred
        recieved["rows"] = rows
        recieved["showed_items"] = showed_items
        return "a"

    monkeypatch.setattr(vault_logic.cli, "clear_screen", lambda: None)
    monkeypatch.setattr(vault_logic, "get_five_rows_out_database", fake_get_five_rows_out_database)
    monkeypatch.setattr(vault_logic.storage_logic, "get_all_items_in_database", fake_get_all_items_in_database)
    monkeypatch.setattr(vault_logic, "option_handler", fake_option_handler)
    monkeypatch.setattr(vault_logic.cli, "vault_screen", fake_vault_screen)

    vault_logic.start_flow("test@test.com", 1)

    assert recieved["email"] == "test@test.com"
    assert recieved["total_cred"] == 0
    assert recieved["showed_items"] == 0
    assert recieved["rows"] is None
    assert recieved["choice"] == "a"



def test_start_flow_get_all_return_none(monkeypatch):

    recieved = {}

    def fake_get_five_rows_out_database(userid):
        return ["test", "test", "test", "test", "test"]
    def fake_get_all_items_in_database(userid):
        return None

    def fake_option_handler(choice):
        recieved["choice"] = choice
        return "a"

    def fake_vault_screen(email: str, total_cred: int, rows: list, showed_items: int):
        recieved["email"] = email
        recieved["total_cred"] = total_cred
        recieved["rows"] = rows
        recieved["showed_items"] = showed_items
        return "a"

    monkeypatch.setattr(vault_logic.cli, "clear_screen", lambda: None)
    monkeypatch.setattr(vault_logic, "get_five_rows_out_database", fake_get_five_rows_out_database)
    monkeypatch.setattr(vault_logic.storage_logic, "get_all_items_in_database", fake_get_all_items_in_database)
    monkeypatch.setattr(vault_logic, "option_handler", fake_option_handler)
    monkeypatch.setattr(vault_logic.cli, "vault_screen", fake_vault_screen)

    vault_logic.start_flow("test@test.com", 1)

    assert recieved["email"] == "test@test.com"
    assert recieved["total_cred"] == 0
    assert recieved["showed_items"] == 5
    assert recieved["rows"] == ["test", "test", "test", "test", "test"]
    assert recieved["choice"] == "a"


def test_start_flow_success_none(monkeypatch):

    recieved = {"internal_error_called": False}

    def fake_get_five_rows_out_database(userid):
        return None
    
    def fake_get_all_items_in_database(userid):
        return 0

    def fake_option_handler(choice):
        return None

    def fake_vault_screen(email: str, total_cred: int, rows: list, showed_items: int):
        return "a"

    def fake_print_internal_error():
        recieved["internal_error_called"] = True

    monkeypatch.setattr(vault_logic.cli, "clear_screen", lambda: None)
    monkeypatch.setattr(vault_logic, "get_five_rows_out_database", fake_get_five_rows_out_database)
    monkeypatch.setattr(vault_logic.storage_logic, "get_all_items_in_database", fake_get_all_items_in_database)
    monkeypatch.setattr(vault_logic, "option_handler", fake_option_handler)
    monkeypatch.setattr(vault_logic.cli, "vault_screen", fake_vault_screen)
    monkeypatch.setattr(vault_logic.cli, "print_internal_error", fake_print_internal_error)

    result = vault_logic.start_flow("test@test.com", 1)

    assert recieved["internal_error_called"] is True
    assert result is None
