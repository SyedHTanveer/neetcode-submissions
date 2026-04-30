class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    queue = deque([(r,c)])
                    while queue:
                        cr, cc = queue.popleft()
                        grid[cr][cc] = "0"
                        for dr, dc in neighbors:
                            nr, nc = dr + cr, dc + cc
                            if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1":
                                queue.append((nr,nc))
                    islands += 1
        
        return islands