class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = cost[0]
        dp2 = cost[1]

        for i in range(2,len(cost)):
            dp1, dp2 = dp2, cost[i] + min(dp1, dp2)
        
        return min(dp1, dp2)