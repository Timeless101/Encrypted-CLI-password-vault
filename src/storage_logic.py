import src.storage as storage
import src.errors as errors

DATABASE_NAME = "CLI_Data.db"
LOGIN_TABLE = "login_information"
VAULT_TABLE = "vault_storage"
    
#Search functions
def search_limited_amount_of_items_in_database(userid: int, limit: int) -> list[tuple] | None:

    data: list[tuple] = storage.Search_data.search_interface_password_id(
        userid=userid,
        database=DATABASE_NAME,
        limit=limit
    )

    return data # returns: screen_number_ID, cred_id, Service, Username, Password, Comment, DreationDate, EditedDate
    
def get_all_items_in_database(userid) -> None | int:
    try:
        data: list | None = search_data(
            table_name=VAULT_TABLE,
            table_column="UserID",
            data_to_be_searched=userid
        )

        if data is None:
            return None
        else:
            return len(data)
        
    except errors.TableError as table_error:
        raise errors.TableError(f"No such table: vault_storage") from table_error

def search_data(table_name: str, table_column: str, data_to_be_searched: str) -> list | None:
    try:
        db = storage.Search_data(DATABASE_NAME)
        data:  list | None = db.search_specific_data(
        table=table_name,
        column=table_column,
        data_to_be_searched=data_to_be_searched
        )

        if data is None:
            return None

        return data
    except errors.TableError as table_error:
        raise errors.TableError(f"No such table: {table_name}") from table_error
    

def data_row_search(email: str, table_column: str, table_name: str) -> list | None:
    try:
        data: list | None = search_data(
            table_name=table_name,
            table_column=table_column,
            data_to_be_searched=email
        )
        if data is None:
            return None
        else:
            return data[0]
        
    except errors.TableError as table_error:
        raise errors.TableError(f"No such table: {LOGIN_TABLE}") from table_error


#Insert functions
def insert_data(table_name: str, column_name: list, data: list) -> bool:
    try:
        db = storage.Insert_data(database_name=DATABASE_NAME)
        if db.insert_data(table_name=table_name, column_name=column_name, data_insert=data):
            return True
        
    except errors.WrongDataTypeList as wrong_type_error:
        raise errors.WrongDataTypeList("Datatype isn't an list") from wrong_type_error

    except errors.DataLengthError as wrong_data_length_error:
        raise errors.DataLengthError("column_name and data do not contain the same number of items.") from wrong_data_length_error

    except errors.InsertError as insert_error:
        raise errors.InsertError("Could not insert data into database.") from insert_error
    

#Database creations functions
def table_creator(table_name: str, columns: dict):
    creator = storage.Table_creator(database_name=DATABASE_NAME)
    try:
        if creator.create_table(
            table_name=table_name,
            columns=columns):
            return True

    except errors.WrongDataTypeDict as wrong_type_error:
        raise errors.WrongDataTypeDict("Datatype isn't an dictionary") from wrong_type_error
    
    except errors.TableError as table_error:
        raise errors.TableError(f"No such table: {table_name}") from table_error


def create_database(database_name: str):
    try:
        if storage.create_database(database_name=database_name):
            return True
        return False
    except errors.DatabaseError:
        return False