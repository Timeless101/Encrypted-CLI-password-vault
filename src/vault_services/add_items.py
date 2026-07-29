from src.crypto import password_encryption
from src.storage_logic import insert_data
from datetime import datetime
import src.errors as errors

def add_item_to_database(data: dict, key: bytes, userid: int) -> bool:
    current_time = datetime.now()

    service = data["Service"]
    username = data["Username"]
    password = data["Password"]
    comment = data["Comment"]

    encrypted_password = password_encryption(encryption_key=key, password=password)

    try:
        successs: bool = insert_data(
            table_name="vault_storage",
            column_name=[
                "UserID",
                "Service",
                "Username",
                "Password",
                "Comment",
                "CreationDate",
                "EditedDate"
            ],
            data=[
                userid,
                service,
                username,
                encrypted_password,
                comment,
                current_time.replace(microsecond=0),
                current_time.replace(microsecond=0)
            ]
        )

        if successs:
            return True
        
    except errors.WrongDataTypeList as wrong_type_error:  
        raise errors.WrongDataTypeList("Datatype isn't an list") from wrong_type_error
    
    except errors.DataLengthError as wrong_data_length_error:
        raise errors.DataLengthError("column_name and data do not contain the same number of items.") from wrong_data_length_error

    except errors.InsertError as insert_error:
        raise errors.InsertError("Could not insert data into database.") from insert_error

