"""
1. Data that needs to go to handler is: service, username, comment
- Need function to get the data out of the database.
- vault_logic need to call this function before the cli is called.

2. Logic for the interface need to get here.

3. "e" is pressed, function x is called to call the interface with the data.
- choice returns, based up on this choice the function calles another function
to handel the request further.
"""
import src.interface.vault_interface as vault_interface
import src.storage_logic as storage_logic
def main():
    data = 
    vault_interface.option_v_edit_handler(data=data)