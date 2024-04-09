s = input()

div = []
for i in range(1, len(s) + 1):
    if len(s) % i == 0: div.append(i)

def cutStr(s, d):
    arr = []
    for i in range(0, len(s), d):
        arr.append(s[i : i + d])
    return arr

def makeBeauty(s):
    c0 = 0
    c1 = 0
    for i in s:
        if i == "0": c0 += 1
        else: c1 += 1
    return [c0, c1]


counter = []
for d in div:
    a = cutStr(s, d)
    p = []
    for i in range(len(a)):
        p.append(makeBeauty(a[i]))

    c0 = 0
    for i in range(len(p)):
        if i%2 == 0: k=0
        else: k = 1
        c0 += p[i][k]
    c1 = 0
    for i in range(len(p)):
        if i % 2 == 1: k= 0
        else: k = 1
        c1 += p[i][k]
    counter.append(min(c0, c1))

print(min(counter))


