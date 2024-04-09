k = int(input())

p = []

for i in range(k):

    p.append(list(map(int, input().split())))

#print(k)

#for i in range(k):

#    print(p[i])

 

xMin = p[0][0]

yMin = p[0][1]

xMax = p[0][0]

yMax = p[0][1]

 

for i in range(k):

    if xMin > p[i][0]: xMin = p[i][0]

    if yMin > p[i][1]: yMin = p[i][1]

    if xMax < p[i][0]: xMax = p[i][0]

    if yMax < p[i][1]: yMax = p[i][1]

 

print(xMin, yMin, xMax, yMax)