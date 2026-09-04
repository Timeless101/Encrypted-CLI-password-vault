import subprocess
from time import sleep
from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator

def exit_program():
    print("\n\nYou have exited the program!")
    return exit()

def clear_screen():
    command = ['cmd']
    args = ['/c','cls']
    cli = command + args
    subprocess.run(cli)

def print_copy():
    print("\n\n Password copied!")
    sleep(0.8)

def get_password_with_complexity():
    password = inquirer.secret(
                message="Retype password:",
                qmark="",
                amark="",
                validate=PasswordValidator(
                    length=8,
                    cap=True,
                    special=True,
                    number=True,
                    message="Password doesn't meet complexity",
                ),
            ).execute()
    return password