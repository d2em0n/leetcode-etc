class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s += t
        dict = {}
        for i in s:
            if i not in dict.keys():
                dict[i] = 1
            else:
                dict[i] += 1
        for i in dict.keys():
            if dict[i] % 2 != 0: return i