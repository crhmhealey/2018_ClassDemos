import random
import math as m

# currency convertor
dollars = input('Dollars to yen: ')
result = float(dollars) * 111.47
print("Yen:",result)

x = random.random() # random betwen 0 (inclusive) and 1 (exclusive)
print(x)

y = random.randrange(0,101,10) # random between 0 and 100 inclusive, multiples of 10
print(y)

theta = random.random()*m.pi*2
trigResult = m.sin(theta)**2 + m.cos(theta)**2
print(trigResult)