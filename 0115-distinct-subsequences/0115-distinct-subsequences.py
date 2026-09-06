class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        # dp[j] stores the number of subsequences of s that match t[:j]
        dp = [1] + [0] * n
        
        for char in s:
            # Traverse backwards to ensure we use the previous character's DP state
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]