from typing import List


# basic functions

print("ni hao") # ni hao

# convert str to int
print(int("9")) # 9

# max of 3 elements
print(max(7,8,9)) # 9

# convert int to str
print(str(1)) # 1

# retrieve length of a list, 
# a set, a dictionary, a string
print(len("list set dic ...")) # 16

# verify if a string is empty
print(not "") # True

# process control
if 3 > 2 :
	print("3>2") # only print 3>2
elif 4 > 3 :
	print("4>3")
else:
	print("else")

counter = 10
while counter > 7:
	print(counter) # 10 9 8
	counter -= 1

name = "xiang"
for i in range(len(name)):
	print(name[i],ord(name[i])) # x 120 # i 105 # a 97 # n 110 # g 103
for i in range(4):
	print(i) # 0 1 2 3
for i in range(0,4,2):
	print(i) # 0 2
for i in range(10,7,-1):
	print(i) # 10 9 8
for i in range(10,7,-1):
	if i == 10:
		break
	print(i) # no output
for i in range(10,7,-1):
	if i == 10:
		continue
	print(i) # 9 8


# list

my_list = [1,9,9,4]

# get the first 2 elements
print(my_list[:2]) # [1,9]

# get element from index 1 to 3 inclusive
print(my_list[1:len(my_list)]) # [9,9,4]

# index starts from 0
print(my_list[3]) # 4

# if index out of range
# print(my_list[5]) # IndexError: list index out of range

# add a value in list
my_list.append(0)
my_list.append(1)
print(my_list) # 1 9 9 4 0 1

# combine two lists
my_list2 = [2,7]
my_list.extend(my_list2)
print(my_list) # 1 9 9 4 0 1 2 7

# insert with index
my_list.insert(1,10)
print(my_list) # 1 10 9 9 ...

# iterate
for i in range(len(my_list)):
	print(my_list[i]) # 1 10 9 9 ...

for i in my_list:
	print(i) # 1 10 9 9 ...

for i,v in enumerate(my_list):
	print(i,v) # 0 1, 1 10, 2 9, 3 9, 4 4 ...



# dictionary

dic = {"name":"njk","age":30}
print(dic) # {'name': 'njk', 'age': 30}

# get value
print(dic["age"]) # 30

# change value
dic["age"] = 31
print(dic["age"]) # 31

# add a new key,value pair
dic["pays"] = "JP"
print(dic) # {'name': 'njk', 'age': 31, 'pays': 'JP'}

# delete a key,value pair
del dic["name"]
print(dic) # {'age': 31, 'pays': 'JP'}

# get keys or values
print(dic.keys()) # age, pays
print(dic.values()) # 31, JP

# iterate 
for k,v in dic.items():
	print(k,v) # age 31 , pays JP

# verify if key exists
if "age" in dic:
	print(dic["age"]) # 31

# clear
dic.clear()
print(dic) # {}

# get value, if not exists, return default
print(dic.get("test","test no in dic")) # test no in dic
print(dic.get("test",99)) # 99



# set

my_set = {1,9,9,4}
print(my_set) # {1,9,4}

# add a value in set 
my_set.add(2)
print(my_set) # {1,2,9,4}

# remove an element in list
# remove: if key not exists in set, KeyError, discard: if not exists, do nothing
my_set.discard(10)
# my_set.remove(10) # KeyError: 10

my_set.remove(9)
print(my_set) # {1, 2, 4}

# create an empty set
empty_set = set()
print(empty_set) # set()



# stirng

str1 = "xiang"
print(str1) # xiang

# iterate
for i in str1:
	print(i) # x i a n g
for i in range(len(str1)):
	print(str1[i]) # x i a n g

# ord, convert char to int
print(str1[2]) # a
print(ord(str1[2])) # 97
print(ord('a')) # 97
