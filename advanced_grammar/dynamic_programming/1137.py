class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        if n == 2: return 1
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
    """
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        if n == 2: return 1
        t0 = 0
        t1 = 1
        t2 = 1
        for _ in range(3,n+1):
            pt2 = t2
            t2 += t0 + t1
            t0 = t1
            t1 = pt2
        return t2
    """
            