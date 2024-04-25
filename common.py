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

# heapq, customer sort, sort by the second element, then the first
class MyOb:
  def init (self, i:int,s:str):
    self.i = i
    self.s = s
  
  def lt (self,other):
    if self.s == other.s:
      return self.i < other.i
    return self.s < other.s

m2 = MyOb(22,"bb")
m1 = MyOb(33,"bb")
m3 = MyOb(444,"cc")
m4 = MyOb(999,"a")

import heapq

pq = []
heapq.heappush(pq,m1)
heapq.heappush(pq,m2)
heapq.heappush(pq,m3)
heapq.heappush(pq,m4)

while pq:
  print(heapq.heappop(pq).i)

# BFS matrix
for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
    nx = x + dx
    ny = y + dy
    if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]):
        if grid[nx][ny] == 1:
            grid[nx][ny] = 7
            dq.append([nx,ny])

m = 3  # 行数
n = 4  # 列数

# 声明一个m*n的数组，初始化全为False
array = [[False for _ in range(n)] for _ in range(m)]
print(array) # [[False, False, False, False], [False, False, False, False], [False, False, False, False]]
array[2][0] = True
print(array) # [[False, False, False, False], [False, False, False, False], [True, False, False, False]]

# Example of wrong declaration 
arr2 = [[False]*4 for _ in range(m)]
print(arr2) # [[False, False, False, False], [False, False, False, False], [False, False, False, False]]
arr3 = [[False]*4]*3
print(arr3) # [[False, False, False, False], [False, False, False, False], [False, False, False, False]]
arr3[2][0] = True
print(arr3) # [[True, False, False, False], [True, False, False, False], [True, False, False, False]]