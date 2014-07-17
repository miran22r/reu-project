from sentiwordnet import SentiWordNetCorpusReader, SentiSynset
from nltk.corpus import stopwords
import numpy as np

class lexicon:

	def __init__(self):
		self.swn_filename = 'SentiWordNet.txt'
		self.swn = SentiWordNetCorpusReader(self.swn_filename)
		self.cachedStopWords = stopwords.words("english")
		self.pos_sentiment = 0
		self.neg_sentiment = 0
		self.words = []
		self.tweets = []

	def load_files(self, inputFile):
		f = open('example.txt', mode = 'r')
		self.files = f.readlines()
		self.tweets = self.files
		for line in self.files:
			line = line.lower()
			line = line.translate(None, '.')
			line = line.translate(None, ',')
			line = line.translate(None, '__')
			line = line.translate(None, ':')
			line = line.split()
			self.words.extend(line)
			
	def find_sentiment(self):
		self.cachedStopWords = stopwords.words("english")
		pos_value = 0
		neg_value = 0
		for word in self.words:
			if self.swn.senti_synsets(word):
				if word not in self.cachedStopWords:
					word1 = self.swn.senti_synsets(word)[0]
					self.pos_sentiment = self.pos_sentiment + word1.pos_score
					self.neg_sentiment = self.neg_sentiment + word1.neg_score
			
			print "pos " + str(self.pos_sentiment)
			print "neg " + str(self.neg_sentiment)
		if self.pos_sentiment > self.neg_sentiment:
			print "This tweet is pos: " + str(self.pos_sentiment)
		else:
			print "This tweet is neg: " + str(self.neg_sentiment)
