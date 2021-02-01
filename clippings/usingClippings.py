import re
import os 
import shutil

LOCATION_OF_CLIPPINGS = "Clippings.txt"
BOOK_AUTHOR = {}

def createFolder():
    if os.path.exists('clippings'):
        shutil.rmtree('clippings')
    os.mkdir("clippings")

def getLocation(text):
    splitText = text.split()
    locationIndex = splitText.index("Location")
    return splitText[locationIndex + 1]

# Should be of the form otherwise there will be problems
# Sapiens: A Brief History of Humankind (Yuval Noah Harari)
def getAuthorAndTitle(text):
    splitText = re.split('\((.*)\)', text)
    title = splitText[0].strip()
    author = splitText[1]
    return title, author

def createFile(title):
    file = open("clippings/{}.txt".format(title), "a")
    file.close()

createFolder()
file = open(LOCATION_OF_CLIPPINGS, "r")
allLines = file.readlines()
for i in range(0,len(allLines),5):
    title, author = getAuthorAndTitle(allLines[i].strip())
    if title not in BOOK_AUTHOR.keys():
        BOOK_AUTHOR[title] = author
        createFile(title)
    
    location = getLocation(allLines[i+1].strip())
    file = open("clippings/{}.txt".format(title), "a")
    file.write(allLines[i+3].strip() + ":loco:{}".format(location)+'\n')
    file.close()

# getting the values from the dictionary
# print(BOOK_AUTHOR['\ufeffAtomic Habits: Tiny Changes, Remarkable Results'])
# this type of iteration is fine for accessing the files
# for key, value in BOOK_AUTHOR.items():
#     file = open("clippings/{}.txt".format(key), "r")
#     allLines = file.readlines()
#     for i in allLines:
#         print(i)
