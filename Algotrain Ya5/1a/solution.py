vasya = input()
masha = input()
p = list(map(int, vasya.split()))[0]
v = list(map(int, vasya.split()))[1]
q = list(map(int, masha.split()))[0]
m = list(map(int, masha.split()))[1]
l1 = p - v
r1 = p + v
l2 = q - m
r2 = q + m
if l1 > l2:
    l1, l2 = l2, l1
    r1, r2 = r2, r1
if r1 < l2:
    answer = 2 + 2*v + 2*m
else:
    if r2<r1:
        answer = 1 + abs(l1-r1)
    else:
        answer = 1 + abs(l1-r2)
print(answer)