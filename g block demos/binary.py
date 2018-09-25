def binaryToDecimal(number):
	counter = 0
	total = 0
	while number>0:
		current = number%10
		total += 2**counter * current
		counter += 1
		number = number//10
	return total

print(binaryToDecimal(1101))
print(binaryToDecimal(10))
print(binaryToDecimal(1101000111100010101))