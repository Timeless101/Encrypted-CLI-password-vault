from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from src.interface.helper_functions import clear_screen
from getpass import getpass

CONSOLE = Console()

#Main vault screen functions
#layout vault screen
def vault_screen(email: str, total_cred: int, rows: list, showed_items: str):

    vault_screen_header(email, total_cred)
    vault_screen_small_table(rows)

    CONSOLE.print(f"\n[grey53]Showing {showed_items} of {total_cred} credentials\n")
    vault_options()

    return Prompt.ask("\n[bright_cyan]Option[/]", choices=["A", "V", "S", "E", "D", "Q"], case_sensitive=False, show_choices=False).lower()

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

    CONSOLE.print(panel)

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
    small_password_table.add_column("[cyan]EditedDate[/]", justify="left", no_wrap=True)

    for item in rows:
        cred_id, item_id, service_name, username, password, comment, creation_date, edit_date = item
        small_password_table.add_row(str(cred_id), service_name, username, "********", edit_date)

    CONSOLE.print("\n:lock:[bold bright_cyan] RECENT CREDENTIALS[/]\n")
    
    CONSOLE.print(small_password_table)

def vault_options():
    option_table = Table.grid()

    option_table.add_column(min_width=23)
    option_table.add_column(min_width=23)
    option_table.add_column(min_width=23)

    option_table.add_row("[bold bright_green][A] Add[/]", "[bold bright_blue][V] View[/]", "[bold bright_blue][S] Search[/]")
    option_table.add_row("[bold yellow][E] Edit[/]", "[bold red][D] Delete[/]", "[bold red][Q] Lock[/]")

    CONSOLE.print(option_table)


#vault option A

def add_items_confirmation():
    return Prompt.ask("\n[bright_cyan]Is al information correct?[/]", choices=["y", "N"], case_sensitive=False, show_choices=True).lower()

def add_items_screen():
    service, username, password, comment = add_items_screen_flow()
    return {"Service": service, "Username": username, "Password": password, "Comment": comment}

def vault_option_a_screen(service, username, password, comment):

    clear_screen()

    asterisk = "*" * len(password)
    table = Table.grid(padding=(0, 1), expand=False)

    table.add_column(justify="left",)
    table.add_column()

    table.add_row("[bright_cyan]Service: [/]", service)
    table.add_row("[bright_cyan]Username: [/]", username)
    table.add_row("[bright_cyan]Password: [/]", asterisk)
    table.add_row("[bright_cyan]Comment: [/]", comment)

    panel = Panel(
            table,
            width=70,
            padding=(0, 1))


    CONSOLE.print(panel)

def vault_option_a_question(name):
    return CONSOLE.input(f"[cyan]\n{name}: [/]")


def add_items_screen_flow() -> tuple[str, str, str, str]:

    vault_option_a_screen("", "", "", "")
    service: str = vault_option_a_question("Service")
    vault_option_a_screen(service, "", "", "")
    username: str = vault_option_a_question("Username")
    vault_option_a_screen(service, username, "","")
    password: str = getpass(echo_char="*")
    vault_option_a_screen(service, username, password, "")
    comment: str = vault_option_a_question("Comment")
    vault_option_a_screen(service, username, password, comment)

    return service, username, password, comment