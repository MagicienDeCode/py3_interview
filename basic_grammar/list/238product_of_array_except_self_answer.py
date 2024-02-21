from typing import List

nums = [1,2,3,4]

for i in range(len(nums)):
	print(i,nums[i])

print("=====================")

for i,v in enumerate(nums):
	print(i,v)

print("=====================")

# Iterate through the range from len(nums)-1 to 0 (inclusive), in reverse order.
for i in range(len(nums)-1, -1, -1):
    # Print the current index i and the value at index i in the nums list.
    print(i, nums[i])

print("=====================")
for i in range(len(nums)-1, -1, -2):
	print(i, nums[i])

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
        prefix_products = [1] * len(nums)
        suffix_products = [1] * len(nums)
        # Set the first element of prefix_products to the first element of nums.
        prefix_products[0] = nums[0]
        # Set the last element of suffix_products to the last element of nums.
        suffix_products[len(nums)-1] = nums[len(nums)-1]
        # Compute prefix products.
        for i in range(1, len(nums)):
            prefix_products[i] = prefix_products[i-1] * nums[i]
        # Compute suffix products.
        for i in range(len(nums)-2, -1, -1):
            suffix_products[i] = suffix_products[i+1] * nums[i]
        # Initialize result array with 1s.
        result = [1] * len(nums)
        # Set the first element of result using suffix_products[1].
        result[0] = suffix_products[1]
        # Set the last element of result using prefix_products[len(nums)-2].
        result[len(nums)-1] = prefix_products[len(nums)-2]
        # Compute the product except self for the rest of the elements.
        for i in range(1, len(nums)-1):
            result[i] = prefix_products[i-1] * suffix_products[i+1]
        return result


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
    	result = [1] * len(nums)
    	prefix = 1
    	for i in range(len(nums)):
    		result[i] = prefix
    		prefix *= nums[i]
    	suffix = 1
    	for i in range(len(nums)-1,-1,-1):
    		result[i] *= suffix
    		suffix *= nums[i]
    	return result