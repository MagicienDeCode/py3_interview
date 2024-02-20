# Import necessary modules
from typing import List
from collections import Counter

# Define a list of numbers
nums = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]

# Loop through the list with indexes and values, and print them
for i, v in enumerate(nums):
    print(i, v)

print("==========================================================")
# Loop through the list with indexes and values, and print them
for v, i in enumerate(nums):
    print(v, i)
for i in range(len(nums)):
	print(i,nums[i])

# Print the original list
print(nums)

# Count the frequency of each element in the list
frequency_map = Counter(nums)

# Print the frequency map
print(frequency_map)

# Create a dictionary to store frequency counts
freq_dic = {}

# Count the frequency of each element in the list
for i in nums:
    freq_dic[i] = freq_dic.get(i, 0) + 1

# Print the frequency dictionary
print(freq_dic)

# Sort the frequency dictionary keys based on their values in descending order
sorted_freq_dic = sorted(freq_dic.keys(), key=lambda x: freq_dic[x], reverse=True)
print(sorted_freq_dic)

# Sort the frequency dictionary keys based on their values in descending order
sorted_freq_dic = sorted(freq_dic, key=lambda x: freq_dic[x], reverse=True)
print(sorted_freq_dic)

# Print the first three elements of the list
print(nums[:3])

# Print elements from index 5 to index 8 (inclus) of the list
print(nums[5:9])

# Define a class Solution
class Solution:
    # Define a method to find the top K frequent elements
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store frequency counts
        freq_dic = {}

        # Count the frequency of each element in the list
        for i in nums:
            freq_dic[i] = freq_dic.get(i, 0) + 1
        
        # Sort the frequency dictionary keys based on their values in descending order
        sorted_freq_dic = sorted(freq_dic, key=lambda x: freq_dic[x], reverse=True)
        
        # Return the top K frequent elements
        return sorted_freq_dic[:k]