import src.storage as storage

def screen_logic(userid: int):

    rows = storage.Search_data.search_for_view_items(
        userid=userid,
        limit=5,
        offset=0,
        database="CLI_Data.db"
    )

    return rows
