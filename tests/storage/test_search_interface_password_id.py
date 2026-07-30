from src.storage import Search_data
import sqlite3


def test_search_interface_password_id(tmp_path):
    db = tmp_path / "test.db"

    create_table = """
        CREATE TABLE vault_storage (
            cred_id,
            UserID,
            Service,
            Username,
            Password,
            Comment,
            CreationDate,
            EditedDate
        );
    """

    insert_data = """
        INSERT INTO vault_storage
        VALUES
            (1, 1, "test", "test", "test", "test", "test", "test"),
            (2, 2, "test", "test", "test", "test", "test", "test"),
            (3, 2, "test", "test", "test", "test", "test", "test"),
            (4, 3, "test", "test", "test", "test", "test", "test"),
            (5, 3, "test", "test", "test", "test", "test", "test"),
            (6, 3, "test", "test", "test", "test", "test", "test");
    """

    with sqlite3.connect(db) as connection:
        cursor = connection.cursor()
        cursor.execute(create_table)
        cursor.execute(insert_data)

    rows = Search_data.search_interface_password_id(
        userid=2,
        database=db
    )

    assert rows is not None
    assert len(rows) == 2

    assert rows[0][0] == 1
    assert rows[1][0] == 2

    assert rows[0][1] == 2
    assert rows[1][1] == 3