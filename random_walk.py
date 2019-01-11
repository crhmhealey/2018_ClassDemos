import random as r

def take_walk(steps):
	x, y = 0, 0
	for i in range(steps):
		(dx,dy) = r.choice([(0,1),(0,-1),(1,0),(-1,0)])
		x += dx
		y += dy
	return (x,y)

for blocks in range(100):
	num_walks = 20000
	walk_home = 0
	for i in range(num_walks):
		(x,y) = take_walk(blocks)
		distance_from_home = abs(x)+abs(y)
		if distance_from_home <= 4:
			walk_home+=1
	if walk_home/float(num_walks) >= .5:
		print("Distance:",blocks,"| Walk home:",walk_home/num_walks)


