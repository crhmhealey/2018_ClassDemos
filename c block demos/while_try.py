while True:
	try:
		num = int(input("Pick a number between 1 and 5: "))
		break
	except ValueError:
		print("Yeah, no. That's not an integer.")

while num > 5 or num < 1:
	num = int(input("That's not right. I said, pick a number between 1 and 5: "))

print("Success!")