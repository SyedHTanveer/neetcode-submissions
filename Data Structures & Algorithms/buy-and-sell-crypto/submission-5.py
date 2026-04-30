class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, max_profit , r = 0, 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return max_profit