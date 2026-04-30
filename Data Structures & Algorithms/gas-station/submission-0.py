class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost or len (gas) != len(cost):
            return -1

        start = tank = total = 0

        for i in range(len(gas)):
            
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            

            if tank < 0:
                start = i + 1
                tank = 0
                
        return start if total >= 0 else -1
