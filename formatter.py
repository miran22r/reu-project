from pygeocoder import Geocoder
import numpy as np
from reader import *
from geo import *
import os

class formatter:
	
	def __init__(self):
		self.locations = []
		self.times = []
		self.scores = []
		self.locate = geo()
		self.read = reader()
		self.fileName = open('sbux.txt', mode = 'r')
		self.fileName = iter(self.fileName)
		self.newFile = open('starbucks.txt', mode = 'a')

	def format_tweets(self):
		for line in self.fileName:
			line = line.lower()
			if "***" in line:
				line2 = next(self.fileName)
			#	print "word being passed in " + str(line2)
			#	print self.locate.coordinates(line2)
				if 'None' not in self.locate.coordinates(line2):
			#		print line
					self.times.append(line)
					self.locations.append(str(self.locate.coordinates(line2)))
					line = next(self.fileName)
				if "###" in line:
					for word in line.split():
						self.read.get_scores(word)
					self.scores.append(str(self.read.get_total_sent()))
					self.read.reset()
		for x, y, z in zip(self.scores, self.locations, self.times):
			self.newFile.write(x)
			self.newFile.write(y)
			self.newFile.write(z)
		self.newFile.write(self.scores)
		self.newFile.write(self.locations)
		self.newFile.write(self.times)
