class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        res = []

        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[v].append(u)
            inDegree[u] += 1

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for next in adj[curr]:
                inDegree[next] -= 1
                if inDegree[next] == 0:
                    queue.append(next)
        
        if len(res) == numCourses: return res
        else: return []