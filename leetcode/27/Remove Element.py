class Solution:
    def removeElement(nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

    # nums = [3, 2, 2, 3]
    # val = 3
    # print(removeElement(nums, val))
    # print(nums)
    #
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # val = 2
    # print(removeElement(nums, val))
    # print(nums)
    #
    # nums = [1]
    # val = 1
    # print(removeElement(nums, val))
    # print(nums)
    #
    # nums = [3, 3]
    # val = 3
    # print(removeElement(nums, val))
    # print(nums)
    # nums = []
    #
    # val = 0
    # print(removeElement(nums, val))
    # print(nums)
    #
    # nums = [2,2,3]
    # val = 3
    # print(removeElement(nums, val))
    # print(nums)