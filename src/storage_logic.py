import src.storage as storage
import src.errors as errors

DATABASE_NAME = "CLI_Data.db"
LOGIN_TABLE = "login_information"
VAULT_TABLE = "vault_storage"

#Search all items under userID in Database.
#Return the total items in int.
def get_all_items_in_database(userid):
    try:
        data = search_data(
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
    
#Search the specified amount of rows from the database that is associated with the UserID.
def search_limited_amount_of_items_in_database(table: str, column: str, userid: int, amount_of_items: int):
    try:
        db = storage.Search_data(database_name=DATABASE_NAME)
        data = db.search_limited_amount_of_items(
            table=table,
            column=column,
            userid=userid,
            amount_of_items=amount_of_items
        )

        if data is None:
            return None
        
        return data
    except errors.TableError as table_error:
        raise errors.TableError(f"No such table: {table}") from table_error
    
#Storge database search function.
#searches specific data in the specified column of the specified table.
def search_data(table_name: str, table_column: str, data_to_be_searched: str):
    try:
        db = storage.Search_data(DATABASE_NAME)
        data = db.search_specific_data(
        table=table_name,
        column=table_column,
        data_to_be_searched=data_to_be_searched
        )

        if data is None:
            return None

        return data
    except errors.TableError as table_error:
        raise errors.TableError(f"No such table: {table_name}") from table_error
    

def data_row_search(email: str, table_column: str, table_name: str):
    try:
        data = search_data(
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


def insert_data(table_name: str, column_name: list, data: list):

    print(len(column_name), "\n", len(data))
    print("\n", column_name, "\n", data)

    try:
        db = storage.Insert_data(database_name=DATABASE_NAME)
        if db.insert_data(table_name=table_name, column_name=column_name, data_insert=data):
            return True
        
    except errors.WrongDataTypeList as wrong_type_error:
        raise errors.WrongDataTypeList("Datatype isn't an list") from wrong_type_error

    except errors.DataLengthError as wrong_data_lenght_error:
        raise errors.DataLengthError("column_name and data do not contain the same number of items.") from wrong_data_lenght_error

    except errors.InsertError as insert_error:
        raise errors.InsertError("Could not insert data into database.") from insert_error
    

def table_creator(table_name: str, columns: dict):
    creator = storage.Table_creator(database_name=DATABASE_NAME)
    try:
        if creator.create_table(
            table_name=table_name,
            columns=columns):
            return True

    except errors.WrongDataTypeDict as wrong_type_error:
        raise errors.WrongDataTypeDict("Datatype isn't an dictonary") from wrong_type_error
    
    except errors.TableError as table_error:
        raise errors.TableError(f"No such table: {table_name}") from table_error


def create_database(database_name: str):
    try:
        if storage.create_database(database_name=database_name):
            return True
        return False
    except errors.DatabaseError:
        return False