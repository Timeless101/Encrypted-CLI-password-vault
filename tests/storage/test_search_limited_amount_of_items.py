import src.storage as storage
import src.errors as errors
import sqlite3
import pytest


def test_search_limited_amount_of_items_happy_test(tmp_path):
    db_path = tmp_path / "test.db"
    searcher = storage.Search_data(str(db_path))

    with sqlite3.connect(db_path) as connection:
        c = connection.cursor()

        sql = "CREATE TABLE IF NOT EXISTS test_table (UserID INTEGER NOT NULL, Username TEXT, Password TEXT, Comment TEXT);"
        c.execute(sql)
        connection.commit()
        for _ in range(10):
            sql1 = "INSERT INTO test_table (UserID, Username, Password, Comment) VALUES "
            c.execute(sql1 + "(1, 'test', 'test', 'test')")
        connection.commit()

        query = f"SELECT * from test_table WHERE UserID = ? LIMIT 5"
        usrid = 1

        c.execute(query, (usrid,))

        result = searcher.search_limited_amount_of_items(
            table="test_table",
            column="UserID",
            userid=1,
            amount_of_items=5
        )

        assert len(result) == 5

def test_search_limited_amount_of_items_no_results(tmp_path):
    db_path = tmp_path / "test.db"
    searcher = storage.Search_data(str(db_path))

    with sqlite3.connect(db_path) as connection:
        c = connection.cursor()

        sql = "CREATE TABLE IF NOT EXISTS test_table (UserID INTEGER NOT NULL, Username TEXT, Password TEXT, Comment TEXT);"
        c.execute(sql)
        connection.commit()
        for _ in range(10):
            sql1 = "INSERT INTO test_table (UserID, Username, Password, Comment) VALUES "
            c.execute(sql1 + "(1, 'test', 'test', 'test')")
        connection.commit()

        query = f"SELECT * from test_table WHERE UserID = ? LIMIT 5"
        usrid = 1

        c.execute(query, (usrid,))

        assert searcher.search_limited_amount_of_items(
            table="test_table",
            column="UserID",
            userid=2,
            amount_of_items=5
        ) is None

def test_search_limited_amount_of_items_error_test(tmp_path):
    db_path = tmp_path / "test.db"
    searcher = storage.Search_data(str(db_path))
    
    with pytest.raises(errors.TableError):
        assert searcher.search_limited_amount_of_items("name", "table", 1, 1)