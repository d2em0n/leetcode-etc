
# n = 5
# m = ['W.W', 'C.C', 'WW.', 'CC.', 'CWW']
# # n = 4
# # m = ['W.W'
# # CWC
# # W.W
# # CWW
# #
n = int(input())
m = []
for i in range(n):
    m.append(input())
minimum = -n-1
counter = 0
step = [0, 0, 0]
for i in range(3):
    if m[0][i] == 'W':
        step[i] = minimum
    elif m[0][i] == 'C':
        step[i] = 1
i = 1
while i < n:
    nextStep = [minimum, minimum, minimum]
    for k in range(3):
        if m[i][k] == 'W':
            continue
        elif m[i][k] == 'C' or '.':
            if m[i][k] == 'C':
                ds = 1
            else: ds = 0
            if k == 0:
                s0 = step[0]
                s1 = step[1]
                next = max(s0, s1) + ds
                if nextStep[0] < next : nextStep[0] = next
            elif k == 1:
                s0 = step[0]
                s1 = step[1]
                s2 = step[2]
                next = max(max(s0, s1), s2) + ds
                if nextStep[1] < next: nextStep[1] = next
            else:
                s1 = step[1]
                s2 = step[2]
                next = max(s1, s2) + ds
                if nextStep[2] < next: nextStep[2] = next
    step = nextStep
    counter = max(counter, max(max(step[0], step[1]), step[2]))
    i += 1
print(counter)

