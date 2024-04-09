class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        def  isPointInLine(x, y, a, b):
            return abs(a * x + b - y) < 0.000001
        if len(coordinates) == 2: return True
        if coordinates[0][0] == coordinates[1][0]:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]: return False
            return True
        elif coordinates[0][1] == coordinates[1][1]:
            for i in range(2, len(coordinates)):
                if coordinates[i][1] != coordinates[0][1]: return False
            return True
        a = (float(coordinates[0][1]) - float(coordinates[1][1]))/(float(coordinates[0][0])- float(coordinates[1][0]))
        b = float(coordinates[0][1]) - a*coordinates[0][0]
        for i in range(2, len(coordinates)):
            if not isPointInLine(coordinates[i][0], coordinates[i][1], a, b): return False
        return True