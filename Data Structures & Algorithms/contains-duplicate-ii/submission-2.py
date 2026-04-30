class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashNums = {}

        for idx, num in enumerate(nums):
            if num in hashNums and idx - hashNums[num] <= k:
                    return True
            else:
                hashNums[num] = idx

        return False