class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1: return False
        def dividers(s):
            div = []
            for i in range(2, len(s) + 1):
                if len(s) % i == 0:
                    div.append(i)
            return div
        div = dividers(s)
        if len(div) == 0: return False
        answers =[]
        for i in div:
            if s[: len(s) // i] * i == s: answers.append(True)
            else: answers.append(False)
        for i in answers:
            if i: return True
        else: return False