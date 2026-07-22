import src.vault_logic
import src.errors

def test_start_flow_happy_test(monkeypatch):

    def fake_get_five_rows_out_database(userid):
        return ["test", "test", "test", "test", "test"]

    def fake_get_all_items_in_database(userid):
        return 5

    
    