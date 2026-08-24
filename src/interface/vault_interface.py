from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from src.interface.helper_functions import clear_screen
from getpass import getpass

CONSOLE = Console()

#Main vault screen functions

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
        item_id,service_name, username, edit_date = item
        small_password_table.add_row(str(item_id), service_name, username, "********", edit_date)

    CONSOLE.print("\n:lock:[bold bright_cyan] RECENT CREDENTIALS[/]\n")
    
    CONSOLE.print(small_password_table)

def vault_options():
    option_table = Table.grid()

    option_table.add_column(min_width=23)
    option_table.add_column(min_width=23)
    option_table.add_column(min_width=23)

    option_table.add_row("[bold bright_green][A] Add[/]", "[bold bright_blue][V] View[/]", "[bold bright_blue][S] Search[/]")
    option_table.add_row("[bold red][Q] Lock[/]", "", "")

    CONSOLE.print(option_table)

def vault_screen(email: str, total_cred: int, rows: list, showed_items: str):

    vault_screen_header(email, total_cred)
    vault_screen_small_table(rows)

    CONSOLE.print(f"\n[grey53]Showing {showed_items} of {total_cred} credentials\n")
    vault_options()

    return Prompt.ask("\n[bright_cyan]Option[/]", choices=["A", "V", "S", "Q"], case_sensitive=False, show_choices=False).lower()

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

#Option View_items

def view_password_confirmation():
    return Prompt.ask("\n[bright_cyan]Are you sure you want to reveal the password?[/]", choices=["y", "N"], case_sensitive=False, show_choices=True).lower()

def view_password_delete_confirmation():
    return Prompt.ask("\n:warning:[bright_cyan] Are you sure you want to delete this item?[/]:warning:", choices=["y", "N"], case_sensitive=False, show_choices=True).lower()

def ask_item_id():
    return IntPrompt.ask("[cyan]Item ID[/]")

def option_v_header(total_credentials: int) -> None:
    table = Table.grid(expand= True)

    table.add_column(justify="left", no_wrap=True)
    table.add_column(justify="right", no_wrap=True)

    table.add_row(":locked_with_key: [bold bright_cyan] All Credentials[/]", ":white_heavy_check_mark: [bright_green]Vault Unlocked[/]")
    table.add_row("", "")
    table.add_row("Browse saved credentials", f"{total_credentials} [bold grey53]Credentials[/]")

    panel = Panel(
        table,
        width=70,
        padding= (0, 1)
    )

    CONSOLE.print(panel)
    print("\n")

    

def option_v_main_view(data: list):

    table = Table()

    table.add_column("#")
    table.add_column("[bold bright_cyan]Service[/]")
    table.add_column("[bold bright_cyan]Username[/]")
    table.add_column("[bold bright_cyan]Password[/]")
    table.add_column("[bold bright_cyan]Comment[/]")
    table.add_column("[bold bright_cyan]Edited[/]")

    asterisk = "*" * 8

    for item in data:
        items_id, cred_id, service, username, comment, editdate = item
        table.add_row(str(items_id), service, username, asterisk, comment, editdate)

    CONSOLE.print(table)

def option_v_options(total_cred: int, current_page:int, max_page: int, showing_items_end: int, showing_items_start: int) -> str:
    table = Table.grid(expand= True)
    
    table.add_column(justify="left", no_wrap=True)
    table.add_column(justify="center", no_wrap=True)
    table.add_column(justify="right", no_wrap=True)

    table.add_row("[bright_blue][P] Previous[/]", "[yellow][B] Back[/]", "[bright_blue][N] Next[/]")
    table.add_row("", "")
    table.add_row(f"[grey53]Showing {showing_items_start}-{showing_items_end} of {str(total_cred)}][/]", f"[cyan] Page {current_page}/{max_page}[/]", r"[cyan]\[#] Open item[/]")
    panel = Panel(
        table,
        width=70,
        padding= (0, 1)
    )

    CONSOLE.print(panel)

    return Prompt.ask("\n[bright_cyan]Option[/]", choices=["P", "B", "N", "#"], case_sensitive=False, show_choices=False)

def option_v_no_itmes_options() -> str:

    empty_vault = ":information: [bold yellow]No recent passwords added[/] :information:"
    panel1 = Panel(
        empty_vault,
        width=70
    )
    CONSOLE.print(panel1,"\n")

    table = Table.grid(expand= True)
        
    table.add_column(justify="left", no_wrap=True)
    table.add_column(justify="center", no_wrap=True)
    table.add_column(justify="right", no_wrap=True)

    table.add_row("[bright_green][A] Add credential[/]")
    table.add_row("", "", "")
    table.add_row("[yellow][B] Back[/]")
    panel = Panel(
        table,
        width=70,
        padding= (0, 1)
    )
    
    CONSOLE.print(panel)
    
    return Prompt.ask("\n[bright_cyan]Option[/]", choices=["A", "B"], case_sensitive=False, show_choices=False)

def option_v_view_password_header():
    table = (":locked_with_key: [bold bright_cyan] Credential Details[/]")

    panel = Panel(
        table,
        width= 70
    )

    CONSOLE.print(panel)

def option_v_view_password_item(data: list) -> str:

    service, username, comment, created, editeddate = data

    table = Table.grid(expand=True)

    table.add_column(no_wrap=True)
    table.add_column(no_wrap=True)

    table.add_row("[grey70]Service[/]", service)
    table.add_row("[grey70]Username[/]", username)
    table.add_row("[grey70]Password[/]", "********")
    table.add_row("[grey70]Comment[/]", comment)
    table.add_row("[grey70]Created[/]", created)
    table.add_row("[grey70]Last edited[/]", editeddate)

    panel = Panel(
        table,
        width=70,
    )

    CONSOLE.print(panel)

def option_v_view_password_plain(data: list, password: str) -> None:

    _, service, username, comment, created, editeddate = data[0]

    table = Table.grid(expand=True)

    table.add_column(no_wrap=True)
    table.add_column(no_wrap=True)

    table.add_row("[grey70]Service[/]", str(service))
    table.add_row("[grey70]Username[/]", username)
    table.add_row("[grey70]Password[/]", password)
    table.add_row("[grey70]Comment[/]", comment)
    table.add_row("[grey70]Created[/]", created)
    table.add_row("[grey70]Last edited[/]", editeddate)

    panel = Panel(
        table,
        width=70,
    )

    CONSOLE.print(panel)

def option_v_password_plain_choices() -> str:
    table = Table.grid(expand=True)

    table.add_column()
    table.add_column()

    table.add_row("[green][C] Copy[/]", "[yellow][B] Back[/]")

    panel = Panel(
        table,
        width=70
    )

    CONSOLE.print(panel)

    return Prompt.ask("\n[bright_cyan]Option[/]", choices=["b", "c"], case_sensitive=False, show_choices=False)

def view_password_plain_handeler(data: list[tuple], password: str):
    option_v_view_password_header()
    option_v_view_password_plain(data=data, password=password)
    return option_v_password_plain_choices().lower()

def option_v_view_password_options() -> str:
    table = Table.grid(expand=True)

    table.add_column(no_wrap=True)
    table.add_column(no_wrap=True)
    table.add_column(no_wrap=True)
    table.add_column(no_wrap=True)

    table.add_row("[cyan][R] Reveal Password[/]", "[yellow][E] Edit[/]", "[red][D] Delete[/]", "[yellow][B] Back[/]")

    panel = Panel(
        table,
        width=70
    )

    CONSOLE.print(panel)

    return Prompt.ask("\n[bright_cyan]Option[/]", choices=["r", "r", "d", "b"], case_sensitive=False, show_choices=False)

def option_v_view_password_handler(data: list) -> str:
    option_v_view_password_header()
    option_v_view_password_item(data=data)
    return option_v_view_password_options()

def option_v_screen_handler(data: list, total_credentials: int, current_page: int, max_page: int, showing_items_end: int, showing_items_start: int) -> str:

    if data is None:
        option_v_header(total_credentials=total_credentials)
        option_no_items = option_v_no_itmes_options().lower()
        return option_no_items

    option_v_header(total_credentials=total_credentials)
    CONSOLE.print("\n:lock: [bold bright_cyan]CREDENTIALS [/]\n")
    option_v_main_view(data=data)
    print("\n")
    
    option: str =  option_v_options(
            total_cred=total_credentials,
            current_page=current_page,
            max_page=max_page,
            showing_items_end=showing_items_end,
            showing_items_start=showing_items_start
            ).lower()

    return option