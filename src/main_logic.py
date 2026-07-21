import src.login_logic as login_logic
import src.vault_logic as vault_logic
from time import sleep

def program_flow():

    while True:
        data = login_logic.option_selection(login_logic.main_menu())
        if data is False:
            continue
        else:
            email, userid = data
            break
    
    vault_logic.start_flow(email=email, userid=userid)


if __name__ == "__main__":
    pass