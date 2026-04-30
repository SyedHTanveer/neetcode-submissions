class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        twoSumsHash = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in twoSumsHash:
                return [twoSumsHash[diff], i]
            
            twoSumsHash[n] = i

        return False