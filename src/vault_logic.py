import src.storage_logic as storage_logic
import src.cli as cli
import src.error as error

DATABASE_NAME = "CLI_Data.db"


def start_flow(email: str, userid: int):
    
    cli.clear_screen()

    data = get_five_rows_out_database(userid=userid)
    total_cred = storage_logic.get_all_items_in_database(userid=userid)

    showed_items = "_"
    if total_cred is None:
        total_cred = 0

    if data is None:
        showed_items = 0
    else:
        showed_items = len(data)

    if option_handler(cli.vault_screen(
        email=email,
        total_cred=total_cred,
        rows=data,
        showed_items=showed_items).lower()) is None:
        
        cli.print_internal_error()
        #Make a log entry that logs that there was something wrong while passing the choice
        #no selection from:"A", "V", "S", "E", "D", "Q

def option_handler(choice: str):
    if not choice in ["a", "v", "s", "d", "e", "q"]:
        return None
    
    dispatch_table = {
        "a": add_item,
        "v": view_screen,
        "s": search_item,
        "d": delete_item,
        "e": edit_item,
        "q": quit_program
    }
    func = dispatch_table.get(choice)
    func()
    return True

#search limted amount of items.
#get_all_items_in_database

#Gets 5 rows out of the database and returns data.
def get_five_rows_out_database(userid: int):
    try:
        data = storage_logic.search_limited_amount_of_items_in_database(
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
    except error.TableError:
        cli.print_incorrect_table_name()
        return False


def add_item():
    print("a")
    

def view_screen():
    print('v')

def search_item():
    print("s")

def delete_item():
    print("d")

def edit_item():
    print("e")

def quit_program():
    print("q")

if __name__ == "__main__":
    pass