class Solution5:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for _ in range(len(s))]
        res = s[0]
        for i in range(len(s)): dp[i][i] = 1
        for i in range(len(s)-1,-1,-1): 
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    if j-1==i or dp[i+1][j-1]>=1:
                        dp[i][j] = 2 + dp[i+1][j-1]
                        if j-i+1 > len(res):
                            res = s[i:j+1]
        # for i in dp: print(i)
        return res

class Solution516:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)): dp[i][i] = 1
        for i in range(len(s)-1,-1,-1): 
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i + 1][j])
        #for i in dp: print(i)
        return dp[0][-1]