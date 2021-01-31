# A "collection" corresponds to what's sometimes called a "database" in the Notion UI.

from notion.client import NotionClient
from notion.block import TextBlock

token = "74ddb064bc49e9644ab1b0e5463579593de96e39a573ec0f919efb634ac295d712dc94f272d374125b2330b8814cd723c91782bb80cf1363314828100fc026696bf48c30eb97410e38998373281f"
database_url = "https://www.notion.so/ed3d22c6dea249f8afe0dcef1caa062d?v=31166c255e354980927bc1f9345164b1"

client = NotionClient(token_v2=token)

# enter the url of the database it can also be an id
cv = client.get_collection_view(database_url)
# some other functions not that useful though
# print(cv.parent)
# print(cv.parent.views)

# -------------- get all the rows in a database -------------- #
# allRows = cv.collection.get_rows()
# print(allRows)
# You will see that rows are also blocks then the same functions can be used on them as we did in blocks that we got using get_block
# Also a row only becomes a page when you add blocks in it


# -------------- Add a new record -------------- #
# These fields must already be present
# row = cv.collection.add_row()
# row.name = "Just some data"
# row.is_confirmed = True
# row.estimated_value = 399
# row.files = ["https://www.birdlife.org/sites/default/files/styles/1600/public/slide.jpg"]
# row.person = client.current_user
# row.tags = ["A", "C"]
# row.where_to = "https://learningequality.org"

# -------------- adding text to a page in a database -------------- #
# for row in cv.collection.get_rows():
#     if (row.name == "something else"):
#         row.children.add_new(
#             TextBlock, title="added to a page from a database using row")

# -------------- Deleting a row in a database -------------- #
# for row in cv.collection.get_rows():
#     if (row.name == "remove"):
#         row.remove()

# -------------- Changing property of a table and getting other values -------------- #
# for row in cv.collection.get_rows():
#     if (row.name == "something else"):
#         print(row.is_confirmed)
#         row.estimated_value = 57
