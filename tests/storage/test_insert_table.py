import pytest
import src.error as error
from src.storage import Insert_data, Search_data, Table_creator


def test_insert_missing_table_raises_insert_error(tmp_path):
    db_path = tmp_path / "test.db"
    inserter = Insert_data(str(db_path))

    with pytest.raises(error.InsertError):
        inserter.insert_data(
            "missing_table",
            ["Email", "Password"],
            ["test@example.com", "hash"]
        )