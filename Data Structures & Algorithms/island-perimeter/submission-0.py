class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS, perimeter = len(grid), len(grid[0]), 0

        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for dr, dc in neighbors:
                        nr, nc = dr + r, dc + c
                        if 0 > nr or 0 > nc or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                            perimeter += 1
        return perimeter