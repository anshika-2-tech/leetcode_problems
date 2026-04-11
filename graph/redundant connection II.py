from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        cand1 = []
        cand2 = []
        
        for u, v in edges:
            if v in parent:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break
            parent[v] = u
        
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            uf[py] = px
            return True
        
        uf = list(range(len(edges) + 1))
        
        for u, v in edges:
            if [u, v] == cand2:
                continue
            if not union(u, v):
                if cand1:
                    return cand1
                return [u, v]
        
        return cand2