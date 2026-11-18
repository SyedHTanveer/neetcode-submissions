class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}

        for n,m in zip(s,t):
            freq[n] = freq.get(n, 0) + 1
            freq[m] = freq.get(m, 0) - 1
        for count in freq:
            if freq[count] != 0:
                return False

        return True