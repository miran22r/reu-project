import matplotlib as mpl
import matplotlib.dates as mdates
import matplotlib.axis as axs
import matplotlib.pyplot as plt
from datetime import datetime
from geo import *
import itertools

class plot:
	
	def __init__(self):
		self.cities = {}
		self.scores1 = ""
		self.time1 = ""
		self.scores2 = []
		self.time2 = []
		self.file1 = open('burgerking.txt', mode = 'r')
		self.file2 = open('stock.txt', mode = 'r')
	
	def graph_sentiment(self, scores, locations, times):
		for x in times:
			x = x.translate(None, "*")
			x = x.split()
			del(x[4])
			hours = x[3].split(':')
			if (int(hours[0]) <= 16 and int(hours[1]) <=30) and (int(hours[0]) >= 9 and int(hours[1]) <30):	
				self.time1 = datetime.strptime(x[3], "%H:%M:%S")
				self.scores1 = score
				if location  in self.cities:
					self.cities[location][0].append(self.scores1)
					self.cities[location][1].append(self.time1)
				else:
					self.cities[location] = [[],[]]
					self.cities[location][0].append(self.scores1)
					self.cities[location][1].append(self.time1)

	def graph_sentiment(self):
		for line in self.file1:
			if "***" in line:
				location = next(self.file1)
				score = next(self.file1)	
				line = line.translate(None, "*")
				line = line.split()
				del(line[4])
				if "25" in line[2]:
					hours = line[3].split(':')
					if int(hours[0]) <= 17 and int(hours[0]) >= 8:
						self.time1 = datetime.strptime(line[3], "%H:%M:%S")
						self.scores1 = score
						if location  in self.cities:
							self.cities[location][0].append(self.scores1)
							self.cities[location][1].append(self.time1)
						else:
							self.cities[location] = [[],[]]
							self.cities[location][0].append(self.scores1)
							self.cities[location][1].append(self.time1)

	def graph_stock(self):
		for line in self.file2:
			line = line.split()
			self.time2.append(datetime.strptime(line[0], "%H:%M,"))
			self.scores2.append(line[1])

	def graph(self):
		fig, axes = plt.subplots(nrows=2)
		colors = ['ro', 'bo', 'go', 'co', 'mo', 'ko', 'yo']
		for key, x in zip(self.cities, itertools.cycle(colors)):
			axes[0].plot(self.cities[key][1], self.cities[key][0], x) 
		axes[1].plot(self.time2, self.scores2, 'r-')
		dateFmt = mpl.dates.DateFormatter('%H:%M')
		axs = plt.gca()
		axs.xaxis.set_major_formatter(dateFmt)
		plt.show()
