class Dog:

	# constructor
	# scale out of 10
	def __init__(self, name, energy, fullness):
		self.fullness = fullness
		self.energy = energy
		self.happiness = 5
		self.name = name

	# methods / functions

	def play(self):
		if self.energy > 0 and self.fullness > 0:
			self.happiness+=1
			self.fullness -= 1
			self.energy -= 1
			status = self.name+" played and it was fun."
		else:
			status = "Erm, "+self.name+" needs to not play right now. Maybe try a nap or some food?"
		return status


	def stats(self):
		info = "Name: "+ self.name
		info += "\nEnergy: " + str(self.energy)
		info += "\nHappiness: " + str(self.happiness)
		info += "\nFullness: " + str(self.fullness)
		return info




dog1 = Dog("Tetris", 8, 2)
dog2 = Dog("Bat", 5, 7)
# print(dog1.name)

while True:
	print(dog1.stats())
	choice = input("What would you like to do with your dog?")
	if choice == "play":
		print(dog1.play())
	else:
		print("You can't do that.")














