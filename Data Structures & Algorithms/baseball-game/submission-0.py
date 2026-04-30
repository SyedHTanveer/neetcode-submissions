class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        
        for i in range(len(operations)):
            if "+" == operations[i]:
               scores.append(scores[-1] + scores[-2])
            elif "D" == operations[i]:
                scores.append(2 * scores[-1])
            elif "C" == operations[i]:
                scores.pop()
            else:
                scores.append(int(operations[i]))    
        
        res = 0

        for i in range(len(scores)):
            res += scores[i]

        return res