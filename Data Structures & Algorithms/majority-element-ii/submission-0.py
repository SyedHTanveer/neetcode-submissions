class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        n = len(nums) // 3

        res = []

        for num in freq:
            if freq[num] > n:
                res.append(num)
        
        return res