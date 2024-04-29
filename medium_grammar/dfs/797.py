import copy
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dfs(graph,0,[0],res)
        return res
        
    def dfs(self, graph: List[List[int]],n:int,subs:List[int],res:List[List[int]]):
        if n == len(graph) - 1:
            res.append(copy.deepcopy(subs))
        else:
            for nei in graph[n]:
                subs.append(nei)
                self.dfs(graph,nei,subs,res)
                subs.pop()
