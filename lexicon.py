import numpy as np
from reader import *
import matplotlib.pyplot as plt

class lexicon:

	def __init__(self):
		self.read = reader()
		f = open('test.txt', mode = 'r')
		self.files = f.readlines()
		self.words = []
		self.dates = []
	
	def find_sentiment(self):
		for line in self.files:
			line = line.lower()
			self.words = line.split()
			if self.words:
				if "***" in self.words[0]:
					self.dates.append(self.words)
				if "###" in self.words[0]:
					for word in line.split():
						self.read.get_scores(word)
					print line
					print self.read.get_total_sent()
					print "============================="
				self.read.reset()
