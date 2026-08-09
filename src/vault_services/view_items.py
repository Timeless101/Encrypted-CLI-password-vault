import src.storage as storage

def screen_logic(userid: int, page_size: int, offset: int) -> list[tuple]:

    rows = storage.Search_data.search_for_view_items(
        userid=userid,
        limit=page_size,
        offset=offset,
        database="CLI_Data.db"
    )

    return rows
