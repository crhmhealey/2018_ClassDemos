# def question():
# 	response = input("Give me info: ")
# 	if response == "hi":
# 		print("a")
# 	elif response == "b":
# 		print("b")
# 	else:
# 		print("This is useless info! Try again.")
# 		question()

# question()


# while count<5:
# 	print("hi!")
# 	count+=1

def question():
	response = input("Give me info: ")
	while response != "hi" or response != "b":
		print("This is useless info! Try again.")
		response = input("Give me info: ")

	if response == "hi":
		print("a")
	elif response == "b":
		print("b")

question()


