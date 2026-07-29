import subprocess

def exit_program():
    print("\n\nYou have exited the program!")
    return exit()

def clear_screen():
    command = ['cmd']
    args = ['/c','cls']
    cli = command + args
    subprocess.run(cli)

