import src.interface.vault_interface as vault_interface
import src.storage_logic as storage_logic
import src.crypto as crypto

def main(cred_id: int, userid: int, encryption_key: bytes) -> None:
    data = storage_logic.searcher(
        columns=["Service", "Username", "comment"],
        column=("cred_id",),
        data_to_search=cred_id
    )
    
    choice_table(
        choice=vault_interface.option_v_edit_handler(data=data),
        cred_id=cred_id,
        userid=userid,
        encryption_key=encryption_key
        )

def choice_table(choice, cred_id: int, userid: int, encryption_key: bytes) -> None:
    match choice:

        case "1":
            Edit_searcher.update_data(
                column="Service",
                cred_id=cred_id,
                userid=userid,
            )

        case "2":
            Edit_searcher.update_data(
                column="Username",
                cred_id=cred_id,
                userid=userid,
            )

        case "3":
            Edit_searcher.update_password(
                column="Password",
                cred_id=cred_id,
                userid=userid,
                encryption_key=encryption_key
            )

        case "4":
            Edit_searcher.update_data(
                column="Comment",
                cred_id=cred_id,
                userid=userid,
            )

class Edit_searcher:
    def __init__(self):
        self.question = vault_interface.Edit_data
        self.confirmation = vault_interface.Edit_data

    def update_data(self, column: str, cred_id: int, userid: int) -> True:
        while True:
            current_data = storage_logic.searcher(
                columns=[column,],
                column=("cred_id",),
                data_to_search=cred_id
            )[0][0]

            new_data = self.question.object_one(column, current_data)
            awnser = self.confirmation.confirmation()

            if awnser.lower() not in ("y", "yes"):
                continue
            break
                

        self.search = storage_logic.update_database_item(
            cred_id=cred_id,
            userid=userid,
            column=column,
            new_data=new_data
        )

        return True

    def update_password(self, column: str, cred_id: int, userid: int, encryption_key: bytes) -> True:
        while True:
                    password_encrypted = storage_logic.searcher(
                        columns=[column,],
                        column=("cred_id",),
                        data_to_search=cred_id
                    )[0][0]
                    current_data = crypto.password_decryption(
                        password=password_encrypted,
                        encryption_key=encryption_key
                    )


                    password_decrypted = self.question.object_password(column, current_data)
                    awnser = self.confirmation.confirmation()
        
                    if awnser.lower() not in ("y", "yes"):
                        continue
                    break

        password_encrypted = crypto.password_encryption(
            password=password_decrypted,
            encryption_key=encryption_key
        )
        
        self.search = storage_logic.update_database_item(
            cred_id=cred_id,
            userid=userid,
            column=column,
            new_data=password_encrypted
        )

        return True