from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        heap = [(0, src, 0)]
        dist = dict()
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            if (node, stops) in dist and dist[(node, stops)] <= cost:
                continue
            
            dist[(node, stops)] = cost
            
            for nei, price in graph[node]:
                heapq.heappush(heap, (cost + price, nei, stops + 1))
        
        return -1