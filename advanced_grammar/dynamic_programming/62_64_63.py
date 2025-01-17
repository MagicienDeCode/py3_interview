class Solution62:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]

class Solution64:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[40001]*(n+1) for _ in range(m+1)]
        dp[0][1] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i][j-1],dp[i-1][j])
        return dp[m][n]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1] == 1: dp[i][j] == 0
                else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]