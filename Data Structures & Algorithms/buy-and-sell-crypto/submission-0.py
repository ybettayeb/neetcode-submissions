class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = 0, 1
        bestProfit = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                bestProfit = max(bestProfit,profit)
            sell += 1

        return bestProfit
            
            
        