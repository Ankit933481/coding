class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Optimization: A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
            
        from functools import cache

        @cache
        def dfs(r: int, c: int, balance: int) -> bool:
            # Update balance for current cell
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1
                
            # If balance drops below 0, this path is invalid
            if balance < 0:
                return False
                
            # If we reached the bottom-right corner
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            # Try moving down
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
                
            # Try moving right
            if c + 1 < n and dfs(r, c + 1, balance):
                return True
                
            return False

        return dfs(0, 0, 0)