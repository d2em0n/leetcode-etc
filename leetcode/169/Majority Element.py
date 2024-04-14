class Solution:
    def majorityElement(nums):
        d = {}
        counter = 0
        answer = 0
        for n in nums:

            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1
            if d[n] > counter:
                counter = d[n]
                answer = n
        return answer


    nums = [3, 2, 3]
    # nums = [2, 2, 1, 1, 1, 2, 2]
    # nums = [3, 3, 4]

    print(majorityElement(nums))