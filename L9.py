#Robert Schreibman
#csci250 - Sensors
#2-15-18
#L9

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=",")
#print(data[1])

x = data[0]
y = data[1]

plt.plot([1,2,3],[1,2,3])
#plt.show()