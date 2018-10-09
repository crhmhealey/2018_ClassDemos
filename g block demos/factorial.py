def factorial(n):
	if n is 0 or n is 1:
		return 1
	return factorial(n-1)*n

print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
print(factorial(0))

# evil fib but interesting for recursion
def fib(n):
	if n is 0 or n is 1:
		return n
	return fib(n-1)+fib(n-2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))

# class exercises
def countx(word):
	if len(word) < 1:
		return 0
	if word[0] is "x":
		return 1+countx(word[1:])
	return countx(word[1:])

print(countx("xx53xx"))
print(countx("abcdefgzxjefjnsdzxmijderbgrnjkldms"))

def crazy_eights(n):
	if n is 0:
		return 0
	if n%10 == 8:
		if n%100 == 88:
			return 2 + crazy_eights(n//10)
		return 1 + crazy_eights(n//10)
	return crazy_eights(n//10)

print(crazy_eights(8918228))
print(crazy_eights(88918))
print(crazy_eights(1234))
print(crazy_eights(89288438))
print(crazy_eights(888988980))

# from: https://introcs.cs.princeton.edu/python/23recursion/euclid.py.html
'''
The greatest common divisor (gcd) of two positive integers is the largest integer that divides evenly into both of them. For example, the greatest common divisor of 102 and 68 is 34 since both 102 and 68 are multiples of 34, but no integer larger than 34 divides evenly into 102 and 68.

We can efficiently compute the gcd using the following property, which holds for positive integers p and q:

If p > q, the gcd of p and q is the same as the gcd of q and p % q.
The function gcd() in euclid.py is a compact recursive function whose reduction step is based on this property
'''

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

print(gcd(4, 8))
print(gcd(3, 27))
print(gcd(100,250))
print(gcd(78, 1258))




