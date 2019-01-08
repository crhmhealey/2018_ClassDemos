# Monday Hall Simulation

import random as r

# No Switch
# a "1" in the list indicates the car!
# shuffle the boxes, have the player pick the first box always (randomizing this doesn't change the outcome)
# if the first box is the car, they win
# tally the number of wins and then divide by 1000 to get the percentage of wins
trials = 1000000

wins = 0
for x in range(trials):
	boxes = [1,0,0]
	r.shuffle(boxes)
	if boxes[0] == 1:
		wins += 1

print("No switching:",wins/trials)

# Switch
# a "1" in the list indicates the car!
# shuffle the boxes, have the player pick the first box always (randomizing this doesn't change the outcome)
# if the second box is a 0, "reveal" it and have the player choose the 3rd box
# if the 3rd box is the car, they win
# if the second box is the car, then "reveal" the third box, and have the player switch to pick the 2nd box, winning
wins = 0
for x in range(trials):
	boxes = [1,0,0]
	r.shuffle(boxes)
	if boxes[1] == 0:
		if boxes[2] == 1:
			wins += 1
	else:
		wins += 1

print("Switching:",wins/trials)

# it is better to always switch; you are 2x as likely to win the car if you do!
# all possible outcomes:
#
# Door 1        Door 2        Door 3       Result if Stay #1         Result if Switch
# Car           Goat          Goat         Car                       Goat
# Goat          Car           Goat         Goat                      Car
# Goat          Goat          Car          Goat                      Car
# 
# Winning 2/3 of the time with a switch vs. winning 1/3 of the time if staying is reflected in the outcome of the simulations.
