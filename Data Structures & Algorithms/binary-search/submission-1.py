class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0 , len(nums) - 1

        while i <= j:
            mid = (j + i) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1 
        return -1