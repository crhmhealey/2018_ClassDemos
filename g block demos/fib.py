# beautiful solution from:
# https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/
# but DON'T USE RECURSION!

import sys

def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b 
		# line above explanation: https://stackoverflow.com/questions/8725673/multiple-assignment-and-evaluation-order-in-python
	return a

print(fib(int(sys.argv[1])))