import random
class Account:
	def __init__(self, amount, pin):
		self.balance = amount
		self.pin = pin
		self.account = random.randint(10000000,99999999)
		self.isOpen = True

	def close(self, pin):
		if self.pin == pin:
			isOpen = False
			money = self.balance 
			self.balance = 0
			return money
		else:
			return pinerror()

	def deposit(self, amount, pin):
		if self.pin == pin:
			self.balance += amount
		else:
			return pinerror()

	def widthdrawal(self, amount, pin):
		if self.pin == pin:
			if self.balance > amount:
				self.balance -= amount
				return "success"
			else:
				return "insufficient funds"
		else:
			return pinerror()

	def pinerror(self):
		return "wrong pin"


ba = Account(500, 1111)
print(ba.withdrawal(200, 1123))
print(ba.withdrawal(200, 1111))
print(ba.withdrawal(500, 1111))
print(ba.deposit(500, 5432))
print(ba.deposit(500, 1111))
ba.close() 