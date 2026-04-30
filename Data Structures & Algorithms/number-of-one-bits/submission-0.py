class Solution:
    def hammingWeight(self, n: int) -> int:
        
        n = bin(n)[2:]

        countOnes = 0

        for i in range(len(n)):

            if n[i] == '1':
                countOnes += 1

        return countOnes