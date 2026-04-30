class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen  = {')': '(', '}': '{', ']': '['}
        
        for char in s: # interate through s
            if char in closeToOpen: # what were doing here is checking if its a closing one
                if stack and stack[-1] == closeToOpen[char]: # see if the head of the stack is a open one
                    stack.pop() # take it out
                else:
                    return False # if its not matching, then return flase
            else: 
                stack.append(char)

        return True if not stack else False
