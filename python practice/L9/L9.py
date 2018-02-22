#Robert Schreibman
#csci250 - Sensors
#2-15-18
#L9

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=",")

x = data[0] #time
y = data[1] #cheese

plt.plot(x,y,'rp')
plt.xlabel("Time (years)")
plt.ylabel("Cheese Consumption (lbs)")
plt.title("Cheese Consumption in the Last Decade")

plt.savefig('plot.jpg')

plt.show()

d = {}
for key, value in zip(y,x):
    d[key] = value

print(d)

for cheese in sorted(d, reverse=True):
    print("In {}, {} lbs of cheese was consumed!".format(d[cheese],cheese))
