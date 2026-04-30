class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # res = set()

        # for i in range(len(nums)):
        #     if nums[i] in res:
        #         return True
        #     res.add(nums[i])

        # return False

        return len(set(nums)) < len(nums)