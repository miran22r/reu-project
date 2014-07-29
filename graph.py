import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.axis as axs

locations = []
scores = []
time = []
fileName = open('burgerking.txt', mode = 'r')

# opening up file to be read; this should be tweets

for line in fileName:
	if "***" in line:
	#	if the *** found, go to next line; the *** is the timestamps
		line2 = next(fileName)
		if "nigga" not in line2:
			locations.append(line2)
		# 	the location is found on line after the time stamp
			line2 = next(fileName)	
			line = line.translate(None, "*")
			line = line.split()
			del(line[4])
			hours = line[3].split(':')
			if int(hours[0]) > 8:
				if int(hours[0]) < 13:
					line = " ".join(line)
					time.append(datetime.strptime(line, "%a %b %d %H:%M:%S %Y"))
			# taking time stamp of tweets between specified hours; checking hours to see if they fall within specified range	
					scores.append(line2)
			# scores are found in line after location; only taking scores between designated hours
plt.plot(time, scores, 'r-')
plt.show()
