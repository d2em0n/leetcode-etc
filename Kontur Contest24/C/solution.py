n, q = map(int, input().split())


def siege(rook):
    for i in range(1, n + 1):
        field[rook[0]][i] = -1
        field[i][rook[1]] = -1

def paint(x0, y0, step):
    for y in range(y0, n+2):
        if field[x0][y] != -1:
            field[x0][y] = step
        else:
            break
        for x in range(x0, n +2):
            if field[x][y] != -1:
                field[x][y] = step
            else:
                break



rooksQ = [list(input().split()) for i in range(q)]
rooks = []
for i in range(q):
    field = [[0] * (n + 2) for k in range(n + 2)]
    for j in range(n + 2):
        field[0][j] = -1
        field[j][0] = -1
        field[n + 1][j] = -1
        field[j][n + 1] = -1

    if rooksQ[i][0] == "+":
        rooks.append((int(rooksQ[i][1]), int(rooksQ[i][2])))
    else:
        rooks.remove((int(rooksQ[i][1]), int(rooksQ[i][2])))

    for rook in rooks:
        siege(rook)

    step = 0
    for y in range(1, n+2):
        for x in range(1, n+1):
            if field[x][y] == 0:
                step += 1
                paint(x, y, step)

    print(step)




for i in field:
    for k in range(len(i)):
        print(i[k], end = "\t")
    print("\n")



