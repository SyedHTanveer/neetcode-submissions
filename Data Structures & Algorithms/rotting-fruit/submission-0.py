class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        
        q = deque()
        count = 0
        fresh = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r , c))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while fresh > 0 and q:
            for i in range(len(q)):
                r , c = q.popleft()
                for dr, dc in directions:
                    nr , nc = r + dr, c + dc
                    if (nr in range(row)) and (nc in range(col)) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            count += 1
        return count if fresh == 0 else -1