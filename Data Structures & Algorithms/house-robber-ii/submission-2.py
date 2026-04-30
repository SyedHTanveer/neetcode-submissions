class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def rob(arr):
            r1, r2 = 0, 0
            for n in arr:
                r1, r2 = r2, max(n + r1, r2)
            return r2
        
        return max(rob(nums[:-1]), rob(nums[1:]))
