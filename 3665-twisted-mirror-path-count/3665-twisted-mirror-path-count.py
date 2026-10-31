class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        # memo[r][c][dir] stores the landing cell (r', c') or (-1, -1)
        memo = [[[None, None] for _ in range(n)] for _ in range(m)]
        
        def get_jump(r, c, dir):
            if memo[r][c][dir] is not None:
                return memo[r][c][dir]
            
            # Initial step into the grid based on direction
            if dir == 0:
                curr_r, curr_c = r, c + 1
            else:
                curr_r, curr_c = r + 1, c
                
            curr_dir = dir
            vis = set()
            res = (-1, -1)
            
            while True:
                if not (0 <= curr_r < m and 0 <= curr_c < n):
                    res = (-1, -1)
                    break
                
                state = (curr_r, curr_c, curr_dir)
                if state in vis:
                    res = (-1, -1)
                    break
                vis.add(state)
                
                if grid[curr_r][curr_c] == 0:
                    # Landed on an empty cell
                    res = (curr_r, curr_c)
                    break
                else:
                    # Hit a mirror cell, reflect immediately
                    if curr_dir == 0:
                        curr_r, curr_c, curr_dir = curr_r + 1, curr_c, 1
                    else:
                        curr_r, curr_c, curr_dir = curr_r, curr_c + 1, 0
            
            memo[r][c][dir] = res
            return res

        # DP table: dp[i][j] = number of ways to reach (i, j)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue
                
                # Try moving right (dir = 0)
                nxt_r, nxt_c = get_jump(i, j, 0)
                if nxt_r != -1:
                    dp[nxt_r][nxt_c] = (dp[nxt_r][nxt_c] + dp[i][j]) % MOD
                    
                # Try moving down (dir = 1)
                nxt_r, nxt_c = get_jump(i, j, 1)
                if nxt_r != -1:
                    dp[nxt_r][nxt_c] = (dp[nxt_r][nxt_c] + dp[i][j]) % MOD
                    
        return dp[m - 1][n - 1]