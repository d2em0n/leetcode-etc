n = int(input())

l = list(map(int, input().split()))

maxL = l[0]

sumL = l[0]

for i in range(1, n):

    sumL+=l[i]

    if maxL < l[i]: maxL=l[i]

#print(sumL, maxL)

if sumL-maxL >= maxL: print(sumL)

else: print(2*maxL - sumL)