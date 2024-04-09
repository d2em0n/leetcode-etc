class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        borders = [0, len(matrix[0]), len(matrix), 0]
        def goRight():
            for x in range(borders[0], borders[1]):
                answer.append(matrix[borders[3]][x])
            borders[1] -= 1
        def goDown():
            for y in range(borders[3] + 1, borders[2] ):
                answer.append(matrix[y][borders[1]])
            borders[2] -= 1
        def goLeft():
            for x in range(borders[1] - 1, borders[0] - 1, -1):
                answer.append(matrix[borders[2]][x])
            borders[0] += 1
        def goUP():
            for y in range(borders[2] -1 , borders[3], -1):
                answer.append(matrix[y][borders[0] - 1])
            borders[3] += 1
        def checked():
            return borders[0] <= borders[1] and borders[2] >borders[3]

        while True:
            goRight()
            if not checked(): break
            goDown()
            if not checked(): break
            goLeft()
            if not checked(): break
            goUP()
            if not checked(): break
        return answer