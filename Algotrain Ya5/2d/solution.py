n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

p = tuple((points[i]) for i in range(n))

xCounter = 0
dX = (0, 0, -1, 1)
dY = (-1, 1, 0, 0)
for i in range(n):
    for k in range(len(dX)):
        if ([p[i][0] + dX[k] , p[i][1] +dY[k]]) in p:
            xCounter += 1

if n == 1: print(4)
else: print( n*4 - xCounter)