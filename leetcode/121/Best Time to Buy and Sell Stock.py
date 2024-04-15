class Solution:
    def maxProfit(prices):
        maxProfit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            sell += 1
        return maxProfit


    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    print(maxProfit(prices))