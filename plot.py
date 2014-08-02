import matplotlib as mpl
import matplotlib.dates as mdates
import matplotlib.axis as axs
import matplotlib.pyplot as plt
from datetime import datetime
from geo import *
import itertools
import heapq
import numpy as np

class plot:
	def __init__(self):
		self.score_length = {}
		self.cities = {}
		self.scores1 = ""
		self.time1 = {}
		self.scores2 = []
		self.time2 = []
		self.times = []
		self.time_scores = []
		self.file1 = open('starbucks.txt', mode = 'r')
		self.file2 = open('stock.txt', mode = 'r')

	def graph_sentiment(self):
		for line in self.file1:
			if "***" in line:
				location = next(self.file1)
				score = next(self.file1)	
				line = line.translate(None, "*")
				line = line.split()
				del(line[4])
				hours = line[3].split(':')	
				del(hours[2])
				hours = ":".join(hours) 
				self.scores1 = score
				if location in self.cities:
					self.cities[location][0].append(self.scores1)
					if hours in self.cities[location][1]:
						self.cities[location][1][hours].append(float(self.scores1))
					else:
						self.cities[location][1][hours] = []
						self.cities[location][1][hours].append(float(self.scores1))
				else:
					self.cities[location] = [[],{}, [], []]
					self.cities[location][0].append(self.scores1)
					if hours in self.cities[location][1]:
						self.cities[location][1][hours].append(float(self.scores1))
					else:
						self.cities[location][1][hours] = []
						self.cities[location][1][hours].append(float(self.scores1))

	def graph_stock(self):
		for line in self.file2:
			line = line.split()
			self.time2.append(datetime.strptime(line[0], "%H:%M,"))
			self.scores2.append(line[1])

	def graph(self):
		fig, axes = plt.subplots(nrows=6)
		for key in self.cities:
			self.score_length[key] = len(self.cities[key][0])	
		topCities = sorted(self.score_length, key=self.score_length.get, reverse=True)[:5]
		print topCities
		for x in topCities:
			print len(self.cities[x][0])	
		for location in self.cities:
			for hour in self.cities[location][1]:
				self.cities[location][2].append(datetime.strptime(hour, "%H:%M"))
				self.cities[location][3].append(np.mean(self.cities[location][1][hour]))
		self.times = sorted(self.times)
		colors = ['k-', 'b-', 'g-', 'c-', 'm-']
		for top, x, y in zip(topCities, itertools.cycle(colors), range(5)):
			axes[y].plot(sorted(self.cities[top][2]), self.cities[top][3], x)
		axes[5].plot(self.time2, self.scores2, 'r-')
		dateFmt = mpl.dates.DateFormatter('%H:%M')
		axs = plt.gca()
		axs.xaxis.set_major_formatter(dateFmt)
		plt.show()
