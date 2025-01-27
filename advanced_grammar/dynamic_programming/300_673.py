class Solution300:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [1,3,6,7,9,4,10,5,6]
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

class Solution673:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j] + 1:
                        count[i] += count[j]
                    if dp[i] <= dp[j]: 
                        count[i] = count[j]
                    dp[i] = max(dp[i],dp[j]+1)
                    
        lis = max(dp)
        res = 0
        for i in range(len(count)):
            if dp[i] == lis:
                res += count[i]
        return res