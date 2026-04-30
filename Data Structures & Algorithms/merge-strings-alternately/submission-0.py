class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = j = 0

        while i < len(word1) and j < len(word2):
            res = res + word1[i] + word2[j]
            i += 1
            j += 1
        
        if i == len(word1):
            res = res + word2[j:]
        else:
            res = res + word1[i:]
        return res

