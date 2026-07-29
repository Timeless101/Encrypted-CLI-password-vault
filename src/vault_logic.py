import src.storage_logic as storage_logic
import src.interface.error_messages as error_messages
import src.interface.vault_interface as vault_interface
from src.interface.helper_functions import clear_screen, exit_program
import src.errors as errors
from src.vault_services.add_items import add_item_to_database as add_items


#Helper functions.
def get_five_rows_out_database(userid: int) -> list | None:
    try:
        data: list | None = storage_logic.search_limited_amount_of_items_in_database(
            table="vault_storage",
            column="UserID",
            userid=userid,
            amount_of_items=5
        )

        if data is None:
            return None

        if len(data) > 5:
            raise ValueError("Length of the data is not 5")
        
        return data
    except errors.TableError:
        error_messages.print_incorrect_table_name()
        return False

def option_handler(choice: str) -> str | None:
    if not choice in ["a", "v", "s", "d", "e", "q"]:
        return None
    
    dispatch_table = {
        "a": option_a,
        "v": option_v,
        "s": option_s,
        "d": option_d,
        "e": option_e,
        "q": option_q
    }
    func = dispatch_table.get(choice)
    return func()

#Main flow
def start_flow(email: str, userid: int, encryption_key: bytes):
    global key
    key = encryption_key

    global usrid
    usrid = userid

    try:
        clear_screen()

        data = get_five_rows_out_database(userid=userid)
        total_cred = storage_logic.get_all_items_in_database(userid=userid)

        showed_items = "_"
        if total_cred is None:
            total_cred = 0

        if data is None:
            showed_items = 0
        else:
            showed_items = len(data)

        successs = option_handler(vault_interface.vault_screen(
            email=email,
            total_cred=total_cred,
            rows=data,
            showed_items=showed_items))
            
        if successs is None:
            error_messages.print_internal_error()
            #Make a log entry that logs that there was something wrong while passing the choice
            #no selection from:"A", "V", "S", "E", "D", "Q
        return successs
    except (KeyboardInterrupt, EOFError):
        exit_program()

def option_a():
    clear_screen()
    while True:
        result = vault_interface.add_items_screen()
        confirmation = vault_interface.add_items_confirmation()
        match confirmation:
            case "y":
                if add_items(data=result, key=key, userid=usrid):
                    break
                else:
                    error_messages.print_internal_error()
                    break

            case "n":
               continue
    return "a"
    
    

def option_v():
    print('v')

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