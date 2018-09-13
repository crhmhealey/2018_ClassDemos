import random
import math as m

celsius = float(input("Please enter degrees in celsius: "))
kelvin = celsius + 273.15
print("The temp is:",kelvin)

theta = random.random()*m.pi*2
trigResult = m.sin(theta)**2 + m.cos(theta)**2
print(trigResult)