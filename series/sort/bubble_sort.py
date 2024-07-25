class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(0,len(nums)-1-i):
                if nums[j] > nums[j+1]:
                    nums[j] = nums[j] ^ nums[j+1]
                    nums[j+1] = nums[j] ^ nums[j+1]
                    nums[j] = nums[j] ^ nums[j+1]
        return nums