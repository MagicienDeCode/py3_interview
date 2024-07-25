class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            m = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[m]: m = j
            if m != i:
                nums[m] = nums[m] ^ nums[i]
                nums[i] = nums[m] ^ nums[i]
                nums[m] = nums[m] ^ nums[i]
        return nums