from MakeClippings import MakeClippings
from AddToNotion import AddToNotion

makeClippings = MakeClippings("Clippings.txt")
makeClippings.makeSeparateFiles()

token_v2 = ""
database_url = ""
BOOK_AND_AUTHOR = makeClippings.BOOK_AND_AUTHOR

addToNotion = AddToNotion(token_v2 = token_v2,database_url = database_url, BOOK_AND_AUTHOR = BOOK_AND_AUTHOR)
