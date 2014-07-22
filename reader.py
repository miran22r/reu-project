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

	def get_pos(self):
		return self.pos

	def get_neg(self):
		return self.neg
 
	def get_scores(self, word):
		self.fileName = open(self.file1)
		for line in self.fileName:
			if not line.startswith("#"):
				cols = self.split_line(line)	
				words = cols[4].split("#")
				if word in words:
					self.pos = self.pos + float(self.get_positive(cols))
					self.neg = self.neg + float(self.get_negative(cols))
					self.counter = self.counter +1
		if self.counter is not 0:
			print word
			print self.counter
			print self.pos/self.counter
			print self.neg/self.counter
			self.counter = 0
			self.pos = 0
			self.neg = 0
