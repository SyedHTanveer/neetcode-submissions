class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        close_to_open = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in close_to_open:
                # Check if stack is empty or top doesn't match
                if not stack or stack.pop() != close_to_open[c]:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(c)

        return len(stack) == 0