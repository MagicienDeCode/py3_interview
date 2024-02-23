from typing import List

x = 1
y = 2
# print max of x and y
print(max(x,y))
z = 3
print(max(x,y,z))

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list of numbers into a set for faster lookup
        nums_set = set(nums)
         # Initialize the result to store the longest consecutive sequence length
        res = 0
        # Iterate through each number in the list
        for n in nums:
            # Initialize count for the current consecutive sequence
            count = 1
            # Check if the next consecutive number is in the set
            plus = n + 1
            while plus in nums_set:
                # Remove the number from the set to avoid redundant counting
                nums_set.remove(plus)
                # Increment the count for consecutive numbers
                count += 1
                # Move to the next consecutive number
                plus += 1
            # Check if the previous consecutive number is in the set
            minus = n - 1
            while minus in nums_set:
                nums_set.remove(minus)
                count += 1
                minus -= 1
            # Update the result with the maximum count encountered so far
            res = max(res,count)
        # Return res
        return res