import src.login_logic as login_logic
import src.vault_logic as vault_logic
from time import sleep

def program_flow():

    while True:
        data = login_logic.option_selection(login_logic.main_menu())
        if data is False:
            continue
        
        email, userid = data
        while True:
            result = vault_logic.start_flow(email=email, userid=userid)
            print(result)
            sleep(5)
            if result == "q":
                break
        
    


if __name__ == "__main__":
    pass