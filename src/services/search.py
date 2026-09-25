from src.interface.search_interface import screen_handler
from src.services.pagination import Pagination

def search_main(total_cred: int, data: list):
    pag = Pagination(total_cred=total_cred)
    
    screen_handler(
        data=data,
        total_credentials=total_cred,
        current_page=pag.current_page,
        max_page=pag.total_pages,
        showing_items_start=pag.showing_items_start,
        showing_items_end=pag.showing_items_end
    )