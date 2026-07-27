import src.login_logic as login_logic
import src.vault_logic as vault_logic

def program_flow():

    while True:
        data = login_logic.option_selection(login_logic.main_menu())
        if data is False:
            continue
        
        email, userid, encryption_key = data
        while True:
            result = vault_logic.start_flow(email=email, userid=userid, encyption_key=encryption_key)
            match result:
                case "q":
                    encryption_key = None
                    break

                case "a":
                    continue


if __name__ == "__main__":
    pass