from typing import List

class Solution35:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # if value equal to target, can return index as insert postion
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[left] >= target:
            return left
        if nums[right] >= target and target > nums[left]:
            return right
        return right + 1

class Solution74:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first, determine in which row, row[0] <= targat <= row[len-1] 
        row_index = self.rowBinarySearch(matrix,target)
        # if target is not in matrix, return False
        if row_index == -1:
            return False
        # use binary search template to find an index, if not found, return -1
        target_index = self.binarySearch(matrix[row_index],target)
        return False if target_index == -1 else True

    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1

    def rowBinarySearch(self, matrix: List[List[int]], target: int) -> int:
        left = 0
        right = len(matrix) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            # we compare the first element in each row with target
            if matrix[mid][0] == target:
                return mid
            elif matrix[mid][0] > target:
                right = mid
            else:
                left = mid
        # after while loop, we have two rows, matrix[left] and matrix[right], if target is not in these two rows, return -1
        if target < matrix[left][0] or target > matrix[right][len(matrix[0])-1]:
            return -1
        # since matrix are in non-decreasing order, verify target >= matrix[right][0], if not return left.
        if target >= matrix[right][0]:
            return right
        return left
    