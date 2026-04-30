class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if we sort every character its nlogn * m

        # count the chars instead, use a hashmap. o(m [the input string given] * n[length of string])

        res = defaultdict(list) # mapping the char count of each string to the list of anograms

        for s in strs:
            count = [0] * 26 # a ... z - good point on edge case question (is it upper or lower)

            for c in s:
                count[ord(c) - ord("a")] += 1 # this is so we map to 0-26 not 80 to 106
            res[tuple(count)].append(s)

        return list(res.values()) #just return the values grouped. need to cast to list