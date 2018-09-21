import random as r

def getNum():
	global usedNumbers, userOrder
	userchoice = int(input("Number:"))
	count = 0
	worked = False;
	while count < len(numbers):
		if (numbers[count] == userchoice and usedNumbers[count]!= True):
			usedNumbers[count] = True
			userOrder.append(numbers[count])
			worked = True
			break
		count+=1
	if (worked!=True):
		print("You can't pick that number.")


numbers = [r.randrange(1,14,1),r.randrange(1,14,1),r.randrange(1,14,1),r.randrange(1,14,1)]

usedNumbers = [False, False, False, False]

userOrder = []

print(numbers)

getNum()

print(numbers,usedNumbers,userOrder)

getNum()

print(numbers,usedNumbers,userOrder)



