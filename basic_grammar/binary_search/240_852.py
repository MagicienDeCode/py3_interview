class Solution240:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for int_list in matrix:
            # if this line max element >= target
            if int_list[len(int_list)-1] >= target:
                res = self.binarySearch(int_list,target)
                if res != -1:
                    return True
        return False

    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

class Solution852:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while left + 1 < right:
            mid = left + (right - left) // 2
            # verify peak
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                left = mid
            else:
                right = mid
        # left right
        return left if nums[left] > nums[right] else right