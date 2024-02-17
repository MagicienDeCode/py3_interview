from typing import List
# declare a dictionary dic
dic = {"name": "hanzawa naoki", "age": 30, "city": "kanazawa"}
# print the dictionary
print(dic)

# print the value associated with the key "name"
print(dic["name"])
# add a new key-value pair to the dictionary
dic["country"] = "France"
print(dic)
# update the value associated with the key "age"
dic["age"] = 31

# delete the key-value pair associated with the key "city"
del dic["city"]
print(dic)
# check if "city" is in the dictionary, if not, check for "name" and "age"
if "city" in dic:
    print("city in dic")
elif "name" in dic:
    print("name in dic")
elif "age" in dic:
    print("age in dic")
else:
    print("else")

# print the keys of the dictionary
print(dic.keys())

# print the values of the dictionary
print(dic.values())

# iterate through the dictionary and print key-value pairs
for k,v in dic.items():
    print(k,v)

# get the value associated with the key "name" or return "unknown" if the key is not present
print(dic.get("name","if not found"))

# get the value associated with the key "test" or return "unknown" if the key is not present
print(dic.get("test","if not found"))
print(dic.get("test",1992))
# clear all key-value pairs from the dictionary
dic.clear()
print(dic)

print("=======================================")
# declare my_list
my_list = [1, 1, 9, 9, 9, 9, 2, 4, 1, 0, 1, 1, 0, 2]

# add new values 5,7 in list using append()
my_list.append(5)
my_list.append(7)
print(my_list)
# declare dictionaries for values at odd and even indices
dic_odd = {}
dic_even = {}

# Separate values into dictionaries based on odd and even indices
for i in range(len(my_list)):
    if i % 2 == 0:
        dic_even[i] = my_list[i]
    else:
        dic_odd[i] = my_list[i]
# print values in dic_odd
print(dic_odd.keys())
print(dic_odd.values())
# print values in dic_even
print(dic_even.keys())
print(dic_even.values())
print("=======================================")

# declare a dictionary to store indices of each unique value in the list
# key= element in list, value= list of indices
dic_value_index = {}

# populate dic_value_index with indices for each unique value in my_list
for i in range(len(my_list)):
    if my_list[i] in dic_value_index:
        dic_value_index[my_list[i]].append(i)
    else:
        dic_value_index[my_list[i]] = []
        dic_value_index[my_list[i]].append(i)

# print the dictionary containing indices for each unique value
print(dic_value_index)

# clear dic_value_index
dic_value_index.clear()
# Alternatively, achieve the same result using setdefault
for i in range(len(my_list)):
    # line 80 to 84
    dic_value_index.setdefault(my_list[i],[]).append(i)

print(dic_value_index)

# resolve twoSum using dictionary
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in value_index:
                return [i,value_index[remain]]
            value_index[nums[i]] = i
        return []
