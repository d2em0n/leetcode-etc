class Solution:
    def removeDuplicates(nums):
        i = 0
        k = 0
        while i < len(nums):
            counter = 0
            while nums[i] == nums[k]:
                counter += 1
                i+=1
                if i == len(nums): break
            if counter == 1:
                if i < len(nums):
                    nums[k + 1] = nums[i]
                k += 1

            elif counter == 2:
                nums[k] = nums[i-1]
                nums[k + 1] = nums[i-1]
                if i < len(nums):
                    nums[k + 2] = nums[i]
                k += 2

            else:
                nums[k] = nums[i - 1]
                nums[k + 1] = nums[i - 1]
                if i < len(nums):
                    nums[k + 2] = nums[i]
                k += 2
        return k
    # nums = [0,0,1,1,1,1,2,3,3]
    # nums = [1,1,1,2,2,3]
    # nums = [0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]
    nums = [1,1,1]
    print(removeDuplicates(nums))
    print(nums)
