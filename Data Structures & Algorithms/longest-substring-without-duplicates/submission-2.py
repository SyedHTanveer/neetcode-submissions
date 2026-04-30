class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can do a set since set's only contain uniques

        # then run through the list and see

        # a couple of ways actually
        # brut force would be to go through all the strings and find the string
        # that is currently the longest and then compare that to every other substring
        # this would be o(n*2) though and not so optimal

        # next we could use a set here since sets contain all uniques and return
        # the sets length

        # well we cant just do a set and return it, we need to figure out how
        # to reset the set if there exists a longer substring, this runs into a
        # space complexity problem

        # we could do a hashset?
        # we go through the list and find all the substrings add to hashset
        # then go through hashset and find the longest substring
        # lets try this


        # hash_subset = set()

        # for c in s:
        #     if c not in hash_subset:
        #         hash_subset.add(c)
        
        # return len(hash_subset)

        # the above will only give you a length of all the unique chars not a unique substring

        charSet = set()

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res