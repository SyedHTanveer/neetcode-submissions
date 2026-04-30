class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # optimal solution is to have a hashmap
        # [0 ... 0] -> []
        # [1 ... 1] -> [[],[]]

        # so the key is the frequency of the letter,
        # the list is the words themselves
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())
