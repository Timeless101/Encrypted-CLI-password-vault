import subprocess
from time import sleep

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