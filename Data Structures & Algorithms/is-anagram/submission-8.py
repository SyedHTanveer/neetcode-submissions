class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for x,y in zip(s, t):
            dict1[x] += 1
            dict2[y] += 1

        return dict1 == dict2