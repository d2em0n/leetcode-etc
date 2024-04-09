class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True

        def isMonotonicInc(nums):
            for i in range(1, len(nums)):
                if nums[i] >= nums[i-1]:
                    continue
                else: return False
            return True

        def isMonotonicDec(nums):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    continue
                else: return False
            return True

        if isMonotonicInc(nums): return True
        if isMonotonicDec(nums): return True
        return False