class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()
            
        return newStr == newStr[::-1]

        # left = 0
        # right = len(s) - 1

        # while left != right:
        #     if s[left].isalpha() and s[right].isalpha():
        #         if s[left] != s[right]:
        #             return False
        #         left += 1 
        #         right -= 1
        #     if s[left].isalpha() == False:
        #         left += 1 
        #     if s[right].isalpha() == False:
        #         right -= 1    
        
        # return True