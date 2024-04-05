from collections import deque

dq = deque()

"""
appendleft(2) >>========================<< append(1)
popleft()     <<========================>> pop()
"""


dq.append(1)
dq.append(2)

print(dq) # [1 2]

dq.appendleft(3)

print(dq) # [3,1,2]

print(dq.pop()) #2

while dq:
	print("dq is not empty")
	break

print(dq.popleft()) # 3
print(dq.popleft()) # 1

print(not dq) # True , because dq is empty

dq2 = deque()
dq2.append(9)
dq2.append(4)
while dq2:
	print(dq2.popleft())
print("end dq2")