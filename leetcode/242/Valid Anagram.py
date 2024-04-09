class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        a = list(i for i in s)
        b = list(i for i in t)
        a.sort()
        b.sort()
        for i in range(len(a)):
            if a[i] != b[i]: return False
        return True