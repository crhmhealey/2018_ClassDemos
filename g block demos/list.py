import random

# empty list
a = []

# print list
print(a)

# add to list
a.append(5)
a.append(3)
a.append(8)
a.append(8)

print(a)

a = [1,2,3,4,5] + a

print(a)

# a.insert(0,[1,2,3,4,5])
# remove from list
del a[5]
print(a.pop()) # can accept argument for location

print(a)

print(len(a))

# remove random from list
x = random.randint(0,len(a)-1)
del a[x]
print(a)

# last thing in list
print(a[len(a)-1])
print(a[-1])

# swap
y,z = 5,10
y,z = z,y
print(y,z)

a[0],a[-1] = a[-1],a[0]

print(a)

sevens = []
for i in range(7,701,7):
	sevens.append(i)
print(sevens, len(sevens))
# print(*sevens, len(sevens)) # unpacks list

b = []
for i in range(2,5000,2):
	b.append(i)
print(b)

c = [x for x in range(2,5000,2)]










