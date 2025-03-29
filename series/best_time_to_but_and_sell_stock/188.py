class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        
        n = len(prices)
        if k * 2 >= n:
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
        
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        
        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]
        """
        dp[i][j][0] doesn't have stock
        dp[i-1][j][1] + prices[i] today sell stock
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])

        dp[i][j][1] have stock
        dp[i-1][j-1][0] - prices[i] today buy stock
        dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        """
        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        
        return dp[n-1][k][0]