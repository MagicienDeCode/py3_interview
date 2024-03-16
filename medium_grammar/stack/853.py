class Solution853:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = []
        #for i in range(len(position)):
            #ps.append([position[i],speed[i]])
        for p,s in zip(position,speed):
            ps.append([p,s])
        # ps = [[p1,s1],[p2,s2],...]
        ps_sorted = sorted(ps, key= lambda x: x[0], reverse=True)
        stack = [ps_sorted[0]]
        for pre in ps_sorted[1:]:
            car = stack[-1]
            if not self.fleet(pre,car,target):
                stack.append(pre)
        return len(stack)

    def fleet(self,pre:List[int],car:List[int],target:int) -> bool:
        if pre[1] <= car[1]:
            return False
        new_p = ((car[0] - pre[0]) * car[1] / (pre[1] - car[1])) + car[0]
        return new_p <= target

