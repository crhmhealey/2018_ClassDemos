while True:
	try:
		num = int(input("Pick a number between 1 and 5: "))
		if 1<=num<=5:
			break
		else:
			print("That's not in the right range.")
	except ValueError:
		print("That's not a number. Try again.")

print("Success!")

