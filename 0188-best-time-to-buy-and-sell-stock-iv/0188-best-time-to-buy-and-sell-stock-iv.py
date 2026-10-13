class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        # If k is large enough, the problem reduces to unlimited transactions
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))
        
        # dp[i][0]: max profit with at most i transactions, not holding stock
        # dp[i][1]: max profit with at most i transactions, holding stock
        dp = [[0, -prices[0]] for _ in range(k + 1)]
        
        for price in prices[1:]:
            for i in range(1, k + 1):
                dp[i][0] = max(dp[i][0], dp[i][1] + price)
                dp[i][1] = max(dp[i][1], dp[i-1][0] - price)
                
        return dp[k][0]