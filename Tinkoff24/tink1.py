# n = 9
# # m = [5, 5, 4, 5, 4, 5, 4, 5, 4]
# n = 8
# m = [3, 4, 4, 4, 4, 5, 4, 5]
# n = 10
# m = [5, 5, 5, 5, 5, 3, 5, 5, 5, 5]
# n = 7
# m = [5, 5, 5, 5, 5, 5, 5]
# n = 5
# m = [3, 2, 3, 5, 5]
n = int(input())
m = list(map(int, input().split()))
counter = -1
for i in range(n-6):
    cur = 0
    bad = 0
    for k in range(i, i + 7):
        if m[k] == 5: cur += 1
        if m[k] ==2 or m[k] == 3:
            bad += 1
            break
    if bad == 0: counter = max(cur, counter)
print(counter)

print(n)
print(m)