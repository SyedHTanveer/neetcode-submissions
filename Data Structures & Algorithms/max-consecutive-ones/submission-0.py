class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_ones = 0
        curr_one = 0

        for num in nums:
            if num == 0:
                consecutive_ones = max(curr_one, consecutive_ones)
                curr_one = 0
                continue
            curr_one += 1
            
        consecutive_ones = max(curr_one, consecutive_ones)
        return consecutive_ones