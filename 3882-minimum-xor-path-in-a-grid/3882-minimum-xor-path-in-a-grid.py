class Solution:

  def minCost(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # dp[i][j] stores all possible XOR path values to reach cell (i, j)
    dp = [[set() for _ in range(n)] for _ in range(m)]
    dp[0][0].add(grid[0][0])

    for i in range(m):
      for j in range(n):
        current_xors = dp[i][j]
        if not current_xors:
          continue

        # Move right
        if j + 1 < n:
          right_val = grid[i][j + 1]
          for x in current_xors:
            dp[i][j + 1].add(x ^ right_val)

        # Move down
        if i + 1 < m:
          down_val = grid[i + 1][j]
          for x in current_xors:
            dp[i + 1][j].add(x ^ down_val)

    return min(dp[m - 1][n - 1])