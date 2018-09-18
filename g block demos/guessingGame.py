import random
number = random.randrange(1,11)

def start():
	guess = eval(input("Guess a number between 1 and 10: "))
	if guess == number:
		print("That's it! Well done.")
		exit()
	elif guess > number:
		print("That's too high! Guess again.")
	elif guess < number:
		print("That's too low! Guess again.")
	else:
		print("Something went wrong. Guess again?")
	start()

start()