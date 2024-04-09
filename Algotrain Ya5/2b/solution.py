sizes = list(map(int, input().split()))

days = list(map(int, input().split()))

n, k  = sizes[0], sizes[1]

margin = 0

 

for i in range(k):

    days.append(0)

 

for i in range(n):

    for j in range(1, k + 1):

        if days[i + j] - days[i] > margin: margin = days[i + j] - days[i]

 

print(margin)