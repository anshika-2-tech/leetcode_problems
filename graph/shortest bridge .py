from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        flag = False

        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            q.append((r, c))

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc)

        for i in range(n):
            if flag:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    flag = True
                    break

        ans = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return ans
                        
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            q.append((nx, ny))

            ans += 1