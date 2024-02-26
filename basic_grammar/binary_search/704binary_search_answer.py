from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # assign min index to left
        left = 0
        # assign max index to right
        right = len(nums) - 1
        # while loop
        while left + 1 < right:
            # calculate mid index
            mid = left + (right - left) // 2
            # compare value at mid index with target
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        # verify if value at right index satisfy condition
        if nums[right] == target:
            return right
        # verify if value at left index satisfy condition
        elif nums[left] == target:
            return left
        # if both are unsatisfied, return default value
        return -1

solution = Solution()
print(solution.search([-1,0,3,5,9,12],9))


