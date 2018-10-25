class Dog:
	# constructor
	# initializes properties and sets up the dog object
	# kind = "Dog"
	def __init__(self, name, hunger, energy):
		self.hunger = hunger
		self.energy = energy
		self.name = name

	# methods / functions
	def eat(self,amount):
		status = ""
		if self.hunger > 0:
			self.hunger -= amount
			self.energy += amount
			status = self.name+" just ate a delicious meal!"
		else:
			status = self.name+" refused to eat because they feel like a fatty!"
		return status


	# there is an awesome nice ting to do here; talk about later
	def stats(self):
		return "Name: "+self.name+"\nEnergy: "+str(self.energy)+"\nHunger: "+str(self.hunger)


dogname = input("What do you want to name your dog?")
dog1 = Dog(dogname, 5, 2)
dog2 = Dog("Mary", 3, 9)

while True:
	print(dog1.stats())
	print(dog2.stats())
	choice = input("What do you want to do?")
	if choice == "eat":
		print(dog1.eat(2))
		print(dog2.eat(2))
	else:
		print("Can't do that.")















