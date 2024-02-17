from typing import List
# declare a dictionary dic
dic = {"name": "hanzawa naoki", "age": 30, "city": "kanazawa"}
# print the dictionary
print(dic)

# print the value associated with the key "name"

# add a new key-value pair to the dictionary


# update the value associated with the key "age"


# delete the key-value pair associated with the key "city"


# check if "city" is in the dictionary, if not, check for "name" and "age"


# print the keys of the dictionary


# print the values of the dictionary


# iterate through the dictionary and print key-value pairs


# get the value associated with the key "name" or return "unknown" if the key is not present


# get the value associated with the key "test" or return "unknown" if the key is not present


# clear all key-value pairs from the dictionary

print(dic)


# declare my_list
my_list = [1, 1, 9, 9, 9, 9, 2, 4, 1, 0, 1, 1, 0, 2]

# add new values 5,7 in list using append()

print(my_list)
# declare dictionaries for values at odd and even indices
dic_odd = {}
dic_even = {}

# Separate values into dictionaries based on odd and even indices

# print values in dic_odd

# print values in dic_even

print("=======================================")

# declare a dictionary to store indices of each unique value in the list
# key= element in list, value= list of indices
dic_value_index = {}

# populate dic_value_index with indices for each unique value in my_list

# print the dictionary containing indices for each unique value
print(dic_value_index)

# clear dic_value_index

# Alternatively, achieve the same result using setdefault

print(dic_value_index)

# resolve twoSum using dictionary
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
