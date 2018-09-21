while True:
	try:
		x = int(input("Enter a number: "))
		break
	except ValueError:
		print("Nope. Try again.")

count = 0

while count < x:
	print("Hello!")
	count+=1
