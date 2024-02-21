from typing import List

nums = [1,2,3,4]

# Iterate through the range from len(nums)-1 to 0 (inclusive), in reverse order.

    # Print the current index i and the value at index i in the nums list.


print("=====================")
# Iterate through the range from len(nums)-1 to 0 (inclusive), with a step of -2.

    # Print the current index i and the value at index i in the nums list.


"""
input [1,2,3,4]
output[24,12,8,6]

main idea: calculate prefix and suffix product,
then for index i, result[i] = prefix[i-1] * suffix[i+1]

prefix_products = [1,2,6,24]
suffix_products = [24,24,12,4]
result[0] = suffix_products[1] = 24
result[1] = prefix_products[0] * suffix_products[2] = 1 * 12 = 12
result[2] = prefix_products[1] * suffix_products[3] = 2 * 4 = 8
result[3] = prefix_products[2] = 6
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize prefix_products and suffix_products arrays with 1s.

        # Set the first element of prefix_products to the first element of nums.

        # Set the last element of suffix_products to the last element of nums.

        # Compute prefix products.

        # Compute suffix products.

        # Initialize result array with 1s.

        # Set the first element of result using suffix_products[1].

        # Set the last element of result using prefix_products[len(nums)-2].

        # Compute the product except self for the rest of the elements.
        return []


"""
[1,2,3,4]
[24,12,8,6]

main idea, calculate prefix into result,
then calculate suffix then directly multiply prefix in result
prefix_products = [1,2,6,24]
suffix_products = [24,24,12,4]
resut [1, 1, 1, 1]
pre   [1, 1, 2, 6]
suf   [24,12,4, 1]

		 [1,2,3,4]
result = [1,1,2,6]
suffix = 1

result[i] = result[i] * suffix
suffix = suffix * nums[i]
i -= 1

i = 3, result[3] = 6 * 1 = 6
suffix = 1 * 4

i = 2, result[2] = 2 * 4 = 8
suffix = 4 * 3 = 12

i = 1, result[1] = 1 * 12 = 12
suffix = 12 * 2 = 24

i = 0, result[0] = 1 * 24 = 24
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    	return []