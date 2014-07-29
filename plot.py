import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.axis as axs

locations = []
scores = []
time = []
fileName = open('stock.txt', mode = 'r')

# 	opening the file that has stocks in it; should be in "Time, Price" format
for line in fileName:
			line = line.split()
			time.append(datetime.strptime(line[0], "%H:%M,"))
			scores.append(line[1])
#	taking the hours and minutes of the stocks

plt.plot(time, scores, 'b-')
dateFmt = mpl.dates.DateFormatter('%H:%M')
axs = plt.gca()
axs.xaxis.set_major_formatter(dateFmt)
#	formatting text in the hour:minute format
plt.show()
