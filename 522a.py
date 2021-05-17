n = int(input())

men = [0] * (n+1)
for i in range(n+1):
	men[i] = [0] * 2

men[0][0] = 'polycarp'
men[0][1] = 1

for i in range (n):
	x, b, y = input().split()
	a = x.lower()
	c = y.lower()
	men[i+1][0] = a
	for j in range (n+1):
		if men[j][0] == c:
			men[i+1][1] = men[j][1]+1

k = 0
for i in range (n+1):
	if men[i][1] > k:
		k = men[i][1]



print(k)
