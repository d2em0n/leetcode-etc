class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        lbl1 = 0
        lbl2 = 0
        lbl3 = 0
        for i in range(-1, len(s)*(-1) - 1, -1):

            if s[i] == "I" and lbl1 == 0: result += 1
            elif s[i] == "I" and lbl1 == 5 :
                result -= 1
                lbl1 = 0
            elif s[i] == "I" and lbl1 == 10:
                result -= 1
                lbl1 = 0
            if s[i] == "V":
                result += 5
                lbl1 = 5

            if s[i] == "X" and lbl2 == 0:
                result += 10
                lbl1 = 10
            elif s[i] == "X" and lbl2 == 50:
                result -= 10
                lbl2 = 0
            elif s[i] == "X" and lbl2 == 100:
                result -= 10
                lbl2 = 0
            if s[i] == "L":
                result += 50
                lbl2 = 50

            if s[i] == "C" and lbl3 == 0:
                result += 100
                lbl2 = 100
            elif s[i] == "C" and lbl3 == 500:
                result -= 100
                lbl3 = 0
            elif s[i] == "C" and lbl3 == 1000:
                result -= 100
                lbl3 = 0
            if s[i] == "D":
                result += 500
                lbl3 = 500
            if s[i] == "M":
                result += 1000
                lbl3 = 1000
        return result