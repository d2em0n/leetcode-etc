class Solution:
    def mySqrt(x):
        a = 2
        b = x // 2
        while b > a:
            b = b // 2
            a = a * 2

        while b < a and a - b > 1:
            m = (a + b) // 2
            if m * m <= x:
                b = m
            else:
                a = m
        return b

    print(mySqrt(6))
