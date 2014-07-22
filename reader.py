import sys

class reader:

	def __init__(self):
		self.file1 = 'SentiWordNet.txt'
		self.pos = 0
		self.neg = 0
		self.counter = 0
		self.pos_words = []
		self.neg_words = []

	def split_line(self, line):
		cols = line.split("\t")
		return cols

	def get_positive(self, cols):
		return cols[2]
 
	def get_negative(self, cols):
		return cols[3]

	def get_total_sent(self):
		return sum(self.pos_words) - sum(self.neg_words)
	
	def reset(self):
		self.pos_words = []
		self.neg_words = []

	def get_scores(self, word):
		self.fileName = open(self.file1)
		for line in self.fileName:
			cols = self.split_line(line)	
			words = cols[4].split("#")
			if word in words:
				self.pos = self.pos + float(self.get_positive(cols))
				self.neg = self.neg + float(self.get_negative(cols))
				self.counter = self.counter +1
		if self.counter is not 0:
			self.pos_words.append(self.pos/self.counter)
			self.neg_words.append(self.neg/self.counter)
			self.counter = 0
			self.pos = 0
			self.neg = 0
