class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dpStairs = [0] * (n + 1)

        dpStairs[1] = 1
        dpStairs[2] = 2

        for i in range(3, n + 1):
            dpStairs[i] = dpStairs[i-1] + dpStairs[i-2]
        return dpStairs[n]