class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    nbrs = deque([(r,c)])
                    islands += 1
                    while nbrs:
                        cr, cc = nbrs.popleft()
                        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                nbrs.append((nr, nc))
        return islands