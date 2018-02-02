#Robert Schreibman
#CSCI250 - Sensors
#Date: 1/30/18
#Python Practice: L6

import numpy as n
import random as r


randomVal = r.uniform(1,100)
print("Random Value: ", randomVal)

arr = n.full((1,100),100)
print(arr)

arr2 = []

for i in range(100):
	arr2.append(round(r.uniform(1,100),2))

print(arr2)
for j in arr2:
	if arr2.index(j) % 2 == 0:
		print(j)


	





