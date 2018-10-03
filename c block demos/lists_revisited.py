apples = []
for orange in range(5):
	apples.append(orange)

i = [x for x in range(5)]

i = [[1,2,3],[4,5,6],[7,8,9]]
i[1][0]

i = [0 for x in range(12)]
print(i)

j = [0]*12
print(j)

i = [[0]*10 for x in range(10)]
print(i)

for x in range(len(i)):
	print(*i[x])