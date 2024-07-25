class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            p = i - 1
            current = nums[i]
            while p >=0 and nums[p] >current:
                nums[p+1] = nums[p]
                p-=1
            nums[p+1] = current
        return nums