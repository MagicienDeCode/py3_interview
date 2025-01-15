class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * 10001
        maxv = 0
        for n in nums:
            maxv = max(maxv,n)
            dp[n]+=1
        for i in range(2,maxv+1):
            dp[i] = max(dp[i-1],dp[i-2] + dp[i]*i)
        return dp[maxv]