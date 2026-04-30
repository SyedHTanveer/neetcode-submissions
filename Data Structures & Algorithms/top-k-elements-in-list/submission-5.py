class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        kFreq = {}
        
        for n in nums:
            kFreq[n] = kFreq.get(n, 0) + 1
        
        print(kFreq)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in kFreq.items():
            bucket[freq].append(num)

        print(bucket)
        res = []

        for i in range(len(bucket) - 1, 0 , -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        return res