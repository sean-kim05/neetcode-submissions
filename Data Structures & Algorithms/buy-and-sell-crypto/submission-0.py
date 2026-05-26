class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        lowest_price = prices[0]
        for i in prices:
            if i < lowest_price:
                lowest_price = i
            profit = max(profit, i - lowest_price)
        return profit
        