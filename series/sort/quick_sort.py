class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums,0,len(nums)-1)
        return nums
    
    def quickSort(self,nums,start,end):
        if start >= end: return
        pivot = nums[start + (end-start)//2]
        print(pivot)
        left = start
        right = end
        while left <= right:
            while left <= right and nums[left] < pivot: left += 1
            while left <= right and nums[right] > pivot: right -= 1
            if left <= right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        self.quickSort(nums,start,right)
        self.quickSort(nums,left,end)
