class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         numdict = set()

         for n in nums:
            if n in numdict:
                return True
            else:
                numdict.add(n)
        
         return False