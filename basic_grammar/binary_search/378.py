class Solution378:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # minimal element in matrix
        left = matrix[0][0]
        # maximal element in matrix
        right = matrix[n-1][n-1]
        while left + 1 < right:
            mid = left + (right - left) // 2
            # count how many element <= mid
            if self.count(mid,matrix) >= k:
                right = mid
            else:
                left = mid
        # left right
        # if left satisfy condition, return left, exmaple [[1,2],[1,3]] k=1
        if self.count(left,matrix) >= k:
            return left
        return right

    def count(self, target: int,matrix: List[List[int]]) -> int:
        result = 0
        for i in matrix:
            # binary search how many element in this row <= target
            result += self.bsCountRow(target,i)
            """
            for j in i:
                if j <= target:
                    result += 1
            """
        return result
    
    # count how many elements <= target
    def bsCountRow(self, target: int, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        # left right
        # index from 0, so if nums[7] <= target, this row has 8 elements <= target
        if nums[right] <= target:
            return right + 1
        if nums[left] <= target:
            return right
        return left