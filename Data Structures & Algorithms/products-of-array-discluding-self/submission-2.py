class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force: go through each number, go through j
        # if i == j, skip, i = i * j
        res = [1 for _ in range(len(nums))]
        postfix = 1

        for i in range(1,len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        
        for i in range(len(nums) - 2, -1 , -1):
            postfix = nums[i + 1] * postfix
            res[i] = postfix * res[i]
        return res