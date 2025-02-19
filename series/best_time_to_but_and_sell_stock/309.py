class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cd = [0]*n
        b = [0]*n
        s = [0]*n
        b[0] = -prices[0]
        for i in range(1,n):
            b[i] = max(b[i-1],cd[i-1]-prices[i])
            s[i] = max(s[i-1],b[i-1]+prices[i])
            cd[i] = max(cd[i-1],s[i-1])
        return max(s[-1],cd[-1])