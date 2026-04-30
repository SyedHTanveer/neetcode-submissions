class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            
            r = i + 1

            while r < len(prices):
                if prices[i] < prices[r]:
                    max_profit = max(max_profit, prices[r] - prices[i])
                    r += 1
                elif prices[i] == prices[r]:
                    r += 1
                else:
                    break
            
        return max_profit