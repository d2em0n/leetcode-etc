class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difs = {}
        for i in range(len(nums)):
            difs[nums[i]] = [target - nums[i], i]

        for i in range(len(nums)):
            if target - nums[i] in difs.keys() and i != difs[target - nums[i]][1]:
                return [i, difs[target - nums[i]][1]]