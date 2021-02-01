# This is all about different types of blocks and how you can use them
# Most data in Notion is stored as a "block" (including pages, and all the individual elements within a page).

from notion.block import TodoBlock, TextBlock, DividerBlock, PageBlock, TableOfContentsBlock
from notion.client import NotionClient

token = "74ddb064bc49e9644ab1b0e5463579593de96e39a573ec0f919efb634ac295d712dc94f272d374125b2330b8814cd723c91782bb80cf1363314828100fc026696bf48c30eb97410e38998373281f"
normal_page_url = "https://www.notion.so/The-title-has-now-changed-and-has-live-updated-in-the-browser-d3ff3ac38f8b4a94bb911c3dc7688f6e"

client = NotionClient(token_v2=token)

# -------------- using get_block -------------- #
# get block accepts either an url or the id of that block
page = client.get_block(normal_page_url)
# this may not be a page can be textblock
# for child in page.children:
#     if (child._type == 'text'):
#         text_blocks = client.get_block(child.id)
#         print(text_blocks)

# -------------- locking and unlocking a page -------------- #
# page.locked = True

# -------------- using remove method -------------- #
# this will also work on all the blocks
# page.remove()

# since page is block we can get its type and this will work on all other blocks
# print(page._type)
# so what this code is doing is iterating through all the elements of the page block and getting their types
# if the type is divider then I remove it
# for child in page.children:
#     if (child._type == 'divider'):
#         child.remove()

# -------------- adding something to a page -------------- #
# it will always be appended at the end of the list
# when you create a new block it returns an instance which can then be used to access its functions like we do in the todo component
# page.children.add_new(TextBlock, title="Something to get done")
# new_element = page.children.add_new(TodoBlock, title="Something to get done")
# new_element.checked = True

# -------------- to get all the contents of single page -------------- #
# this wont work for database urls
# for child in page.children:
#     print(child)

# -------------- using the divider block -------------- #
# page.children.add_new(DividerBlock)

# other common blocks and their properties are present in block.py from line 482
# all blocks that inherit BasicBlock expect title

# -------------- creating a page and setting its title, cover page and icon -------------- #
# page_block = page.children.add_new(PageBlock, title="this is a new page")
# page_block.icon = "https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80"
# page_block.cover = "https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80"

# -------------- going to a page inside a page and writing something in it -------------- #
# for child in page.children:
#     if(child._type == 'page'):
#         child.children.add_new(
#             TextBlock, title="This was the text added to see page inside a page")

# another way of adding a some content is
# for child in page.children:
#     if(child._type == 'page'):
#         subpage = client.get_block(child.id)
#         subpage.children.add_new(
#             TextBlock, title="This was the text added to see page inside a page using get_block method")

# similarly listing the contents of the page inside it
# for child in page.children:
#     if(child._type == 'page'):
#         for subchild in child.children:
#             print(subchild)

# -------------- adding table of contents -------------- #
# for this some modificaions have to be made
# page.children.add_new(TableOfContentsBlock)

""" 
Block methods discovered till now
_type 
remove 
children -> iterated to get the blocks in that page -> add_new -> to add a new block
move_to -> to move the blocks 
remove
"""
