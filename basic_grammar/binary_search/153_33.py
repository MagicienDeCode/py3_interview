class Solution153:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[0]:
                left = mid
            else:
                right = mid
        return min(nums[left],nums[right])

class Solution33:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # if mid index in left up
            if nums[mid] > nums[0]:
                if nums[mid] > target and target >= nums[left]:
                    right = mid
                else:
                    left = mid
            # if mid index in right bottom
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1