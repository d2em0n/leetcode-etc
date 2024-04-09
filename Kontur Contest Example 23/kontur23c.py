# inp = [*map(int, input().split())]
# n= inp[0]
# k= inp[1]
# a = [*map(int, input().split())]
n = 4
k = 1
a = [0, 1, 1, 0]
# n = 4
# k = 4
# a = [1, 2, 3, 4]
counter = 0
for i in range(n):
    zeroC = 0
    s = 0
    j = i
    while j < n:
        s += a[j]
        if s > k: break
        if a[j] == 0: zeroC += 1
        if zeroC > 1: break
        counter += 1
        j += 1

print(n, k)
print(a)
print(counter)