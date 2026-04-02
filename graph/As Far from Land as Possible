from collections import deque

class Solution:
    def maxDistance(self, grid):
        n = len(grid)
        queue = deque()

        # Step 1: push all land cells
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        # Edge case
        if not queue or len(queue) == n * n:
            return -1

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        distance = -1

        # Step 2: BFS
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        queue.append((nx, ny))
            distance += 1

        return distance