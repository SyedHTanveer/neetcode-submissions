class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffLookup = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in diffLookup:
                return [diffLookup[diff], idx]
            diffLookup[num] = idx
            