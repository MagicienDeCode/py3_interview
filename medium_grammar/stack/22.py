class Solution22Stack:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def dfs(left,right):
            if left == right and left == n:
                result.append("".join(stack))
                return
            if left < n:
                stack.append('(')
                dfs(left+1,right)
                stack.pop()
            if right < left:
                stack.append(')')
                dfs(left,right+1)
                stack.pop()
        dfs(0,0)
        return result

class Solution22:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        str_list = ['']*(n*2)
        for i in range(0,len(str_list),2):
            str_list[i] = "("
        def dfs(rI:int,restR:int):
            if rI == (len(str_list) - 1):
                str_list[rI] = ")" * restR
                result.append("".join(str_list))
                return
            # current position can put how many ) 
            max_right = rI // 2 + 1 - (len(str_list)//2 - restR)
            for i in range(0,max_right+1):
                str_list[rI] = ")" * i
                dfs(rI+2,restR-i)
                str_list[rI] = ""
        dfs(1,n)
        return result