class Solution739:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        stack store index
        while [current] > [top]:
            pop
            calculate result = current - pop
        """
        stack_index = []
        res = [0] * len(temperatures)
        for i,v in enumerate(temperatures):
            while len(stack_index) != 0 and v > temperatures[stack_index[-1]]:
                pop_index = stack_index.pop()
                res[pop_index] = i - pop_index
            stack_index.append(i)
        return res
        