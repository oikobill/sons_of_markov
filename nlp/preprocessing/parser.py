import numpy as np
import string, nltk, re, glob


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
		i = _text.rfind('***') # find last instance of  ***
		_text = _text[i:] # erase everything before that
		allowed = string.ascii_letters + " "
		new_txt = ''.join(ch for ch in _text if ch in allowed)
		self.text = new_txt.lower()

	def create_bigrams(self):
		self.bigram = list(nltk.bigrams(self.text.split()))

	def print_bigrams(self):
		print(*map(' '.join, self.bigram), sep=', ')

	def __init__(self, _text):

		self.set_author(_text)
		self.set_title(_text)
		self.set_text(_text)
		self.create_bigrams()

class Library(Book):

	def create_Book(self, filename):
		f = open(filename,"r")
		text = f.read()
		new_book = Book(text)
		self.works[new_book.author + "/" + new_book.title] = new_book

	def __init__(self):
		self.works = {}
		# self.create_Book("../data/test.txt")
		filename = glob.glob("../data/*") # import all files
		for file in filename:
			self.create_Book(file)


library = Library()
library.works['Nicolas Raga/Test'].print_bigrams()

