from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0
        
        for i in range(n):
            if not visited[i]:
                count += 1
                queue = deque([i])
                
                while queue:
                    node = queue.popleft()
                    for j in range(n):
                        if isConnected[node][j] == 1 and not visited[j]:
                            visited[j] = True
                            queue.append(j)
        
        return count