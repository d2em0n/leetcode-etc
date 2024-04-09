#известный художник

# n =  int(input())
# days = [*map(int, input().split())]
# n = 6
# days = [1, 2, 1, 3, 1, 3]
n = 4
days = [2, 1, 0, -1]

minA, maxA, minI, maxI = 0, 0, 0, 0
if days[0] >= days[1]:
    maxA = days[0]
    maxI = 0
    minA = days[1]
    minI = 1
else:
    maxA = days[1]
    maxI = 1
    minA = days[0]
    minI = 0

for i in range(2, n):
    if days[i] >= maxA:
        maxA = days[i]
        maxI = i
    if days[i] < minA:
        minA = days[i]
        minI = i

print(maxI + 1, minI + 1)