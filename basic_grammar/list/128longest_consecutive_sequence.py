from typing import List

x = 1
y = 2
# print max of x and y

z = 3
# print max of x,y,z


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list of numbers into a set for faster lookup

         # Initialize the result to store the longest consecutive sequence length

        # Iterate through each number in the list

            # Initialize count for the current consecutive sequence

            # Check if the next consecutive number is in the set


                # Remove the number from the set to avoid redundant counting

                # Increment the count for consecutive numbers

                # Move to the next consecutive number

            # Check if the previous consecutive number is in the set

            # Update the result with the maximum count encountered so far

        # Return res
        return 0