class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = idx - stackI
            stack.append((temp, idx))
        return res