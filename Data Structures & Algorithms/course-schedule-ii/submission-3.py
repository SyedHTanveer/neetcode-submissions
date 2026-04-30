class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0] * numCourses
        adj = defaultdict(list)

        for src , dst in prerequisites:
            adj[dst].append(src)
            indegree[src] += 1
        
        queue = deque()

        for idx, n in enumerate(indegree):
            if n == 0:
                queue.append(idx)
    
        res = []
        finish = 0
        while queue:
            node = queue.popleft()
            res.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if finish != numCourses:
            return []
        return res

