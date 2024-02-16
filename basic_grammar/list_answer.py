from typing import List
# declare an int list with values 1,9,9,4
my_list = [1,9,9,4]
# index  0->1,1->9,2->9,3->4
your_list = []
# print entire my_list
print([1,9,9,4])
print(my_list)
print(your_list)
# print the first element in my_list 
print(my_list[0])
# print the second element in my_list
print(my_list[1])
#print(my_list[4]) # IndexError: list index out of range
# for loop, print each index of my_list
for i in range(0,4):
  print(i) # 0 1 2 3
print("=========================================")
print(len(my_list))
for i in range(len(my_list)):
  print(i)
# for loop, print each element of my_list
for i in my_list:
  print(i)
print("=========================================")
# declare a string list named str_list contains "python3","kotlin","java"
str_list = ["python3","kotlin","java"]
# print length of this list
print(len(str_list))
# print element "java" in this list
print(str_list[2])
# print each element in list using its index
for i in range(len(str_list)):
  print(str_list[i])
for i in str_list:
  print(i)
print("=========================================")
# define a function named countLen5 that accept a string list as parameter and return an int as result
def countLen5(param:List[str]) -> int:
  # declare a variable named res, assign value 0
  res = 0
	# iterate list directly, when element's len >= 5, add 1 for res
  for i in param:
    if len(i) >= 5:
      res+= 1
	# return res
  return res

# print result: call previous function using str_list above
print(countLen5(["python3","kotlin","java"]))
print(countLen5(str_list))
result = countLen5(str_list)
print(result)