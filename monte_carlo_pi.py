import random 
circle = 0

i=1

trials = 10000

for i in range(trials):
	x = random.uniform(-1,1)
	y = random.uniform(-1,1)
	if (x**2 + y**2 <= 1):
		circle += 1

pi = 4*circle/float(trials)
print(pi)


