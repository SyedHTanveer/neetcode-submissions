class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # sliding window
        charSet = set()
        l = 0
        res = 0
        # go through s
        for r in range(len(s)):
            # while charSet contains s[r]:
            while s[r] in charSet:
                # remove the char
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res