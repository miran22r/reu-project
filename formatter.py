from nltk.corpus import stopwords
from pygeocoder import Geocoder
import numpy as np
from reader import *

class formatter:
	
	def __init__(self):
		self.read = reader()
		self.fileName = open('bkw.txt', mode = 'r')
		self.fileName = iter(self.fileName)
		self.newFile = open('burgerking1.txt', mode = 'a')

	def format_tweets(self):
		for line in self.fileName:
			line = line.lower()
			if "***" in line:
				self.newFile.write(line)
				line = next(self.fileName)
				try:
					self.newFile.write(str(Geocoder.geocode(line)))
					self.newFile.write("\n")
				except: 
					self.newFile.write("none")
					self.newFile.write("\n")
				if "###" in line:
					for word in line.split():
						read.get_scores(word)
					self.newFile.write(str(self.read.get_total_sent()))
					self.newFile.write("\n")
					self.read.reset()
