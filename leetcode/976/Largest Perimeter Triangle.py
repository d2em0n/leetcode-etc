class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def triangeIsPossible(a, b, c):
            return a + b > c and a + c > b and b + c > a
        perimeter = 0
        nums.sort(reverse = True)
        for i in range(2, len(nums)):
            if triangeIsPossible(nums[i], nums[i-1], nums[i-2]):
                if perimeter < nums[i] + nums[i-1] + nums[i-2]:
                    perimeter = nums[i] + nums[i-1] + nums[i-2]
                    break
                else: continue
        return perimeter

