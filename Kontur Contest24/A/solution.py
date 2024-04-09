n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sMin = sum(a)
sMax = sum(b)
if (t >= sMin) and (t<= sMax): print("YES")
else: print("NO")

print(n, t)
print(a)
print(b)