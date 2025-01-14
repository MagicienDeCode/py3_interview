class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost.copy()
        dp.append(0)
        for i in range(2,len(dp)):
            dp[i] += min(dp[i-2],dp[i-1])
        return dp[len(cost)]