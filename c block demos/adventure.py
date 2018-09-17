def start():
    response = input("\n\n\n\n\n\nGreetings! \n\nYou are looking for treasure. Your map says that the treasure can be found northerly. However, your friend says he heard someone talking about treasure in the south. \n\nDo you 1) Trust your Friend, or 2) Trust the Map? ")
    if response == "1":
    	friend()
    elif response == '2':
    	map()
    else:
    	print("You must type 1 or 2. Please try again.")
    	start()

def map():
	print("You lost.")
	response = (input("Do you want to play again?")).lower()
	if response == "yes" or response == "y":
		start()
	else:
		exit() # quits program

def friend():
	pass

start()