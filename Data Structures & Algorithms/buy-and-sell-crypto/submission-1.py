class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i, j, maxProfit = 0, 1, 0

        while j < len(prices):
            if prices[i] < prices[j]:
                currProfit = prices[j] - prices[i]
                maxProfit = max(maxProfit, currProfit)
            else:
                i = j
            j += 1

        return maxProfit