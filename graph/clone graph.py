from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        visited = {}  
        
        def dfs(curr):

            if curr in visited:
                return visited[curr]
            
            
            copy = Node(curr.val)
            visited[curr] = copy
            
    
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)