import heapq

lst1 = [10,9,8,7,6,5,4]

heapq.heapify(lst1)
print(lst1) # [4, 6, 5, 7, 9, 10, 8]

while lst1:
	print(heapq.heappop(lst1)) # 4,5,6,7,8,9,10

heapq.heappush(lst1,2)
heapq.heappush(lst1,1)

while lst1:
	print(heapq.heappop(lst1)) # 1,2


import queue

lst2 = [10,9,8,7,6,5,4]
pq = queue.PriorityQueue()
for l2 in lst2:
	pq.put(l2)

while not pq.empty():
	print(pq.get())