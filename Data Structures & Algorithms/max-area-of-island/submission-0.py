class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxA = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    queue = [(r, c)]
                    area = 0
                    grid[r][c] = 0
                    while queue:
                        node = queue.pop()
                        area += 1
                        rr, cc = node[0], node[1]
                        for dr, dc in [(1,0), (-1,0), (0, 1), (0, -1)]:
                            nr, nc = rr + dr, cc + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                queue.append((nr, nc)) 
                    maxA = max(maxA, area)
        return maxA