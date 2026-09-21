import math
import pyperclip
import src.storage as storage
import src.interface.error_messages as error_messages
import src.interface.view_interface as view_interface
import src.errors as errors
from src.services import edit
from src.crypto import password_decryption
from src.services.helper_functions import clear_screen
from src.services.helper_functions import clear_screen, print_copy, confirmation_prompt
from src.services.add_items import add_main


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

def password_item_flow(choice: str, encryption_key: bytes, data: list[tuple], id_choice, userid: int, cred_id: int):
    match choice:

        case "r":
            if confirmation_prompt(text="\n[bright_cyan]Are you sure you want to reveal the password?[/]") == "y":
                clear_screen()
                password = view_password(encryption_key=encryption_key, data=data, id_choice=id_choice)
                while True:
                    clear_screen()
                    if view_interface.view_password_plain_handeler(data=data, password=password) == "c":
                        pyperclip.copy(password)
                        print_copy()
                    else:
                        break
                    
        case "e":
            edit.main(cred_id=cred_id, userid=userid, encryption_key=encryption_key)

        case "d":
            if confirmation_prompt(text="\n:warning:[bright_cyan] Are you sure you want to delete this item?[/]:warning:") == "y":
                delete_item(cred_id=id_choice)
            pass
                
            
        case "b":
            return False

def select_item_flow(data: list) -> str:
    id_choice: int = view_interface.ask_item_id()
    clear_screen()
    view_item_data, cred_id = data_handler(data=data, choice=id_choice)

    if view_item_data is None:
        error_messages.print_option_out_of_range()
        return False

    return view_interface.view_password_handler(data=view_item_data), id_choice, cred_id


def new_func(userid: int, page_size: int, offset: int, total_cred: int, current_page: int, total_pages: int, showing_items_end: int, showing_items_start: int):
    data: list[tuple] = get_view_screen_data(
        userid=userid,
        page_size=page_size,
        offset=offset
        )

    option: str = view_interface.screen_handler(
            data=data,
            total_credentials=total_cred,
            current_page=current_page,
            max_page=total_pages,
            showing_items_end=showing_items_end,
            showing_items_start=showing_items_start
            )
    return option, data

def openitem(data: list, encryption_key: bytes, userid: int):
    result = select_item_flow(data=data)
    if result is False:
        return False
    
    choice, id_choice, cred_id = result

    if choice is None:
        return False
    password_item_flow(choice=choice, id_choice=id_choice, data=data, encryption_key=encryption_key, userid=userid, cred_id=cred_id)

def pagination(userid: int, total_cred: int, encryption_key: bytes) -> str:

    current_page: int = 1
    page_size: int = 5
    offset: int = 0
    total_pages: int = math.ceil(total_cred / page_size)
    
    while True:
        clear_screen()

        pages: int = (current_page - 1) * page_size
        showed_items: int = pages + page_size

        showing_items_start: int = (current_page * page_size) - 4
        showing_items_end: int = min(current_page * page_size, total_cred)

        option, data = new_func(
                        userid=userid,
                        page_size=page_size,
                        offset=offset,
                        total_cred=total_cred,
                        current_page=current_page,
                        total_pages=total_pages,
                        showing_items_end=showing_items_end,
                        showing_items_start=showing_items_start
                    )

        match option:
            case "b":
                return ""

            case "n":
                if showed_items < total_cred:
                    current_page += 1
                    offset += page_size
                    continue

            case "p":
                if showed_items > page_size:
                    current_page -= 1
                    offset -= page_size
                    continue

            case "#":
                openitem(data=data, encryption_key=encryption_key, userid=userid)

            case "a":
                add_main(userid=userid, encryption_key=encryption_key)