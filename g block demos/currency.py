import math as m
import random as r

# Currency Converter
# Dollars to Yen

dollars = float(input("Dollars: "))
# print(type(dollars))
yen = dollars * 111.61
print("Yen:",yen)

theta = r.random()*m.pi*2 # values between 0 and 2PI
result = m.sin(theta)**2 + m.cos(theta)**2
print(result)
