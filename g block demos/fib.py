# beautiful solution from:
# https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/
# but DON'T USE RECURSION!

import sys

def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a

print(fib(int(sys.argv[1])))