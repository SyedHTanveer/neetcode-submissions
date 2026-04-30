class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        prev1, prev2, prev3 = 1, 1, 0

        for i in range(2,n):
            t = prev1 + prev2 + prev3

            prev1, prev2, prev3 = t, prev1, prev2
        
        return prev1