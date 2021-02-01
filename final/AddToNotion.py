from notion.client import NotionClient

# TODO Iterate through the folder and check if present in the notion database


class AddToNotion():
    def __init__(self, token_v2, database_url, BOOK_AND_AUTHOR):
        self.database_url = database_url
        self.client = NotionClient(token_v2=token_v2)
        self.BOOK_AND_AUTHOR = BOOK_AND_AUTHOR

    


    