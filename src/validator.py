import re

#menu selection validator.
def main_menu_validator(selection: str) -> bool | int:
    try:
        int_selection: int = int(selection)
        if int_selection > 0 and int_selection <= 4:
            return int(selection)
        else:
            return False         
    except ValueError:
            return False


#password match validator.
def password_match_checker(passworda: str, passwordb: str) -> bool:
    if passworda == passwordb:
        return True
    else:
        return False


#Email check.
def email_checker(email: str) -> bool:
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return True
    else:
        return False


#Check if email allready exist.
def email_is_available(database_email: str, new_email: str) -> bool:
    if database_email == new_email:
        return False
    
    if database_email is None:
        return True

    if database_email != new_email:
        return True

if __name__ == "__main__":
    pass