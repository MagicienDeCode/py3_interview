class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.isValid(mid,piles,h):
                right = mid
            else:
                left = mid
        # left right
        if self.isValid(left,piles,h):
            return left
        return right

    """
    [3,6,7,11] h=8 target=5
    3  > 5       ==> 1
    6  > 5 5     ==> 2
    7  > 5 5     ==> 2
    11 > 5 5 5   ==> 3
               sum = 8
    """
    def isValid(self, target:int ,piles: List[int], h: int) -> bool:
        count = 0
        for i in piles:
            count += i // target + (0 if i%target==0 else 1)
        return count <= h
        