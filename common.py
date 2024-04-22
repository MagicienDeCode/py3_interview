# sort a dictionnary by keys and return keys
dic = {"a":333,"c":22,"b":1}
print(dic) # {'a': 333, 'c': 22, 'b': 1}
sorted_dic = sorted(dic,key = lambda x: x[0])
print(sorted_dic) # ['a', 'b', 'c']

# sort a dictionnary by keys and return sorted list of pair
print(dic) # {'a': 333, 'c': 22, 'b': 1}
sorted_dic = sorted(dic.items(),key = lambda x: x[0])
print(sorted_dic) # [('a', 333), ('b', 1), ('c', 22)]

# sort a dictionnary by values and return sorted list of pair
print(dic) # {'a': 333, 'c': 22, 'b': 1}
sorted_dic = sorted(dic.items(),key = lambda x: x[1])
print(sorted_dic) # [('b', 1), ('c', 22), ('a', 333)]
# build an array using the first element
print([p1 for p1,p2 in sorted_dic]) # ['b', 'c', 'a']
# build an array using the second element
print([p2 for p1,p2 in sorted_dic]) # ['1', '22', '333']

lst = [("bb",22),("aa",22),("c",1)]
# sort lst firstly by the second element, if equals, by the first element
sorted_lst = sorted(lst, key = lambda x: (x[1],x[0]))
print(sorted_lst) # [('c', 1), ('aa', 22), ('bb', 22)]

# sort reverse order
sorted_lst2 = sorted(lst, key = lambda x: (x[1],x[0]), reverse = True)
print(sorted_lst2) # [('bb', 22), ('aa', 22), ('c', 1)]

