# empty list
a = []

# add 2 to our list?
a += [2]
a.append(4)
a.append(7)
a.append(1)
a.append(3)
a = [2,1,2,3,4,5] + a
print(a)

# update a value
a[4] = 7

# print the list
print(a)

# remove from the list
del a[5]
print(a)

print(a.pop())
print(a)

a.remove(2)
print(a)

print(a[3])
print(a[-2])

# swap
c = 1
b = 5

temp = c 
c = b
b = temp

c,b = 1,5
c,b = b,c
print(c,b)

a[3],a[5] = a[5],a[3]
print(a)
#--------------------------
sevens = []
count = 0
while count < 700:
	sevens.append(count)
	count += 7
print(sevens,len(sevens))
#-----------------------------
sevens = []
for x in range(0,700,7):
	sevens.append(x)
print(sevens,len(sevens))
#----------------------------
sevens = [x for x in range(0,700,7)]
print(sevens,len(sevens))
#--------------------------
sevens = []
for i in range(100):
	sevens.append(7*i)
print(sevens,len(sevens))


# range(5) = 0-4
# range(5,8) = 5-7







