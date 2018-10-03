i = [[1,2,3],[4,5,6],[7,8,9]]

print(i[2][1])

j = []
for x in range(10):
	j.append(0)
print(j)

j = [0]*10
print(j)


j = []
for x in range(10):
	k = [0]*10
	j.append(k)
print(j)

j = [[0]*10 for x in range(10)]
print(j)

for x in range(len(j)):
	print(*j[x])

