class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        tracker = []

        for c in s:
            if c in pair:
                if tracker and tracker[-1] == pair[c]:
                    tracker.pop()
                else:
                    return False
            else:
                tracker.append(c)    
                
        return True if not tracker else False