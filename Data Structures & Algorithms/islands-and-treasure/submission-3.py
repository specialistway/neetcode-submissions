from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        n, m = len(grid), len(grid[0])
        q = deque()
        
        # 1. 将所有宝藏(0)加入队列
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        # 2. 多源BFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 只在未访问的水域(INF)上更新
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))