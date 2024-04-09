class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        i = -1
        while s[i] == " " and i > len(s) * (-1) - 1:
            i -= 1
        while s[i] != " ":
            i -= 1
            counter += 1
            if i == len(s) * (-1) - 1: break
        return counter