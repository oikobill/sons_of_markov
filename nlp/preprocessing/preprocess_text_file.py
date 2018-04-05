import numpy as np
import nltk
import re
import string


class Parser:

	def __init__(self):
		self.text = None
		self.author = None
		self.title = None

	def read_file(self, filename):
		f = open(filename,"r")
		self.text = f.read()
		

	def find_author(self, text):	
		result = re.search('Author:  *.*', text).group(0)
		self.author = result.strip()[7:].strip()

	def find_title(self, text):
		result = re.search('Title:  *.*', text).group(0)
		self.title = result.strip()[7:].strip()

	def remove_punctuation(self, text):
		exclude = set(string.punctuation)
		new_txt = ''.join(ch for ch in s if ch not in exclude)


	def to_lowercase(self, text):
		return text.lower()

	def process(self):
		txt = self.to_lowercase(self.text)
		txt = self.remove_punctuation(txt)




parser = Parser()
parser.read_file("../data/darwin/2355-0.txt")
parser.process()
