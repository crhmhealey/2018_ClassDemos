def start():
	choice = input("\n\n\n\n\n\nGreetings! \n\nYou are heading to the dining hall one day when there's a bear walking with a dinosaur on campus!! Do you \n\n1) stay inside, or \n2) head on over to walk with them?\n\n>> ")
	if choice == "1":
		inside()
	elif choice == "2":
		walkWithDinoBear()
	else:
		print("Please enter a 1 or a 2. Thank you!")
		start()
	print("hi!")

def inside():
	print("Lame!")

def walkWithDinoBear():
	print("Awesome!")


start()
# exit() <-- end the entire game