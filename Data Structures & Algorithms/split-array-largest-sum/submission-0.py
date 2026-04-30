class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l < r:
            
            mid = (l + r) // 2
            subarray = 1
            running_sum = 0
            for i in range(len(nums)):
                running_sum += nums[i]
                if running_sum > mid:
                    subarray += 1
                    running_sum = nums[i]
            if subarray <= k:
                r = mid
            else:
                l = mid + 1
        
        return r