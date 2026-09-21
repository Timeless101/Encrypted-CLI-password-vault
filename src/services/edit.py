import src.interface.edit_interface as edit_interface
import src.storage_logic as storage_logic
import src.crypto as crypto

class Edit_searcher:

    def update_data(self, column: str, cred_id: int, userid: int) -> True:
        while True:
            current_data = storage_logic.searcher(
                columns=[column,],
                column=("cred_id",),
                data_to_search=cred_id,
                userid=userid
            )[0][0]

            new_data = edit_interface.Edit_prompt.new_data_question(column, current_data)
            awnser = edit_interface.Edit_prompt.confirmation()

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
                        data_to_search=cred_id,
                        userid=userid
                    )[0][0]

                    current_data = crypto.password_decryption(
                        password=password_encrypted,
                        encryption_key=encryption_key
                    )

                    password_decrypted = edit_interface.Edit_prompt.new_data_question(column, current_data)
                    awnser = edit_interface.Edit_prompt.confirmation()
        
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

def main(cred_id: int, userid: int, encryption_key: bytes) -> None:

    data = storage_logic.searcher(
        columns=["Service", "Username", "comment"],
        column=("cred_id",),
        data_to_search=cred_id,
        userid=userid
    )
    
    choice_table(
        choice=edit_interface.handler(data=data),
        cred_id=cred_id,
        userid=userid,
        encryption_key=encryption_key
        )

def choice_table(choice, cred_id: int, userid: int, encryption_key: bytes) -> None:
    update = Edit_searcher()
    match choice:

        case "1":
            update.update_data(
                column="Service",
                cred_id=cred_id,
                userid=userid,
            )

        case "2":
            update.update_data(
                column="Username",
                cred_id=cred_id,
                userid=userid,
            )

        case "3":
            update.update_password(
                column="Password",
                cred_id=cred_id,
                userid=userid,
                encryption_key=encryption_key
            )

        case "4":
            update.update_data(
                column="Comment",
                cred_id=cred_id,
                userid=userid,
            )