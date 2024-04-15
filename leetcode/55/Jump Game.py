class Solution:
    def canJump(nums):
        destinations = [0, nums[0]]
        for i in range(1, len(nums)):
            if i > destinations[1]: return False
            else:
                if destinations[1] < nums[i] + i:
                    destinations[1] = nums[i] + i
        return True

    # nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    print(canJump(nums))
