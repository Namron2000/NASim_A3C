
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from scipy.signal import savgol_filter
filepath = "./results/trained on 2 envs not det/scores.txt"

#this is literally not necessary but np > python
file = open(filepath, 'r')
#skip headers
file.readline()
data = np.loadtxt(file)
file.close()
xt = data[:,0]
median = data[:,4]
min = data[:,7]
max = data[:,6]
"""
#code to make different smooth lines from median to see difference in different window sizes
ypreds = []
for i in range(21,202,50):
    ypreds.append(savgol_filter(median, i, 3))
"""
"""
#code to visualize those different smooth lines (one window per view)
for i,ypred in enumerate(ypreds):
    f = plt.figure(figsize=(10,5))
    plt.plot(xt, data[:,4])
    #plt.plot(xt, data[:,6])
    #plt.plot(xt, data[:,7])
    plt.plot(xt,ypred)
plt.show()
"""
#1001 is an arbitrary number. The higher it is the smoother the curve. Also it must be odd.
smooth_median = savgol_filter(median, 1001, 3)
smooth_min = savgol_filter(min, 1001, 3)
smooth_max = savgol_filter(max, 1001, 3)

plt.plot(xt, smooth_median,label = "median", color='r')
plt.plot(xt, smooth_min,label = "min", color='g')
plt.plot(xt, smooth_max,label = "max", color='b')
plt.fill_between(xt, smooth_min, smooth_max, alpha=.1, color='r')
plt.grid(True)
plt.ylabel("reward")
plt.xlabel("steps")
plt.title("Training")
plt.legend()
plt.show()