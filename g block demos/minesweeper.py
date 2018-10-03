import sys
import random

# add 1 around bomb location
def increase_around_bombs(r,c):
	for y in range(r-1, r+2):
		for x in range(c-1, c+2):
			if (board[y][x] is not "*"):
				board[y][x] += 1

# command line info
# +2 to make minesweeper "buffer"
# board larger than actually appears
height = int(sys.argv[1]) + 2
width = int(sys.argv[2]) + 2
mines = int(sys.argv[3])

# create an empty board
board = [[0]*width for i in range(height)]

# adding mines. Picks random box at x, y, then assigns a bomb to it.
# also adjusts counts around the edges 
for i in range(mines):
	x = random.randint(1,height-2)
	y = random.randint(1,width-2)
	while board[x][y] == '*':
		x = random.randint(1,height-2)
		y = random.randint(1,width-2)
	board[x][y] = '*'
	increase_around_bombs(x,y)

# creates board without surrounding extras
for i in range (1,len(board)-1):
	for j in range(1,len(board[0])-1):
		print(board[i][j],end=" ")
	print("")

# alternative print
# for i in board[1:len(board)-1]:
# 	for j in i[1:len(i)-1]:
# 		print(j,end=" ")
# 	print("")

