class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]

        if n == 0:
            return 0
        if n == 1:
            return res
        else:
            maxSub = nums[0]
            cur = 0

            for n in nums:
                if cur < 0:
                    cur = 0
                cur += n
                maxSub = max(maxSub, cur)
            return maxSub
            # for i in range(1, n):
            #     cur = 0
            #     for j in range (i+1,n):
            #         cur += nums[j]
            #         res = max(res,cur)
            # return res