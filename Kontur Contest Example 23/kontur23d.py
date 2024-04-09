n = 3
cubes = [[0, 1, 2, 3, 4, 5], [0, 0, 2, 3, 4, 5], [0, 0, 0, 3, 4, 5]]


# n = int(input())
# cubes = []
# for i in range(n):
#     cubes.append(set(map(int, input().split())))

ans = cubes[0]
temp = []
for i in range(1,n):
    temp.clear()
    for a in set(ans):
        for b in set(cubes[i]):
            temp.append(a + b)
    
    ans = set(temp)


print(len(cubes))
print(ans)
print(len(ans))