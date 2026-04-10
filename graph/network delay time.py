from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        
        heap = [(0, k)]
        
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            
            for nei, w in graph[node]:
                if dist[nei] > d + w:
                    dist[nei] = d + w
                    heapq.heappush(heap, (dist[nei], nei))
        
        res = max(dist.values())
        return res if res != float('inf') else -1