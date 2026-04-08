from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands in a 2D grid.
        An island is formed by connecting adjacent lands ('1') horizontally or vertically.
      
        Args:
            grid: 2D grid of '1's (land) and '0's (water)
      
        Returns:
            Number of islands in the grid
        """
      
        def dfs(row: int, col: int) -> None:
            """
            Depth-first search to mark all connected land cells as visited.
            Modifies the grid in-place by changing '1' to '0'.
          
            Args:
                row: Current row index
                col: Current column index
            """
         
            grid[row][col] = '0'
          
            
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_row, next_col = row + dr, col + dc
              

                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    grid[next_row][next_col] == '1'):
                   
                    dfs(next_row, next_col)
      
       
        island_count = 0
      
      
        rows, cols = len(grid), len(grid[0])
      
   
        for i in range(rows):
            for j in range(cols):
             
                if grid[i][j] == '1':
                    
                    dfs(i, j)
                
                    island_count += 1
      
        return island_count
