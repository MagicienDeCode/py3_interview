class Solution1218:
    def longestSubsequence(self, nums: List[int], difference: int) -> int:
        diffdp = {nums[0]:1}
        for i in range(1,len(nums)):
            pre = nums[i] - difference
            diffdp[nums[i]]= diffdp.get(pre,0) + 1
        return max(diffdp.values())

class Solution1027:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        res = 2
        diffdp = [{} for _ in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                diffdp[i][diff] = diffdp[j].get(diff,1) + 1
                res = max(diffdp[i][diff],res)
        return res