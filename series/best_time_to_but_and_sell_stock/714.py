class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        b = -prices[0]
        s = 0
        for p in prices[1:]:
            b = max(b, s-p)
            s = max(s,b+p-fee)
        return s