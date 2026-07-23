import src.vault_logic as vault_logic


def test_option_handler_test_add_items(monkeypatch):

    received= {"add_items_calls": 0}

    def fake_add_items():
        received["add_items_calls"] += 1
        return "add_result"

    monkeypatch.setattr(vault_logic, "add_items", fake_add_items)

    result = vault_logic.option_handler("a")

    assert received["add_items_calls"] == 1
    assert result == "add_result"

def test_option_handler_test_view_screen(monkeypatch):

    received= {"view_screen_calls": 0}

    def fake_view_screen():
        received["view_screen_calls"] += 1
        return "view_screen"

    monkeypatch.setattr(vault_logic, "view_screen", fake_view_screen)

    result = vault_logic.option_handler("v")

    assert received["view_screen_calls"] == 1
    assert result == "view_screen"


def test_option_handler_test_search_items(monkeypatch):

    received= {"search_item_calls": 0}

    def fake_search_item():
        received["search_item_calls"] += 1
        return "search_item"

    monkeypatch.setattr(vault_logic, "search_item", fake_search_item)

    result = vault_logic.option_handler("s")

    assert received["search_item_calls"] == 1
    assert result == "search_item"


def test_option_handler_test_delete_item(monkeypatch):

    received= {"delete_item_calls": 0}

    def fake_delete_item():
        received["delete_item_calls"] += 1
        return "delete_item"

    monkeypatch.setattr(vault_logic, "delete_item", fake_delete_item)

    result = vault_logic.option_handler("d")

    assert received["delete_item_calls"] == 1
    assert result == "delete_item"

def test_option_handler_test_edit_item(monkeypatch):

    received= {"edit_item_calls": 0}

    def fake_edit_item():
        received["edit_item_calls"] += 1
        return "edit_item"

    monkeypatch.setattr(vault_logic, "edit_item", fake_edit_item)

    result = vault_logic.option_handler("e")

    assert received["edit_item_calls"] == 1
    assert result == "edit_item"

def test_option_handler_test_quit_program(monkeypatch):

    received= {"quit_program_calls": 0}

    def fake_quit_program():
        received["quit_program_calls"] += 1
        return "quit_program"

    monkeypatch.setattr(vault_logic, "quit_program", fake_quit_program)

    result = vault_logic.option_handler("q")

    assert received["quit_program_calls"] == 1
    assert result == "quit_program"

def test_option_handler_test_none():

    assert vault_logic.option_handler(None) is None

def test_option_handler_test_choice_not_in_list(monkeypatch):

    assert vault_logic.option_handler("w") is None