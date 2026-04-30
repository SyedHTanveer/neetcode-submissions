class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        nei = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()

        freshFruit = 0
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshFruit += 1
    
        while freshFruit > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()    
                for dr, dc in nei:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        freshFruit -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            time += 1
        return time if freshFruit == 0 else -1