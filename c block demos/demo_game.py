def lake(): 
	choice = input('You are sitting on the lake, enjoying your picnic, when the water starts stirring and bubbling. Do you run [r] to the mountains for safety, or stand [s] your ground and prepare to fight? ')
	if check(choice,'r','s') == 'r':
		print('You decide to flee to the mountain for safety. ')
		mountain()
	else:
		stand()

def stand():
	print('That was stupid. How are you going to fend off a sea monster with some apple juice and a baguette? You die. ')
	again()

def mountain():
	print('You sit on top of the mountaintop and enjoy the sunshine and your delicious juice and baguette. What a lovely picnic! ')
	again()

def start():
	choice = input('You are going on a picnic. Do you want to picnic at a lake [l] or on a mountaintop [m]? ')
	if check(choice,'l','m') == 'l':
		lake()
	else: 
		mountain()

def again():
	choice = input('Would you like to play again? [y] or [n] ')
	if check(choice,'y','n') == 'y':
		start()
	else:
		print('Goodbye.')

def check(choice,a,b):
	while choice!=a and choice!=b:
		choice = input('Please choose '+a+' or '+b+': ')
	return choice

start()
