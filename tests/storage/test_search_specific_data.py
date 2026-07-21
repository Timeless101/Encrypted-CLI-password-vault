import pytest
import src.error as error
import sqlite3
from src.storage import Search_data


def test_search_function_wrong_table(tmp_path):
    db_path = tmp_path / "test.db"
    searcher = Search_data(str(db_path))

    with pytest.raises(error.TableError):
        searcher.search_specific_data(
            table="test.db",
            column="test",
            data_to_be_searched="test_data"
        )


def test_search_function_wrong_column(tmp_path):
    db_path = tmp_path / "test.db"
    searcher = Search_data(str(db_path))

    with sqlite3.connect(db_path) as connection:
        c = connection.cursor()

        sql = "CREATE TABLE IF NOT EXISTS test_table (name TEXT);"
        c.execute(sql)
        connection.commit()

    with pytest.raises(error.TableError):
        searcher.search_specific_data(
            table="test_table",
            column="wrong_column",
            data_to_be_searched="test_data"
        )


def test_search_function_wrong_data_to_be_searched(tmp_path):
    db_path = tmp_path / "test.db"
    searcher = Search_data(str(db_path))

    with sqlite3.connect(db_path) as connection:
        c = connection.cursor()

        sql = "CREATE TABLE IF NOT EXISTS test_table (Id TEXT);"
        sql1 = "INSERT INTO test_table (Id) VALUES ('hello');"
        c.execute(sql)
        c.execute(sql1)
        connection.commit()
        assert searcher.search_specific_data(
            table="test_table",
            column="Id",
            data_to_be_searched="Whut?"
        ) is None

    