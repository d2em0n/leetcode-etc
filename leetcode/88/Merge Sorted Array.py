class Solution:
    def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        i = -1
        while i >= len(nums1) * (-1) and n > 0:
            if nums1[m - 1] == nums2[n-1]:
                nums1[i] = nums1[m - 1]
                m -= 1
                i -= 1
                nums1[i] = nums2[n - 1]
                n -= 1
                i -= 1
            elif nums1[m-1] > nums2[n-1]:
                nums1[i] = nums1[m-1]
                m -= 1
                i -= 1
            else:
                nums1[i] = nums2[n-1]
                n -= 1
                i -= 1
        else:
            for i in range(n):
                nums1[i] = nums2[i]


    #
    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3


    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0

    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1

    # nums1 = [1, 0]
    # m = 1
    # nums2 = [2]
    # n = 1

    # nums1 = [2, 0]
    # m = 1
    # nums2 = [1]
    # n = 1

    # nums1 =    [1, 0, 0, 0, 0, 0]
    # m =    1
    # nums2 =    [2, 3, 4, 5, 6]
    # n = 5
    #
    # merge(nums1, m, nums2, n)
    # print(nums1)