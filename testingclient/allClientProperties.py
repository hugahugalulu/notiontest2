from notion.client import NotionClient

token = "74ddb064bc49e9644ab1b0e5463579593de96e39a573ec0f919efb634ac295d712dc94f272d374125b2330b8814cd723c91782bb80cf1363314828100fc026696bf48c30eb97410e38998373281f"

# initializing a notion client
client = NotionClient(token_v2=token)

# -------------- get the email and id of the client ------------------ #
# email = list(client.get_email_uid().keys())[0]
# user_id = client.get_email_uid()[email]
# print(client.get_user(user_id))

# -------------- get all the top level pages ------------------ #
# for i in client.get_top_level_pages():
#     print(i)
