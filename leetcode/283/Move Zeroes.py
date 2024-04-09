class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def moveZero(nums):
            zeroI = []
            for i in range(len(nums)):
                if nums[i] == 0:
                    zeroI.append(i)
            return zeroI            

        zeroI = moveZero(nums)
        
        for i in range(len(zeroI)):
            zeroI[i] -= i
        for i in zeroI:
            nums.pop(i)
            nums.append(0)
