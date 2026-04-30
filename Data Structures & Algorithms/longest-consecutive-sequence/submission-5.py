class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # novel approach - sort, track a consec #, 
        # set a prev #, see if prev is only 1 less than curr?
            # add 1 to consec
            # otherwise continue
        # return conrec

        res = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in nums:
                length = 0
                while n + length in nums:
                    length += 1
                longest = max(length, longest)
        return longest