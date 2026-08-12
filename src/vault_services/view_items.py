import src.storage as storage

def get_view_screen_data(userid: int, page_size: int, offset: int) -> list[tuple]:

    rows = storage.Search_data.search_for_view_items(
        userid=userid,
        limit=page_size,
        offset=offset,
        database="CLI_Data.db"
    )

    return rows


def view_password(userid: int, encryption_key: bytes, choice: int):
    pass