stack = []

# add element in stack
stack.append(1)
stack.append(9)
stack.append(9)
stack.append(4)
stack.append(2)
stack.append(7)

print(stack)

# pop element from stack

last_in_element = stack.pop()

print(last_in_element)
print(stack)

# get top element in stack, not pop
print(stack[-1])
#print(stack[len(stack)-1])

list_stack = []
print(len(list_stack) == 0)
print(not list_stack)

"""
1. push element in stack, append()
2. pop element from stack, pop()
3. verify if empty
4. get last(top) element, [-1]
"""

# given A,B,C push them into a stack, push order is A,B,C
# you can pop at any moment.

# Example, push A, pop, push B, push C, pop, pop
# Output A,C,B

# write code show all possible results

# A,C,B
# C,B,A
# B,A,C
# A,B,C
# B,C,A