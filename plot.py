import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.axis as axs
from geo import *

class plot:
	
	def __init__(self):
		self.locate = geo()
		self.locations = {}
		self.scores1 = []
		self.time1 = []
		self.scores2 = []
		self.time2 = []
		self.file1 = open('burgerking.txt', mode = 'r')
		self.file2 = open('stock.txt', mode = 'r')
	
	def graph_sentiment(self):
		for line in self.file1:
			if "***" in line:
				line2 = next(self.file1)
				self.locate.coordinates(line2)
			#	self.locations.append(line2)
				line2 = next(self.file1)	
				line = line.translate(None, "*")
				line = line.split()
				del(line[4])
				if "25" in line[2]:
					hours = line[3].split(':')
					if int(hours[0]) <= 12 and int(hours[0]) >= 8:
						self.time1.append(datetime.strptime(line[3], "%H:%M:%S"))
						self.scores1.append(line2)
	
	def graph_stock(self):
		for line in self.file2:
			line = line.split()
			self.time2.append(datetime.strptime(line[0], "%H:%M,"))
			self.scores2.append(line[1])

	def graph(self):
		fig, axes = plt.subplots(nrows=2)
		axes[0].plot(self.time1, self.scores1, 'b-')
		axes[1].plot(self.time2, self.scores2, 'r-')
		dateFmt = mpl.dates.DateFormatter('%H:%M')
		axs = plt.gca()
		axs.xaxis.set_major_formatter(dateFmt)
		plt.show()
