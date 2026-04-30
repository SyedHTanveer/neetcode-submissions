class Solution:
    def isValid(self, s: str) -> bool:
        trackValid = deque()
        pairs = {
            '(': ')',
            '{' : '}',
            '[' : ']'
        }

        for c in s:
            if c in pairs:
                trackValid.append(c)
            else:
                if not trackValid:
                    return False
                validBracket = trackValid.pop()
                if pairs[validBracket] != c:
                    return False
        return len(trackValid) == 0
