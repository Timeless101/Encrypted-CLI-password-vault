import src.interface.vault_interface as vault_interface
import src.storage_logic as storage_logic

def main(cred_id: int):
    data = storage_logic.searcher(
        columns=["Service", "Username", "comment"],
        column=("cred_id",),
        data_to_search=cred_id
    )
    
    choice = vault_interface.option_v_edit_handler(data=data)