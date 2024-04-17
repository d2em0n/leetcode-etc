class Solution:
    def jump(nums):
        if len(nums) == 1: return 0
        destinations = [0, nums[0]]
        step = 1
        d0 = 0
        d1 = 0
        while True:

            for i in range(destinations[0], destinations[1] + 1):
                if len(nums) - 1 <= destinations[1]:
                    return step
                if i + nums[i] > destinations[1]:
                    d0 = destinations[1]
                    d1 = max(i + nums[i], d1)
            destinations[0] = d0
            destinations[1] = d1
            step += 1








    # nums = [2, 3, 1, 1, 4]
    # nums  = [2, 3, 0, 1, 4]
    # nums = [1, 2]
    nums = [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7, 0,
     3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6, 7, 5,
     1, 9, 9, 3, 5, 0, 7, 5]
    # nums = [1, 2, 3]
    # nums = [2, 3, 1]
    # nums  = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
    print(jump(nums))