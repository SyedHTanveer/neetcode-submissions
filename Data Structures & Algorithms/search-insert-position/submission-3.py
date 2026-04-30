class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if nums[n-1] < target:
            return n

        l, r = 0 , len(nums) - 1

        while l <= r:
            mid = (l + r) // 2 
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                n = mid
                r = mid - 1
            else:
                l = mid + 1
        return n