import re
import os 
import shutil

class MakeClippings():
    def __init__(self, clippingsFile):
        self.clippingsFile = clippingsFile
        self.BOOK_AND_AUTHOR = {}
    
    def _createFolder(self):
        if os.path.exists('clippings'):
            shutil.rmtree('clippings')
        os.mkdir("clippings")
    
    def _getLocation(self, text):
        splitText = text.split()
        locationIndex = splitText.index("Location")
        return splitText[locationIndex + 1]

    def _getAuthorAndTitle(self, text):
        """
        Should be of the form given below otherwise there will be problems
        Sapiens: A Brief History of Humankind (Yuval Noah Harari)
        """
        splitText = re.split('\((.*)\)', text)
        title = splitText[0].strip()
        author = splitText[1]
        return title, author

    def _createFile(self, title):
        file = open("clippings/{}.txt".format(title), "a")
        file.close()

    def makeSeparateFiles(self):
        self._createFolder()
        file = open(self.clippingsFile, "r")
        allLines = file.readlines()
        for i in range(0,len(allLines),5):
            title, author = self._getAuthorAndTitle(allLines[i].strip())
            if title not in self.BOOK_AND_AUTHOR.keys():
                self.BOOK_AND_AUTHOR[title] = author
                self._createFile(title)
            
            location = self._getLocation(allLines[i+1].strip())
            file = open("clippings/{}.txt".format(title), "a")
            file.write(allLines[i+3].strip() + ":loco:{}".format(location)+'\n')
            file.close()
