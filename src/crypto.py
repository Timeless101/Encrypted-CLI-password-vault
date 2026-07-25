import bcrypt



#password encryption.
def hash_password(password: str):
    password = password
    salt = bcrypt.gensalt(rounds=12)
    bytes = password.encode("utf-8")
    hash_password = bcrypt.hashpw(bytes, salt)
    return hash_password, salt


#Check password
def verify_password(input_password: str, database_password: bytes):
    return bcrypt.checkpw(input_password.encode("utf-8"), database_password)

if __name__ == "__main__":
    ...