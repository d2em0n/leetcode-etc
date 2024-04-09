class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def findZeroes():
            arrZ = []
            for y in range(len(matrix)):
                for x in range(len(matrix[0])):
                    if matrix[y][x] == 0:
                        arrZ.append([y, x])
            return arrZ

        def setZeroRow(x):
            for y in range(len(matrix)):
                matrix[y][x] = 0

        def setZeroColumn(y):
            for x in range(len(matrix[0])):
                matrix[y][x] = 0

        zeroes = findZeroes()
        xZeroes = set(zeroes[i][1] for i in range(len(zeroes)))
        yZeroes = set(zeroes[i][0] for i in range(len(zeroes)))
        for x in xZeroes:
            setZeroRow(x)
        for y in yZeroes:
            setZeroColumn(y)
        