def Clicks(spaces):

    if spaces == 0: return 0

    counter = spaces // 4

    remainder = spaces % 4

    if remainder == 0: return counter

    if remainder == 1: return counter + 1

    if remainder == 2: return counter + 2

    if remainder == 3: return counter + 2

 

 

size = int(input())

sum = 0

for i in range(0, size):

    sum += Clicks(int(input()))

print(sum)