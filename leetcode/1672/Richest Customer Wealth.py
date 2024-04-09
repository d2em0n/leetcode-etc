class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealth = 0
        for account in accounts:
            if sum(account) > maxWealth: maxWealth = sum(account)
        return maxWealth