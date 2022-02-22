# Problem: Best Time to Buy and Sell Stock II
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#
# Problem outline:
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_length = len(prices)

        buy_price, sell_price, profits = prices[0], -1, 0

        for n in range(1, price_length):
            price_diff = prices[n] - prices[n - 1]

            # if price has dropped,
            # either sell off at previous day's price (peak) if no sale was previously made
            # or buy at this price
            if price_diff < 0:
                if sell_price > -1:
                    profits += sell_price - buy_price
                    sell_price = -1
                    buy_price = prices[n]
                else:
                    buy_price = prices[n] if prices[n] < buy_price else buy_price
            else:  # if price has increased, do not buy and look for max selling price
                sell_price = prices[n] if prices[n] > sell_price else sell_price

        # accounts for non-sale if price does not drop in the last few days
        potential = sell_price - buy_price
        if potential > 0:
            profits += potential

        return profits