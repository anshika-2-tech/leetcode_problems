from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n, edges, t, target):
        graph = defaultdict(list)
        
        # Build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque([(1, 1.0, 0)])  # (node, probability, time)
        visited.add(1)
        
        while queue:
            node, prob, time = queue.popleft()
            
            # If time reached
            if time == t:
                if node == target:
                    return prob
                continue
            
            # Count unvisited neighbors
            unvisited = []
            for nei in graph[node]:
                if nei not in visited:
                    unvisited.append(nei)
            
            # If no unvisited neighbors
            if not unvisited:
                if node == target:
                    return prob
                continue
            
            # Move to neighbors
            for nei in unvisited:
                visited.add(nei)
                queue.append((nei, prob / len(unvisited), time + 1))
        
        return 0.0