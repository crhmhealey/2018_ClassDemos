def start():
	result = input("\n\nYou are here to save the princess! \n\nShe has been kidnapped by Bowser and Bowser Jr. You are at a fork in the road, and you can either \n\n1) Go ahead and save the Princess or \n2) Turn back in shame and dishonor.\n\n>> ")
	if result == '1':
		savePrincess()
	elif result == '2':
		shame()
	else:
		print("I don't know what "+result+" means. Please type a 1 or a 2.")
		start()
	print("Hi!")

def savePrincess():
	pass

def shame():
	pass

start()