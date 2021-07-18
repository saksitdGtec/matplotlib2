import matplotlib.pyplot as plt
import numpy as np

ypt = np.array([3,8,1,10])


# plt.plot(ypt,marker = 'o')
# plt.show()

# plt.plot(ypt,marker = 'X')    #mark X is filled
# plt.show()

# plt.plot(ypt, 'o:r', ms =5 )    #mark X is filled  o = ring , r =red  this parameter called FMT
# plt.show()

# plt.plot(ypt, marker='o', ms =5, mec = 'r' )    #mark X is filled  o = ring , r =red  this parameter called FMT
# plt.show()

# plt.plot(ypt, marker='o', ms =10, mfc = 'r' )    #mark X is filled  o = ring , r =red  this parameter called FMT
# plt.show()


# plt.plot(ypt, marker='o', ms =10, mfc = 'r', mec = 'r' )    #mark X is filled  o = ring , r =red  this parameter called FMT
# plt.show()


plt.plot(ypt, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')    #mark X is filled  o = ring , r =red  this parameter called FMT
plt.show()

plt.plot(ypt, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()