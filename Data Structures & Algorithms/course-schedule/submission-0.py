class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for  src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1

        queue = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        finish = 0

        while queue:
            curr = queue.popleft()
            finish += 1
            for next in adj[curr]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)
        
        return finish == numCourses