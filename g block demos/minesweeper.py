import sys
import random

# add 1 around bomb location
def increase_around_bombs(r,c,board):
	for y in range(r-1, r+2):
		for x in range(c-1, c+2):
			if (board[y][x] is not "*"):
				board[y][x] += 1

# adding mines. Picks random box at x, y, then assigns a bomb to it.
# also adjusts counts around the edges 
def add_mines(board):
	for i in range(mines):
		x = random.randint(1,height-2)
		y = random.randint(1,width-2)
		while board[x][y] == '*':
			x = random.randint(1,height-2)
			y = random.randint(1,width-2)
		board[x][y] = '*'
		increase_around_bombs(x,y,board)

# prints board without surrounding extras
def print_board(board):
	for i in board[1:-1]:
		print(*i[1:-1])

# command line info
# +2 to make minesweeper "buffer"
# board larger than actually appears
height = int(sys.argv[1]) + 2
width = int(sys.argv[2]) + 2
mines = int(sys.argv[3])

# create an empty board
solution = [[0]*width for i in range(height)]

add_mines(solution)
print_board(solution)