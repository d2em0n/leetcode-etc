# n, m = map(int, input().split())
# f = [input() for i in range(n)]
# # #

n,m = 5, 4
f = ['4412', '3212', '0121', '2192', '4103']
p = []

for str in f:
   p.append([int(symbol) for symbol in str])

def sumCross(x, y, lst):
   str = 0
   for i in range(len(lst[x])):
      str += lst[x][i]
   col = 0
   for i in range(len(lst)):
      col += lst[i][y]
   return str + col - lst[x][y]

def findMax(arr, exceptRow, exceptColumn):
   ans = 0
   x, y = 0, 0
   for i in range(len(arr)):
      if i!=exceptRow:
         for j in range(len(arr[i])):
            if j!=exceptColumn:
               if ans < arr[i][j]:
                  ans = arr[i][j]
                  x = i
                  y = j
   return x, y, ans

xMax, yMax, maxValue = findMax(p, -1, -1)
print(xMax, yMax, maxValue)
xExceptRow, yExceptRow, vExceptRow = findMax(p, xMax, -1)
x1, y1, v1 = findMax(p, xMax, yExceptRow)
xExceptColumn, yExceptColumn, vExceptColumn = findMax(p, -1, yMax)
x2, y2, v2 = findMax(p, xExceptColumn, yMax)

if v1<v2: print(xMax + 1, y1 + 1)
else: print(x2 + 1, yMax + 1)
print(findMax(p, -1, -1))