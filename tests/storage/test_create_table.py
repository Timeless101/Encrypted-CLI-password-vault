import pytest
import src.errors as errors
from src.storage import Table_creator


def test_create_tabale__wrong_input(tmp_path):
    db_path = tmp_path / "test.db"

    with pytest.raises(errors.WrongDataTypeDict):
        Table_creator(str(db_path)).create_table(
            table_name="bad",
            columns="hello"
        )

def test_create_tabale_raise_error(tmp_path):
    db_path = tmp_path / "test.db"

    with pytest.raises(errors.TableError):
        Table_creator(str(db_path)).create_table(
            table_name="bad",
            columns={"hello": "how are you?",
                     "what": "????",}
        )