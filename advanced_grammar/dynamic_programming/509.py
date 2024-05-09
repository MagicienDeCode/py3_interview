class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        f0 = 0
        f1 = 1
        for _ in range(1,n):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return f1

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

class Solution:
    """
    F4 = F3 + F2
    F3 = F2 + F1
    """
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        self.dp = [-1] * (n+1)
        self.dp[0] = 0
        self.dp[1] = 1
        return self.dfs(n)

    def dfs(self, n:int) -> int:
        if self.dp[n] != -1:
            return self.dp[n]
        self.dp[n] = self.dfs(n-1) + self.dfs(n-2)
        return self.dp[n]