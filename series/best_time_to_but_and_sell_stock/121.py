class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the min value in list
        # find the max value which index > min_value_index
        m = prices[0]
        res = 0
        for p in prices[1:]:
            res = max(res, p-m)
            m = min(m,p)
        return res