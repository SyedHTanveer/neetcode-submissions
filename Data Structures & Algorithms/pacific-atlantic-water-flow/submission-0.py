class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0]) 

        def bfs(starts, ocean):
            nei = [(1,0),(-1,0),(0,1),(0,-1)]
            q = deque(starts)
            while q:
                r,c = q.popleft()
                ocean.add((r,c))
                for dr, dc in nei:
                    nr, nc = dr + r, dc + c
                    if (nr,nc) not in ocean and nr in range(ROWS) and nc in range(COLS) and heights[r][c] <= heights[nr][nc]:
                        q.append((nr,nc))
    
        pac, atl = set(), set()

        bfs([(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)], pac)
        bfs([(ROWS-1, c) for c in range(COLS)] + [(r, COLS-1) for r in range(ROWS)], atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and  (r,c) in pac:
                    res.append((r,c))
        
        return res