class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        ans = ""
        if len1 == len2:
            for i in range(len1):
                ans+=word1[i]
                ans+=word2[i]
        elif len1 < len2:
            for i in range(len1):
                ans+=word1[i]
                ans+=word2[i]
            ans+=word2[i+1:]
        else:
            for i in range(len2):
                ans+=word1[i]
                ans+=word2[i]
            ans+=word1[i+1:]        
        return ans

        