from nltk.corpus import stopwords
import numpy as np
from reader import *
import matplotlib.pyplot as plt

class lexicon:

	def __init__(self):
		self.graph = dict()
		self.graph = { '01': [], '02': [], '03': [],'04': [],'05': [],'06': [],'07': [],'08': [],'09': [],'10': [],'11': [],'12': [],'13': [],'14': [],'15': [],'16': [],'17': [],'18': [],'19': [],'20': [],'21': [],'22': [],'23': [],'24': [],'25': [],'26': [],'27': [],'28': [],'29': [],'30': []}
		self.read = reader()
		f = open('sample.txt', mode = 'r')
		self.files = f.readlines()
		self.words = []
		self.days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
		self.values = []
	
	def find_sentiment(self):
		index = 0
		for line in self.files:
			index = index+1
			line = line.lower()
			line = line.translate(None, ',')
			line = line.translate(None, '.')
			line = line.translate(None, '!')
			line = line.translate(None, '"')
			self.words = line.split()
			if self.words:
				if self.words[0] in self.days:
					if 'jun' in self.words[1] and '2014' in self.words[5]:
						line = self.files[index + 1]
						for word in self.words:
							self.read.get_scores(word)
							self.graph[self.words[2]].append(float(self.read.get_total_sent()))
						self.read.reset()
		for x in self.graph:
			print x
			print len(self.graph[x])
			self.values.append(np.mean(self.graph[x]))
		myList = []
		myList = list(xrange(31))
		del(myList[0])
		plt.plot(myList, self.values)
		plt.ylabel('Twitter Sentiment for Mcdonalds during June 2014')
		plt.show()
