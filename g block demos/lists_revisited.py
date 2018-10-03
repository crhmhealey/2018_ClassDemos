i = [[1,2,3],[4,5,6],[7,8,9]]

print(i[2][1])

i = []
for x in range(10):
	i.append(0)

print(i)

i = [0]*10
print(i)

i = [[0]*10 for x in range(10)]
print(i)

i = []
for x in range(10):
	k = [0]*10
	i.append(k)

print(i)

for x in range(len(i)):
	print(i[x])

for x in i:
	print(*x)










