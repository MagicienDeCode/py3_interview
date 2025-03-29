class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.res = ""
        self.given = set(nums)
        self.dfs(len(nums[0]),[])
        return self.res
    
    def dfs(self,l,t):
        if len(self.res) != 0: return
        if len(t) == l:
            ubs = "".join(t)
            if ubs not in self.given:
                self.res = ubs
            return
        t.append("0")
        self.dfs(l,t)
        t.pop()
        t.append("1")
        self.dfs(l,t)
        t.pop()

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            if nums[i][i] == '0': res.append('1')
            else: res.append('0')
        return "".join(res)
            