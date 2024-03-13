class MinStack155:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if min stack is empty
        # or min stack top element >= current (new min element) 
        if (not self.min_stack) or (self.min_stack[-1] >= val):
            self.min_stack.append(val)

    def pop(self) -> None:
        top_element = self.stack.pop()
        # if pop element == min element, also pop it
        if top_element == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


class Solution150:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_set = {'+','-','*','/'}
        for s in tokens:
            if s in operator_set:
                second = int(stack.pop())
                first = int(stack.pop())
                # result should be pushed back into stack
                stack.append(self.calculate(first,second,s))
            else:
                stack.append(s)
        return int(stack[-1])

    def calculate(self,first:int,second:int,opr:str) -> int:
        if opr == '+':
            return first + second
        elif opr == '-':
            return first - second
        elif opr == '*':
            return first * second
        else:
            return first / second