#коллекционер ковров
# n = 8
# points = [[0, 0],[1,1], [0,2], [5,0], [5,2], [0,4], [3, 0], [3, 4]]
n= 4
points = [[1, -1], [1,1], [-1, 1], [1,0]]


# n = int(input())
# points = []
# for i in range(n):
#     points.append(list(map(int, input().split())))
s = 0
p = tuple((points[i]) for i in range(n))

dictX = {}
for i in range(n):
    if points[i][0] not in dictX.keys(): dictX[points[i][0]] = [points[i][1]]
    else: dictX[points[i][0]].append(points[i][1])

dictY = {}
for i in range(n):
    if points[i][1] not in dictY.keys(): dictY[points[i][1]] = [points[i][0]]
    else: dictY[points[i][1]].append(points[i][0])

for i in range(n):
    if len(dictX[points[i][0]]) < 2 or len(dictY[points[i][1]]) < 2: continue
    else:
        for y in dictX[points[i][0]]:
            if y != points[i][1]:
                for x in dictY[y]:
                    if x!=points[i][0]:
                        if [x, y] in p:
                            tempS = (y - points[i][1]) * (x - points[i][0])
                            if tempS > s: s= tempS


print(points)
print(dictY, dictX)
print(s)