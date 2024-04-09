class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        if n > 0:
            return pow(x, n)
        else:
            return pow(1/x, -n)

    @staticmethod
    def pow(self, x: float, n: int) -> float:
        if n // 2 == 1:
            return x
        if n % 2 == 1:
            y = pow(x, n // 2)
            return x*y*y
        else:
            y = pow(x, n // 2)
            return y*y