# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # send my guess to the API, i get back -1 if its lower, 1 if its higher, 0 if im right
        l , r = 0 , n
        while True:
            myGuess = (r + l) // 2
            if guess(myGuess) == -1: 
                r = myGuess - 1
            elif guess(myGuess) == 1:
                l = myGuess + 1
            else: 
                return myGuess

