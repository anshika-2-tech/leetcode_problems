from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g= defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        q= deque[(source)]
        visit= set()
        while(q):
            x= q.popleft()
            if x== destination:
                return True
            visit.add(x)
            for i in g[x]:
                q.append(i)
        return False
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        q = deque([source])
        visit = set()
        while q:
            x = q.popleft()
            if x == destination:
                return True
            visit.add(x)
            for i in g[x]:
                if i not in visit:
                  
                    q.append(i)

        return False

        