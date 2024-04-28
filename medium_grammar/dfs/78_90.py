import copy
class Solution78:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums,0,[],res)
        return res
    
    def dfs(self, nums: List[int],index:int,subs:List[int],res:List[List[int]]):
        # print("=======================>")
        # print(subs)
        # print(res)
        res.append(copy.deepcopy(subs))
        for i in range(index,len(nums)):
            subs.append(nums[i])
            self.dfs(nums,i+1,subs,res)
            subs.pop()

class Solution90:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums,0,[],res)
        return res

    def dfs(self, nums: List[int],index:int,subs:List[int],res:List[List[int]]):
        res.append(copy.deepcopy(subs))
        for i in range(index,len(nums)):
            if i > 0 and nums[i] == nums[i-1] and i > index:
                continue
            subs.append(nums[i])
            self.dfs(nums,i+1,subs,res)
            subs.pop()