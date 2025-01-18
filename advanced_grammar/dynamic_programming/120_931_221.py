class Solution120:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1,len(triangle)):
            for c in range(0,r+1):
                v = triangle[r][c]
                if c == 0:
                    v += triangle[r-1][c]
                elif c == r:
                    v += triangle[r-1][c-1]
                else:
                    v += min(triangle[r-1][c],triangle[r-1][c-1])
                triangle[r][c] = v
        return min(triangle[-1])

class Solution931:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(0,len(matrix)):
                v = matrix[i][j]
                if j == 0:
                    v += min(matrix[i-1][j],matrix[i-1][j+1])
                elif j == len(matrix)-1:
                    v += min(matrix[i-1][j-1],matrix[i-1][j])
                else:
                    v += min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])
                matrix[i][j] = v
        return min(matrix[-1])

class Solution221:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        v = 0
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
                    v = max(v,dp[i][j])
        return v*v