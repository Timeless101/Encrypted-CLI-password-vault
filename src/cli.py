from pystyle import Colors, Colorate
from getpass import getpass
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import subprocess

CONSOLE = Console()

#clear the screen.
def clear_screen():
    command = ['cmd']
    args = ['/c','cls']
    cli = command + args
    subprocess.run(cli)

#Exit helper Function
def exit_program():
    print("\n\nYou have exited the program!")
    return exit()

global MAIN_SCREEN_LOGO
MAIN_SCREEN_LOGO = r"""
    _____________________________________________________________________________________
    |                                                                                   |
    |       _____                                    _  __      __         _ _          |
    |      |  __ \                                  | | \ \    / /        | | |         |
    |      | |__) |_ _ ___ _____      _____  _ __ __| |  \ \  / /_ _ _   _| | |_        |
    |      |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |   \ \/ / _` | | | | | __|       |
    |      | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |    \  / (_| | |_| | | |_        |
    |      |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|     \/ \__,_|\__,_|_|\__|       |
    |                                                                                   |
    |   By Diego                                                                        |
    |___________________________________________________________________________________| 
        """
global MAIN_SCREEN_OPTIONS
MAIN_SCREEN_OPTIONS= """
    Options:
    1) Login
    2) Sign-Up
    3) About
    4) Exit
            """

def main_menu():
    print(Colorate.Horizontal(Colors.rainbow, MAIN_SCREEN_LOGO), MAIN_SCREEN_OPTIONS)
    selection = input("Selection: ")
    return selection

def login_screen():
    login_screen = r"""
________________________________________________________________
|    _                 _                                       |
|   | |               (_)                                      |
|   | |     ___   __ _ _ _ __    ___  ___ _ __ ___  ___ _ __   |
|   | |    / _ \ / _` | | '_ \  / __|/ __| '__/ _ \/ _ \ '_ \  |
|   | |___| (_) | (_| | | | | | \__ \ (__| | |  __/  __/ | | | |
|   \_____/\___/ \__, |_|_| |_| |___/\___|_|  \___|\___|_| |_| |
|                 __/ |                                        |
|                |___/                                         |
|______________________________________________________________| 

                    """    
    print(Colorate.Horizontal(Colors.rainbow, login_screen))
    username = input("Email: ").strip().lower()
    password = getpass()
    return username, password
    
def register_screen():
    register_screen = r"""
 ____________________________________________       
 |   _____ _                                |
 |  /  ___(_)                               |
 |  \ `--. _  __ _ _ __ ______ _   _ _ __   |
 |   `--. \ |/ _` | '_ \______| | | | '_ \  |
 |  /\__/ / | (_| | | | |     | |_| | |_) | |
 |  \____/|_|\__, |_| |_|      \__,_| .__/  |
 |            __/ |                 | |     |
 |           |___/                  |_|     |
 |__________________________________________|

"""
    print(Colorate.Horizontal(Colors.rainbow, register_screen), "\n")
    email = input("Email: ").strip().lower()
    password1 = getpass()
    password2 = getpass("Retype password: ")
    return (email, password1, password2)


def about_screen():
    about_screen = r"""
___________________________________
|    ___  _                 _     |
|   / _ \| |               | |    |
|  / /_\ \ |__   ___  _   _| |_   |
|  |  _  | '_ \ / _ \| | | | __|  |
|  | | | | |_) | (_) | |_| | |_   |
|  \_| |_/_.__/ \___/ \__,_|\__|  |
|_________________________________|
"""
    print(Colorate.Horizontal(Colors.rainbow, about_screen))
    print("\nEncrypted Command Line Password Vault.")
    print("This is my first big project")
    print("\nBy: Diego")
    print("Create: Created: 09/04/2026 dd/mm/yy")
    
    input("\n\nwaiting for input: ")
    return True

#Vault screen header.
def vault_screen_header(email: str, total_cred: int):
    grid_title = Table.grid(expand=True)
    grid_title.add_column(justify="left", no_wrap=True)
    grid_title.add_column(justify="right", no_wrap=True)

    grid_title.add_row(":locked_with_key: [bold bright_cyan]Encrypted Vault[/]", ":white_heavy_check_mark: [bold bright_green]Unlocked[/]")
    grid_title.add_row("", "")
    grid_title.add_row(email, f"{total_cred} [bold grey53]Credentials[/]")

    panel = Panel(
        grid_title,
        width=70,
        padding=(0, 1)
    )

    return CONSOLE.print(panel)


#Small main table that shows 5 items in vault.
def vault_screen_small_table(rows: list):

    if rows is None:
        empty_vault = ":information: [bold yellow]No recent passwords added[/] :information:"
        panel1 = Panel(
            empty_vault,
            width=70
        )
        return CONSOLE.print(panel1)

    small_password_table = Table(width=70)
    small_password_table.add_column("[cyan]ID[/]", justify="center")
    small_password_table.add_column("[cyan]Service[/]", justify="left")
    small_password_table.add_column("[cyan]Username[/]", justify="left")
    small_password_table.add_column("[cyan]Password[/]", justify="left")

    for item in rows:
        cred_id, item_id, service_name, username, password, comment = item
        small_password_table.add_row(str(cred_id), service_name, username, "********")

    CONSOLE.print("\n:lock:[bold bright_cyan] RECENT CREDENTIALS[/]\n")
    
    return CONSOLE.print(small_password_table)
        
        

#Makes the vault screen layout.
def vault_screen(email: str, total_cred: int, rows: list, showed_items: str):

    vault_screen_header(email, total_cred)
    vault_screen_small_table(rows)

    CONSOLE.print(f"\n[grey53]Showing {showed_items} of {total_cred} credentials\n")
    vault_options()

    return Prompt.ask("\n[bright_cyan]Option[/]", choices=["A", "V", "S", "E", "D", "Q"], case_sensitive=False, show_choices=False)

#Vaul
def vault_options():
    option_table = Table.grid()

    option_table.add_column(min_width=23)
    option_table.add_column(min_width=23)
    option_table.add_column(min_width=23)

    option_table.add_row("[bold bright_green][A] Add[/]", "[bold bright_blue][V] View[/]", "[bold bright_blue][S] Search[/]")
    option_table.add_row("[bold yellow][E] Edit[/]", "[bold red][D] Delete[/]", "[bold red][Q] Lock[/]")

    return CONSOLE.print(option_table)

def password_table(databaseid: str, name: str, password: str):
    table = Table(title="Passwords")

    table.add_column("Id", justify="center", style="cyan", no_wrap=True)
    table.add_column("Name", justify="center", style="red")
    table.add_column("password", justify="center", style="green")

    table.add_row(databaseid, name, password)


    return CONSOLE.print(table)


def vault_option_a_questions():
        service = CONSOLE.input("[bright_cyan]Service name: [/]")
        username = CONSOLE.input("[bright_cyan]Username: [/]")
        password = CONSOLE.input("[bright_cyan]Password: [/]")
        comment = CONSOLE.input("[bright_cyan]comment: [/]")

        return service, username, password, comment

def vault_option_a():
    while True:
        service, username, password, comment = vault_option_a_questions()

        closed_question = Prompt.ask(
            "\n[bright_cyan]information correct? y/n[/]",
            choices=["y", "n", "yes", "no"],
            case_sensitive=False,
            show_choices=False
            ).lower()
        
        if closed_question in ["y", "yes"]:
            return service, username, password, comment
            
        elif closed_question in ["n", "no"]:
            print("\n")
            continue


#Database errors:
def print_error_database():
    CONSOLE.print("\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]COULD_NOT_CREATE_DATABASE[/]", print_contact_support())

def print_insert_error():
    CONSOLE.print("\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]DATABASE_INSERT_ERROR:[/]\n Couldn't insert data into database.")

def print_error_data_insert():
    print("There was an problem with inserting your data into the database", print_contact_support())

def print_search_error():
    print("\nCould not search in database.", print_contact_support())

def print_database_data_row_search():
    print("\nCouln't search for the data in the database.", print_contact_support())

def print_email_exists():
    CONSOLE.print("\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]EMAIL_EXISTS_IN_DATABASE[/]")

def print_account_not_in_database():
    CONSOLE.print("\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]ACCOUNT_NOT_IN_DATABASE[/]")

def print_table_creation_error():
    CONSOLE.print("\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]CAN'T_CREATE_TABLE_WITH_THE_GIVEN_TABLENAME_OR_DATA[/]")

def print_startup_failed():
    CONSOLE.print("\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]DATABASE_STARTUP_FAILED[/]")

def print_incorrect_table_name():
    CONSOLE.print("\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]WRONG_TABLENAME_ENTERD[/]")

#Wronge type errors:
def print_wrong_data_type_dict():
    CONSOLE.print("\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]WRONG_DATATYPE_ENTERD_FOR_TABLE_CREATON\n NOTE: Datatype must be dictionary.[/]")

def print_wrong_data_type_list():
    CONSOLE.print("\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]WRONG_DATATYPE_ENTERD_FOR\nNOTE: Datatype must be a list.[/]")

def print_list_length_error():
    CONSOLE.print("\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]LIST_LENGTH_ERROR[/]\nNOTE: Column name and data insert list length isn't the same.")

#Invalid Input errors:
def print_invalid_email():
    CONSOLE.print("\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]EMAIL_DOESN'T_MATCH_THE_CRITERIA[/]")

def print_password_dont_match():
    CONSOLE.print("\n\n\n:warning: [bold red]ERROR![/bold red]:warning:\n [red]PASSWORD_DON'T_MATCH.[/]\nPlease try again.")

def print_wrong_password():
    CONSOLE.print("\n\n\n:warning: [bold red]ERROR![/bold red]:warning:\n[red]WRONG_PASSWORD_ENTERD[/]")

def print_contact_support():
    return print("\nSomething went wrong, please contact support for further help.")

def print_internal_error():
    CONSOLE.print("\n\n:warning: [bold red]ERROR[/] :warning:\n [red]INTERNAL ERROR[/] \nSomething happend with the system.\n", print_contact_support())

if __name__ == "__main__":
    pass

