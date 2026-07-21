from time import sleep
import src.error as error
import src.storage_logic as storage_logic
import src.cli as cli
import src.validator as validator
import src.crypto as crypto

DATABASE_NAME = "CLI_Data.db"
LOGIN_TABLE = "login_information"



#Exit helper Function
def exit_program():
    print("\n\nYou have exited the program!")
    return exit()

#Main menu selection plus validation.
def main_menu():
    if not initialize_database_bystartup():   
        cli.print_startup_failed()
        input("Press any key to quit: ")
        exit_program()
    
    cli.clear_screen()
    
    try:
        while True:
            selection = cli.main_menu()
            if selection in ["1", "2", "3","4"]:
                break
            else:
                cli.clear_screen()
                print("Please select an option from the list.")
                sleep(1.5)
                cli.clear_screen()
                continue
        return selection
    except (KeyboardInterrupt, EOFError):
        exit_program()

#menu selection.
def option_selection(option: str):
    dispatch_table = {
        "1": login_flow,
        "2": sign_up_flow,
        "3": about,
        "4": exit_program,
    }
    func = dispatch_table.get(option)
    return func()


#Initialize database creates and starts database.
def initialize_database_bystartup():
    try:
        if not storage_logic.create_database(database_name=DATABASE_NAME):
            return False
        
        table1 = storage_logic.table_creator(
            table_name=LOGIN_TABLE,
            columns={
            "Id": "INTEGER UNIQUE PRIMARY KEY",
            "Email": "TEXT UNIQUE NOT NULL",
            "Password": "TEXT NOT NULL",})
        
        table2 = storage_logic.table_creator(
            table_name="vault_storage",
            columns={
                "cred_id": "INTEGER PRIMARY KEY",
                "UserID": "INTEGER NOT NULL",
                "Service": "TEXT",
                "Username": "TEXT",
                "Password": "TEXT",
                "Comment": "TEXT"
            }
        )

        if table1 and table2:
            return True
        
        return False
        
    except error.WrongDataTypeDict:
        return False
    
    except error.TableError:
        return False

#Check if password match
def validate_password(input_password: str, database_password):
    if not crypto.verify_password(input_password=input_password, database_password=database_password):
        return False
    return True

#Function that the login uses to check the email and password in database.
def sign_in_function(email: str, password: str):

    if not validator.email_checker(email):
        raise error.EmailMismatchError("Email doesn't match the criteria.")
    
    row = storage_logic.data_row_search(email=email, table_column="Email", table_name="login_information")
    
    if row is None:
        raise error.AccountError("Account doesn't exists.")
    
    _, _, database_password = row

    if not validate_password(input_password=password, database_password=database_password):
        raise error.InvalidPasswordError("Wrong password has been enterd.")
    
    return True

#Gets the UserID out of the database.
def get_userid(email):
    row = storage_logic.data_row_search(email=email, table_column="Email", table_name="login_information")
    if row is None:
        raise error.AccountError("Account doesn't exists.")
    
    userid, _, _, = row
    return int(userid)

#Login function flow.
def login_flow():
    cli.clear_screen()
    try:
        while True:
            try:
                input_email, input_password = cli.login_screen()
                if sign_in_function(email=input_email, password=input_password):
                    
                    return input_email, get_userid(input_email)

            except error.EmailMismatchError:
                cli.print_invalid_email()
                sleep(1.5)
                cli.clear_screen()
                continue

            except error.AccountError:
                cli.print_account_not_in_database()
                sleep(1.5)
                cli.clear_screen()
                continue

            except error.InvalidPasswordError:
                cli.print_wrong_password()
                sleep(1.5)
                cli.clear_screen()
                continue

    except (KeyboardInterrupt, EOFError):
        exit_program()

#Database search email return str email.
def email_search(email):
    try:

        data = storage_logic.search_data(
            table_name="login_information",
            table_column="Email",
            data_to_be_searched=email
        )

        if data is None:
            return None

        first_data = data[0]
        second_data = first_data[1]
        return second_data
    
    except error.TableError:
        cli.print_search_error()
        return False

#Gets input from CLI and return it to sign-up flow.
def get_input_and_validate_it():

    email, password1, password2 = cli.register_screen()

    if not validator.email_checker(email):
        raise error.EmailMismatchError("Email doesn't match the criteria.")
    
    if not validator.password_match_checker(password1, password2):
        raise error.PasswordMismatchError("Passwords don't match")
    
    if not validator.email_is_available(new_email=email, database_email=email_search(email)):
        raise error.DuplicationError("Email already exists in database.")
    
    return email, crypto.hash_password(password1)


def sign_up_flow():
    cli.clear_screen()
    try:
        while True:
            try:
                email, password_hash = get_input_and_validate_it()

                success = storage_logic.insert_data(
                    table_name= "login_information",
                    column_name= ["Email", "password"],
                    data= [email, password_hash])
                
                if not success:
                    cli.print_error_data_insert()
                    cli.clear_screen()
                    continue
                    #Print path to log file. and wait for input, after go to menu.

                return email , get_userid(email)
                
            except error.EmailMismatchError:
                    cli.print_invalid_email()
                    sleep(3)
                    cli.clear_screen()
                    continue
            
            except error.PasswordMismatchError:
                    cli.print_password_dont_match()
                    sleep(3)
                    cli.clear_screen()
                    continue
            
            except error.DuplicationError:
                    cli.print_email_exists()
                    sleep(3)
                    cli.clear_screen()
                    continue
            
            except error.WrongDataTypeDict:
                cli.print_wrong_data_type_dict()
                sleep(3)
                #Make log file
                exit_program()

            except error.TableError:
                cli.print_incorrect_table_name()
                sleep(3)
                #Make log file
                exit_program()

    except (KeyboardInterrupt, EOFError):
        exit_program()

#Shows Information about the Maker and program.
def about():
    cli.clear_screen()
    if cli.about_screen():
        return False
    

if __name__ == "__main__":
    ...