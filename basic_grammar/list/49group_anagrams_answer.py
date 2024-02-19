from typing import List

str1 = "Destiny takes a hand"
print(str1)

# Iterate through the characters of the string and print each character along with its ASCII value
for i in str1:
    print(i, ord(i))

# Print the sorted version of the string characters
print(sorted(str1))

# Print the string after sorting its characters and joining them back
print("".join(sorted(str1)))

# Define a class named Solution
class Solution:
    # Define a method to group anagrams in a list of strings
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create an empty dictionary to store anagrams
        map = {}
        # Iterate through each string in the list
        for s in strs:
            # Sort the characters of the string and join them back
            sorted_s = ''.join(sorted(s))
            # Append the string to the list of anagrams corresponding to its sorted version
            map.setdefault(sorted_s, []).append(s)
        # Return a list containing the values of the dictionary, which are lists of anagrams
        return list(map.values())