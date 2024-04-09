class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sumPrim = 0
        sumSec = 0
        for i in range(len(mat)):
            sumPrim += mat[i][i]
            sumSec += mat[i][len(mat) - i -1]
        if len(mat)%2 == 0: return sumSec + sumPrim
        else: return sumSec + sumPrim - mat[len(mat)//2][len(mat)//2]