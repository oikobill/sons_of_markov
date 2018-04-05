import numpy as np
import nltk

def read_file(filename):
	f = open(filename,"r")
	raw_txt = f.read()
	return raw_txt