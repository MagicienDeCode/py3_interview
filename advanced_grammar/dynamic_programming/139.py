class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wset = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in wset:
                    dp[i] = True
                    break
        return dp[-1]