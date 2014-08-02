from pygeocoder import Geocoder
import numpy as np
from reader import *
from geo import *
import os

class formatter:
	
	def __init__(self):
		self.counter = 0
		self.locations = []
		self.times = []
		self.scores = []
		self.locate = geo()
	#	self.locate.load_file()
		self.read = reader()
		self.fileName = open('sbux.txt', mode = 'r')
		self.fileName = iter(self.fileName)
		self.newFile = open('starbucks.txt', mode = 'a')

	def format_tweets(self):
		for line in self.fileName:
			self.newFile = open('starbucks.txt', mode = 'a')
			line = line.lower()
			if "***" in line:
				line2 = next(self.fileName)
				if 'None' not in self.locate.coordinates(line2):
					try:
						self.newFile.write(line)
						self.newFile.write(str(self.locate.coordinates(line2)))
						self.newFile.write("\n")
						line = next(self.fileName)
					except Exception, e:
						print type(e)
						print str(e)


				if "###" in line:
					for word in line.split():
						self.read.get_scores(word)	
					self.newFile.write(str(self.read.get_total_sent()))
					self.newFile.write("\n")
					self.counter = self.counter +1
					print self.counter
					self.read.reset()
			self.newFile.close()
