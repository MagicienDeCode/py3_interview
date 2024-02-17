from typing import List
# Creating a set with elements 1, 9, 9, and 4
my_set = {1,9,9,4}

# Printing the set
print(my_set)

# Adding elements 2 and 4 to the set
# dic["key"] = value
# my_list.append()
my_set.add(1)
my_set.add(2)
# Printing the updated set
print(my_set)

# Discarding elements 0 and 9 from the set (if present)
# Note: Using discard() to avoid KeyError if the element is not present
my_set.discard(20)
my_set.discard(9)

# Printing the length of the set
print(len(my_set))

# Checking if specific elements are in the set and printing corresponding messages
if 9 in my_set:
	print("9 is in set")
elif 1 in my_set:
	print("1 is in set")
elif 2 in my_set:
	print("2 is in set")
else:
	print("else")

# Iterating through the set and printing each element
for i in my_set:
	print(i)

# Clearing all elements from the set
my_set.clear()
print(my_set)

# Defining a class Solution with a method containsDuplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Creating a set to store unique integers
        int_set = set()
        # Iterating through the input list of integers
        for i in nums:
            # Checking if the integer is already in the set
            if i in int_set:
                return True
            # Adding the integer to the set if not present
            int_set.add(i)
        # Returning False if no duplicates are found
        return False
