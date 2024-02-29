class Solution34:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        return [self.bsFirstIndex(nums,target),self.bsLastIndex(nums,target)]
    
    def bsFirstIndex(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
            """
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
            """
        # verify left or right
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

    def bsLastIndex(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
            """
            if nums[mid] > target:
                right = mid
            else:
                left = mid
            """
        # verify left or right
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

"""
V V V V V V V [X] X X   X   X
1 2 3 4 5 6 7 8   9 10  11  12

V isBadVersion False
X isBadVersion True
"""

class Solution278:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        # verify left or right
        if isBadVersion(left):
            return left
        return right
