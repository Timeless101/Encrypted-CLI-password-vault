import src.storage as storage
import src.interface.error_messages as error_messages
import src.errors as errors
from src.crypto import password_decryption
import time
def get_view_screen_data(userid: int, page_size: int, offset: int) -> list[tuple]:

    rows = storage.Search_data.search_for_view_items(
        userid=userid,
        limit=page_size,
        offset=offset,
        database="CLI_Data.db"
    )

    return rows


def data_handler(data: list[tuple], choice: int ) -> tuple:
    cred_id = get_cred_id(data=data, choice=choice)

    data = storage.Search_data.search_specific_data(
            database_name="CLI_Data.db",
            table="vault_storage",
            column="cred_id",
            data_to_be_searched=cred_id
        )

    if data is None:
        return None

    return (data[0][2], data[0][3], data[0][5], data[0][6], data[0][7]), cred_id # returns service, username, comment, creationdate, editeddate.

def get_cred_id(data: list[tuple], choice: int):
    for item in data:
        if item[0] == choice:
            return item[1]
        else:
            continue

def view_password(encryption_key: bytes, data: list[tuple], id_choice: int):
    password = storage.Search_data.search_specific_data(
                database_name="CLI_Data.db",
                table="vault_storage",
                column="cred_id",
                data_to_be_searched=get_cred_id(data=data, choice=id_choice)
            )

    return password_decryption(encryption_key=encryption_key, password=password[0][4])

def delete_item(cred_id: int):
    try:
        if storage.delete_item(
        database="CLI_Data.db",
        table="vault_storage",
        cred_id=cred_id
        ):
            return True
    except errors.WrongSQLStatement:
        error_messages.print_internal_error()
        return False
    except errors.DatabaseError:
        error_messages.print_internal_error()
        return False
    except errors.UnexpectedError:
        error_messages.print_contact_support()
        return False
    