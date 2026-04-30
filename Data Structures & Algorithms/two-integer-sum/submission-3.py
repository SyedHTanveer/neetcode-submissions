class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        twoSumsHash = {}

        for i in range(len(nums)):
            twoSumsHash[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in twoSumsHash and twoSumsHash[diff] != i:
                return [i, twoSumsHash[diff]]
        return False