class Solution1035:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1) + 1
        n = len(nums2) + 1
        dp = [[0]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[m-1][n-1]

class Solution1143:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1
        dp = [[0]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[m-1][n-1]