import numpy as np
import nltk
import re


class Parser:

	def __init__(self):
		self.works = {}

	def read_file(self, filename):
		f = open(filename,"r")
		text = f.read()
		author = find_author(text)
		title = find_author(text)
		self.works[author + "/" + title] = text

	def find_author(self, text):	
		result = re.search('Author:  *.*', text).group(0)
		return result.strip()[7:].strip()

	def find_title(self, text):
		result = re.search('Title:  *.*', text).group(0)
		return result.strip()[7:].strip()

	def print_works(self):
		print(self.works)


parser = Parser()
parser.read_file("../data/example_project_gutenberg.txt")
parser.print_works()

