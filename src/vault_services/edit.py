import src.interface.vault_interface as vault_interface
import src.storage_logic as storage_logic

def main(cred_id: int):
    data = storage_logic.searcher(
        columns=["Service", "Username", "comment"],
        column=("cred_id",),
        data_to_search=cred_id
    )
    
    choice_table(
        choice=vault_interface.option_v_edit_handler(data=data),
        cred_id=cred_id
        )

def choice_table(choice, cred_id):
    match choice:

        case "1":
            vault_interface.Edit_data.object_one()

        case "2":
            pass

        case "3":
            pass

        case "4":
            pass

#WIP Need the function that update the data in the database.
class Edit_searcher:
    def __init__(self, columns, cred_id, new_data):
        self.search = storage_logic.searcher(
            columns=[columns,],
            column=(cred_id,),
            data_to_search=cred_id
        )