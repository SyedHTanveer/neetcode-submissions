class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force: go through the list, if i-th is
        # less than i - 1, then you found the cliff

    # we could take the first element and compare to last element
    # if first is < last, then you found the start return first
    # else
    # we can use the first as a compare, find the midpoint,
    # see if the midpoint is < or > than the first, if its 
    # greater than the first, then treverse the right side and find the min
    # else:
    # look in the left, find the min.
    # return the min
        if nums[0] <= nums[len(nums)-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


