class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temps = nums.copy()
        self.mergeSort(nums,temps,0,len(nums)-1)
        return nums
    
    def mergeSort(self,nums,temps,start,end):
        if start >= end: return
        mid = start + (end-start)//2
        self.mergeSort(nums,temps,start,mid)
        self.mergeSort(nums,temps,mid+1,end)
        self.merge(nums,temps,start,end)
    
    def merge(self,nums,temps,start,end):
        mid = start + (end-start)//2
        left = start
        right = mid+1
        i = start
        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                temps[i] = nums[left]
                i+=1
                left+=1
            else:
                temps[i] = nums[right]
                i+=1
                right+=1
        while left <= mid:
            temps[i] = nums[left]
            i+=1
            left+=1
        while right <= end:
            temps[i] = nums[right]
            i+=1
            right+=1
        for i in range(start,end+1):
            nums[i] = temps[i]
