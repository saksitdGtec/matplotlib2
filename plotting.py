import matplotlib.pyplot as plt
import numpy as np

xpt = np.array([1,3])
ypt = np.array([3,10])
plt.plot(xpt,ypt,"o")  # plotting with out line  "o = ring"
plt.show()



xpt = np.array([1,2,6,8])
ypt = np.array([3,8,1,10])
plt.plot(xpt,ypt,"o")  # plotting with out line  "o = ring"
plt.show()



ypt = np.array([3,8,1,10,5,7])
plt.plot(ypt)  # plotting xpt default = [0,1,2,3,4,5]
plt.show()