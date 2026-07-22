import src.login_logic as login_logic
import src.storage_logic as storage_logic
import src.errors as errors
import pytest


#Happy test:
def test_initialize_database_bystartup_happy_test(monkeypatch):
    def fake_create_database(database_name):
        return True
    
    def fake_create_table(table_name: str, columns: dict):
        return True
    
    def fake_vault_storage(table_name: str, columns: dict):
        return True
    
    monkeypatch.setattr(storage_logic, "create_database", fake_create_database)
    monkeypatch.setattr(storage_logic, "table_creator", fake_create_table)
    monkeypatch.setattr(storage_logic, "table_creator", fake_vault_storage)

    assert login_logic.initialize_database_bystartup() is True

#Test error in database:
def test_initialize_database_bystartup_database_error(monkeypatch):
    def fake_create_database(database_name):
        raise errors.DatabaseError()
    
    def fake_create_table(table_name: str, columns: dict):
        return True
    
    def fake_vault_storage(table_name: str, columns: dict):
        return True
    
    monkeypatch.setattr(storage_logic, "create_database", fake_create_database)
    monkeypatch.setattr(storage_logic, "table_creator", fake_create_table)
    monkeypatch.setattr(storage_logic, "table_creator", fake_vault_storage)

    with pytest.raises(errors.DatabaseError):
        assert login_logic.initialize_database_bystartup() is False


#Test create_table error:
def test_initialize_database_bystartup_create_table_wrong_type(monkeypatch):

    def fake_create_table(table_name: str, columns: dict):
        raise errors.WrongDataTypeDict()

    monkeypatch.setattr(storage_logic, "table_creator", fake_create_table)

    assert login_logic.initialize_database_bystartup() is False

#Test create_table error:
def test_initialize_database_bystartup_create_table_error(monkeypatch):

    def fake_create_table(table_name: str, columns: dict):
        raise errors.TableCreationError()
    monkeypatch.setattr(storage_logic, "table_creator", fake_create_table)

    assert login_logic.initialize_database_bystartup() is False


def test_initialize_database_bystartup_vault_storage_table_error(monkeypatch):
    def fake_create_database(database_name):
        return True
    
    def fake_create_table(table_name: str, columns: dict):
        return True
    
    def fake_vault_storage(table_name: str, columns: dict):
        raise errors.TableCreationError()
    
    monkeypatch.setattr(storage_logic, "create_database", fake_create_database)
    monkeypatch.setattr(storage_logic, "table_creator", fake_create_table)
    monkeypatch.setattr(storage_logic, "table_creator", fake_vault_storage)

    assert login_logic.initialize_database_bystartup() is False


def test_initialize_database_bystartup_vault_storage_wrong_type(monkeypatch):
    def fake_create_database(database_name):
        return True
    
    def fake_create_table(table_name: str, columns: dict):
        return True
    
    def fake_vault_storage(table_name: str, columns: dict):
        raise errors.WrongDataTypeDict()
    
    monkeypatch.setattr(storage_logic, "create_database", fake_create_database)
    monkeypatch.setattr(storage_logic, "table_creator", fake_create_table)
    monkeypatch.setattr(storage_logic, "table_creator", fake_vault_storage)

    assert login_logic.initialize_database_bystartup() is False