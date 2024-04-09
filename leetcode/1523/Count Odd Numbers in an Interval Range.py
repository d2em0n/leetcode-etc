class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = (high - low) // 2
        if high %2 != 0: ans += 1
        if low % 2 != 0: ans += 1
        if high %2 != 0 and low % 2 != 0: ans -= 1
        return ans