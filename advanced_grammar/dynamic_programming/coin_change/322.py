class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if c > i: break
                dp[i] = min(dp[i],dp[i-c]+1)
        if dp[amount] > amount: return -1
        return dp[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i],dp[i-c]+1)
        if dp[amount] > amount: return -1
        return dp[amount]