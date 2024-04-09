class Solution:
    def arraySign(self, nums: List[int]) -> int:
        countNegatives = 0
        for num in nums:
            if num == 0: return 0
            elif num < 0: countNegatives += 1
        if countNegatives % 2 == 0: return 1
        else: return -1