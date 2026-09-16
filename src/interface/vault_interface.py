from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

CONSOLE = Console()

def vault_header(email: str, total_cred: int):
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

def vault_small_table(rows: list):

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

    option_table.add_row("[bold bright_green][A] Add[/]", "[bold magenta][V] View[/]", "[bold bright_blue][S] Search[/]")
    option_table.add_row("[bold red][Q] Lock[/]", "", "")

    CONSOLE.print(option_table)

def vault_screen(email: str, total_cred: int, rows: list, showed_items: str):

    vault_header(email, total_cred)
    vault_small_table(rows)

    CONSOLE.print(f"\n[grey53]Showing {showed_items} of {total_cred} credentials\n")
    vault_options()

    return Prompt.ask("\n[bright_cyan]Option[/]", choices=["A", "V", "S", "Q"], case_sensitive=False, show_choices=False).lower()