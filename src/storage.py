import sqlite3
import src.errors as errors

#Create database
def create_database(database_name):
    try:
        with sqlite3.connect(database_name):
            return True
    except sqlite3.Error as sql_error:
        raise errors.DatabaseError(f"Could not open database") from sql_error

#create an table with given input.
class Table_creator():
    def __init__(self, database_name: str):
        self.database_name = database_name

    def create_table(self, table_name: str, columns: dict) -> True:
        if not isinstance(columns, dict):
            raise errors.WrongDataTypeDict("Columns must be a Dictionary.")

        try:
            columns_sql = []
            for column_name, column_definition in columns.items():
                columns_sql.append(f"{column_name} {column_definition}")

            columns_sql_string = ", ".join(columns_sql)

            run = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {columns_sql_string}
            );
            """
            
            with sqlite3.connect(self.database_name) as connection:
                c = connection.cursor()
                c.execute(run)
                connection.commit()
            
            return True

        except sqlite3.DatabaseError as sql_error:
            raise errors.TableCreationError(f"Couldn't create table") from sql_error


#Insert  data in requested database.
class Insert_data():
    def __init__(self, database_name: str):
        self.database_name = database_name
    
    def insert_data(self, table_name: str, column_name: list, data_insert: list) -> True:
        if not isinstance(data_insert, list):
            raise errors.WrongDataTypeList("Data insert isn't a list.")
        
        if not isinstance(column_name, list):
            raise errors.WrongDataTypeList("column isn't a list.")
        
        if len(column_name) != len(data_insert):
            raise errors.DataLengthError("Column name and data insert list length isn't the same.")

        try:
            columns = ", ".join(column_name)
            placeholders = ", ".join(["?"] * len(data_insert))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

            with sqlite3.connect(self.database_name) as connection:
                c = connection.cursor()
                c.execute(sql, data_insert)
                connection.commit()
            return True

        except sqlite3.OperationalError as sql_error:
            raise errors.InsertError(f"No such table: {table_name}") from sql_error

        except sqlite3.DatabaseError as sql_error:
            raise errors.InsertError(f"Couldn't insert data") from sql_error
      
#Search data in datebase.
class Search_data():
    def __init__(self, database_name: str):
        self.database_name = database_name
    
    def search_specific_data(self, table: str, column: str, data_to_be_searched: str,) -> list | None:
        try:
            query = f"SELECT * FROM {table} WHERE {column} = ?"
            value = data_to_be_searched
            with sqlite3.connect(self.database_name) as connection:
                c = connection.cursor()
                c.execute(query, (value,))
                rows = c.fetchall()

            if len(rows) <= 0:
                return None
            
            return rows
        
        except sqlite3.OperationalError as table_error:
            raise errors.TableError(f"No such table: {table}") from table_error

    def search_interface_password_id(userid: int, database: str, limit: int) -> list[tuple] | None:

        try:
            query = """
            SELECT
                ROW_NUMBER() OVER(
                PARTITION BY UserID
                ORDER by cred_id
            ) AS screen_number_ID ,
            cred_id,
            Service,
            Username,
            Password,
            Comment,
            CreationDate,
            EditedDate

            FROM vault_storage
            WHERE UserID = ? LIMIT ?;"""

            with sqlite3.connect(database) as connection:
                c = connection.cursor()
                c.execute(query, (userid, limit))
                rows = c.fetchall()

            if len(rows) == 0:
                return None
            
            return rows # returns: [(screen_number_ID, cred_id, Service, Username, Password, Comment, DreationDate, EditedDate)]

            
        except sqlite3.ProgrammingError as Programmers_fault:
            raise errors.WrongSQLStatement("The SQL statements are wrong, please check the query you wrote.") from Programmers_fault

        except sqlite3.OperationalError as Operation_error:
            raise errors.DatabaseError(f"Database Operation failed: {Operation_error}")

        except sqlite3.Error as Error:
            raise errors.UnexpectedError(f"There was a unexpected error: {Error}")

    def search_for_view_items(userid: int, limit: int, offset: int, database) -> list[tuple] | None:
        try:
            query = """
                SELECT cred_id,
                    Service, 
                    Username,
                    Comment,
                    CreationDate,
                    EditedDate
                FROM vault_storage
                WHERE UserID = ? 
                ORDER BY service ASC, Username ASC, cred_id ASC 
                LIMIT ? 
                OFFSET ?
                """

            with sqlite3.Connection(database) as connection:
                c = connection.cursor()
                c.execute(query, (userid, limit, offset))

                rows = c.fetchall()

                if len(rows) == 0:
                    return None

                return rows
        
        except sqlite3.ProgrammingError as Programmers_fault:
            raise errors.WrongSQLStatement("The SQL statements are wrong, please check the query you wrote.") from Programmers_fault
        
        except sqlite3.OperationalError as Operation_error:
            raise errors.DatabaseError(f"Database Operation failed: {Operation_error}")

        except sqlite3.Error as Error:
            raise errors.UnexpectedError(f"There was a unexpected error: {Error}")


if __name__ == "__main__":
    ...