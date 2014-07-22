from nltk.corpus import stopwords
import numpy as np
from reader import *

class lexicon:

	def __init__(self):
		self.read = reader()
		self.cachedStopWords = stopwords.words("english")
		f = open('example.txt', mode = 'r')
		self.files = f.readlines()
		self.words = []
		self.tweets = []
	
	def find_sentiment(self):
		for line in self.files:
			line = line.lower()
			line = line.translate(None, ',')
			line = line.translate(None, '.')
			line = line.translate(None, '!')
			line = line.translate(None, '"')
			self.words = line.split()
			for word in self.words:
			#	if word not in self.cachedStopWords:
				self.read.get_scores(word)
			print line
			print self.read.get_total_sent()
			self.read.reset()
			print "--------------------------"
