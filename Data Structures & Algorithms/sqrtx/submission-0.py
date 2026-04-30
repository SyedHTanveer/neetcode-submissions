class Solution:
    def mySqrt(self, x: int) -> int:
        
        i, j, res = 0 , x, 0

        while i <= j:
            mid = i + (j -i) // 2
            if mid * mid > x:
                j = mid - 1
            elif mid * mid < x:
                i = mid + 1
                res = mid
            else:
                return mid
        
        return res
