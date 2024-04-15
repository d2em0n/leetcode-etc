class Solution:
    def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        buf = nums[-k:]
        for i in range(-1, -len(nums) + k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = buf[i]

    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 3
    # nums = [-1,-100,3,99]
    # k = 2
    nums  = [-1]
    k = 2
    rotate(nums, k)
    print(nums)