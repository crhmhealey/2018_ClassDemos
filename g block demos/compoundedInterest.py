import sys
import math

p = eval(sys.argv[1]) #principal
r = eval(sys.argv[2]) #interest rate
t = eval(sys.argv[3]) #time

# option 1
result = p*math.exp(r*t)
print("Your money after",t,"years:",result)

# option 2
step1 = math.pow(math.e,r*t)
result = step1*p
print("Your money after",t,"years:",result)
