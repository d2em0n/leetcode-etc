class Solution:
    def removeDuplicates(nums):
        k = 0
        for num in nums:
            if num != nums[k]:
                k += 1
                nums[k] = num
        return k + 1






    # nums = [1, 1, 2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
    print(nums)
