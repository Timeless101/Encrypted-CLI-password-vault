import src.storage_logic as storage_logic
import src.interface.error_messages as error_messages
import src.interface.vault_interface as vault_interface
import src.errors as errors
from src.interface.helper_functions import clear_screen, exit_program
from src.vault_services.add_items import add_item_to_database as add_items
from src.vault_services.view_items import get_view_screen_data, data_handler, view_password
import math
import time


#Helper functions.
def get_five_rows_out_database(userid: int) -> list | None:
    try:
        data: list | None = storage_logic.search_limited_amount_of_items_in_database(
            userid=userid,
            limit=5
        )

        if data is None:
            return None

        if len(data) > 5:
            raise ValueError("Length of the data is not 5")
        
        return data
    
    except errors.TableError:
        error_messages.print_incorrect_table_name()
        return False

def option_handler(choice: str, userid: int, encryption_key: bytes, total_cred: int) -> str | None:
    if not choice in ["a", "v", "s", "d", "e", "q"]:
        return None
    
    dispatch_table = {
        "a": lambda: option_a(userid, encryption_key),
        "v": lambda: option_v(userid, total_cred, encryption_key),
        "s": option_s,
        "d": option_d,
        "e": option_e,
        "q": option_q
    }
    func = dispatch_table.get(choice)
    return func()

#Main flow
def start_flow(email: str, userid: int, encryption_key: bytes):

    try:
        clear_screen()

        data = get_five_rows_out_database(userid=userid)
        total_cred: int | None = storage_logic.get_all_items_in_database(userid=userid)

        showed_items = "_"
        if total_cred is None:
            total_cred = 0

        if data is None:
            showed_items = 0
        else:
            showed_items = len(data)

        successs = option_handler(
            choice=vault_interface.vault_screen(
                    email=email,
                    total_cred=total_cred,
                    rows=data,
                    showed_items=showed_items),
            userid=userid,
            encryption_key=encryption_key,
            total_cred=total_cred
            )
            
        if successs is None:
            error_messages.print_internal_error()
            #Make a log entry that logs that there was something wrong while passing the choice
            #no selection from:"A", "V", "S", "E", "D", "Q
        return successs
    except (KeyboardInterrupt, EOFError):
        exit_program()

def option_a(userid: int, encryption_key: bytes) -> str:
    clear_screen()
    while True:
        result = vault_interface.add_items_screen()
        confirmation = vault_interface.add_items_confirmation()
        match confirmation:
            case "y":
                if add_items(data=result, key=encryption_key, userid=userid):
                    break
                else:
                    error_messages.print_internal_error()
                    break

            case "n":
               continue
    return "a"
    
def select_item_flow(data: list) -> str:
    id_choice = vault_interface.ask_item_id()
    clear_screen()
    view_item_data = data_handler(data=data, choice=id_choice)

    if view_item_data is None:
        error_messages.print_option_out_of_range()
        return False

    return vault_interface.option_v_view_password_handler(data=view_item_data), id_choice

def password_item_flow(choice: str, userid: int, encryption_key: bytes, data: list[tuple], id_choice):
    match choice:

        case "r":
            if vault_interface.view_password_confirmation() == "y":
                print(view_password(encryption_key=encryption_key, data=data, id_choice=id_choice))
                time.sleep(500)

        case "e":
            pass
        case "d":
            pass
        case "b":
            return False



def option_v(userid: int, total_cred: int, encryption_key: bytes) -> str:

    current_page = 1
    page_size = 5
    offset = 0

    total_pages = math.ceil(total_cred / page_size)
    

    while True:
        clear_screen()

        pages = (current_page - 1) * page_size
        showed_items = pages + page_size

        showing_items_start = (current_page * page_size) - 4
        showing_items_end = min(current_page * page_size, total_cred)

        data = get_view_screen_data(
                userid=userid,
                page_size=page_size,
                offset=offset
                )

        option = vault_interface.option_v_screen_handler(
                data=data,
                total_credentials=total_cred,
                current_page=current_page,
                max_page=total_pages,
                showing_items_end=showing_items_end,
                showing_items_start=showing_items_start
                )

        match option:
            case "b":
                return "v"

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
                choice, id_choice = select_item_flow(data=data)
                if choice is None:
                    continue
                password_item_flow(choice=choice, id_choice=id_choice, data=data, encryption_key=encryption_key, userid=userid)



            case "a":
                option_a(userid=userid, encryption_key=encryption_key)


def option_s():
    print("s")

def option_d():
    print("d")

def option_e():
    print("e")

def option_q():
    return "q"

if __name__ == "__main__":
    pass