class Solution:
    def maxProfit(prices):
        buy = prices[0]
        sell = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < buy:
                profit += sell - buy
                buy = price
                sell = price
            else:
                sell = price
                profit += sell - buy
                buy = sell
        return profit

    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [7,6,4,3,1]
    prices = [1, 2, 3, 4, 5]
    print(maxProfit(prices))
