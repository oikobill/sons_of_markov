import numpy as np
import nltk
import re


class Book:
	def __init__(self, _author, _title, _text):
		self.author = _author
		self.title = _title
		self.text = _text

	def get_author(self):
		return self.author

	def get_title(self):
		return self.title

	def get_text(self):
		return self.text

class Parser():

	def __init__(self):
		self.works = {}

	def read_file(self, filename):
		f = open(filename,"r")
		text = f.read()
		author = self._find_author(text)
		title = self._find_title(text)

		self.works[author + "/" + title] = Book(author, title, text)

	#### Helper Functions 
	def _find_author(self, text):
		result = re.search('Author:  *.*', text).group(0)
		return result.strip()[7:].strip()

	def _find_title(self, text):
		result = re.search('Title:  *.*', text).group(0)
		return result.strip()[7:].strip()

	######

	def get_works(self):
		return self.works

	def remove_punctuation(self, text):
		exclude = set(string.punctuation)
		new_txt = ''.join(ch for ch in text if ch not in exclude)
		
	def to_lowercase(self, text):
		return text.lower()

	def process(self):
		txt = self.to_lowercase(self.text)
		txt = self.remove_punctuation(txt)


parser = Parser()
parser.read_file("../data/darwin/2355-0.txt")
works = parser.get_works()
print(works['Charles Darwin/The Formation of Vegetable Mould'].get_title())

