# size = [2, 2]
# array = [[1, 1], [2, 3]]

# size = [1, 1]
# array = [[69]]

# size = [2, 3]
# array = [[1, 2, 3], [4, 5, 6]]



size = list(map(int, input().split()))
array = []
for i in range(size[0]):
    array.append(list(map(int, input().split())))
def rotateArray(array, size):
    ans = [[0] * size[0] for i in range(size[1])]
    for i in range(size[1]):
        for k in range(size[0]):
            ans[i][k] = array[size[0] -1 -k][i]
    return ans

def printArr(array):
    for i in range(len(array)):
        print(*array[i])

printArr(rotateArray(array, size))



