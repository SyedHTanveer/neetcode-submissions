class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sAnagram = {}
        tAnagram = {}

        for c in s:
            if c in sAnagram:
                sAnagram[c] += 1
            else:
                sAnagram[c] = 1

        for c in t:
            if c in tAnagram:
                tAnagram[c] += 1
            else:
                tAnagram[c] = 1

        return sAnagram == tAnagram