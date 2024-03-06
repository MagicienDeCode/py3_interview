class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m * n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.count(m,n,mid) >= k:
                right = mid
            else:
                left = mid
        # left right
        if self.count(m,n,left) >= k:
            return left
        return right

    def count(self, m: int, n: int, mid: int) -> int:
        result = 0
        for i in range(1,m+1):
            result += min(n, (mid // i))
        return result