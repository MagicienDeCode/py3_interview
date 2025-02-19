class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -prices[0]
        sell1 = 0
        buy2 = buy1
        sel2 = 0
        for p in prices[1:]:
            buy1 = max(buy1,-p)
            sell1 = max(sell1,buy1+p)
            buy2 = max(buy2,sell1-p)
            sel2 = max(sel2,buy2+p)
        return sel2