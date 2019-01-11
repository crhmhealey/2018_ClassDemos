# https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html

import random
import matplotlib.pyplot as plt

results = []
for j in range(1000):
	total = 0
	for i in range(10):
		flip = random.randint(0,1)
		total += flip
	results.append(total)

display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]] += 1

plt.plot(display)
# plt.plot([0,1,2,3,4,5,6,7,8,9,10],display,'r^') #r^ r-- rs
# plt.bar([0,1,2,3,4,5,6,7,8,9,10], display)
# plt.bar([0,1,2,3,4,5,6,7,8,9,10], display, color=(.5, 0., .5, 1.0))
plt.ylabel("Number of Trials")
plt.xlabel("Number of Heads")
plt.show()

# print(*display)

