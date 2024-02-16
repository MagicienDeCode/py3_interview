from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through each element in the list
        for i in range(len(nums)):
            # Iterate through the remaining elements in the list
            for j in range(i+1, len(nums)):
                # Check if the sum of the current pair equals the target
                if nums[i] + nums[j] == target:
                    # If it does, return the indices of the two numbers
                    return [i, j]
        
        # If no such pair is found, return an empty list
        return []

# Example usage of the Solution class
solution_instance = Solution()

# Example input values
nums = [2, 7, 11, 15]
target = 9

# Call the twoSum function on the instance
result = solution_instance.twoSum(nums, target)

# Print the result
print(result)