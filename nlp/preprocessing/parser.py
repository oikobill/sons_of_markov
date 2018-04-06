import numpy as np
import string, nltk, re, glob
import pandas as pd


class Book:

    def set_author(self, _text):
        try:
            _author = re.search('Author:  *.*', _text).group(0) #find author line
            self.author = _author.strip()[7:].strip()
        except:
            print('Could not find author \n')
            self.author = "None"

    def set_title(self, _text):
        try:
            _title = re.search('Title:  *.*', _text).group(0) #find title line
            self.title = _title.strip()[7:].strip()
        except:
            print('Could not find title \n')
            self.title = "None"

    def set_text(self, _text):

        # remove some crap from top and bottom
        signal1 = "*** START OF THIS PROJECT GUTENBERG EBOOK " + self.title.upper() + " ***"
        signal2 = "*** END OF THIS PROJECT GUTENBERG EBOOK " + self.title.upper() + " ***"

        start_index = _text.find(signal1)
        end_index = _text.find(signal2)
        _text = _text[start_index+len(signal1):end_index-len(signal2)]

        # replace new lines, tabs and all other crap with spaces
        _text = _text.replace("\n", " ").replace("-", " ").replace("--", " ")
        # removes multiple spaces
        _text = re.sub(' +',' ',_text)

        # remove all non-letter characters
        allowed = string.ascii_letters + " "
        new_txt = ''.join(ch for ch in _text if ch in allowed)
        self.text = new_txt.lower()

    def list_words(self):
        words = self.text.split(" ")
        while "" in words:
            words.remove("")
            
        while " " in words:
            words.remove(" ")

        self.word_list = words

    def count_words(self):
        self.list_words()

        s = pd.Series(self.word_list)
        return s.value_counts()


    def __init__(self, filename):
        # read the file
        f = open(filename,"r")
        text = f.read()
        self.set_title(text)
        self.set_author(text)
        self.set_text(text)

        

# class Library(Book):

#   def create_Book(self, filename):
#       f = open(filename,"r")
#       text = f.read()
#       new_book = Book(text)
#       self.works[new_book.author + "/" + new_book.title] = new_book

#   def __init__(self):
#       self.works = {}
#       # self.create_Book("../data/test.txt")
#       filename = glob.glob("../data/*") # import all files
#       for file in filename:
#           self.create_Book(file)


