
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

filepath = "./results/20211210T045454.583853/scores.txt"
steps = []
min = []
max = []
median = []

with open(filepath, 'r') as f:
    next(f)
    for line in f:
        values = line.split()
        steps.append(values[0])
        min.append(values[7])
        max.append(values[6])
        median.append(values[4])



X_Y_Spline = make_interp_spline(steps, min)

steps_new = np.linspace(0,1000000,500)
min_s = X_Y_Spline(steps_new)
#max_s = interp1d(steps,max,steps_new)
#median_s = interp1d(steps,median,steps_new)

"""
min_s = min.ewm(alpha=(1-0.85)).mean()
max_s = max.ewm(alpha=(1-0.85)).mean()
median_s = median.ewm(alpha=(1-0.85)).mean()
"""

plt.plot(steps, min_s, color='g', label='min')
plt.plot(steps, min, color='g',alpha=.2)

#plt.plot(steps, max_s, color='b', label='max')
#plt.plot(steps, max, color='b',alpha=.2)

#plt.plot(steps, median, color='r',alpha=.2)
#plt.plot(steps, median_s, color='r', label='median')


ax = plt.gca()
ax.axes.xaxis.set_ticks([50,100,150,200,250,300])
ax.axes.yaxis.set_ticks([50,100,150,200,250,300])
plt.grid(True)
plt.ylabel("reward")
plt.xlabel("steps")
plt.title("Training")
plt.legend()
plt.show()
