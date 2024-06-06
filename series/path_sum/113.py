# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.dfs(root,targetSum,0,[])
        return self.res

    def dfs(self,root:Optional[TreeNode],targetSum:int, current:int,subsets:List[int]):
        if not root: return
        current = current + root.val
        subsets.append(root.val)
        if not root.left and not root.right:
            if current == targetSum: self.res.append(copy.deepcopy(subsets))
            return
        if root.left:
            self.dfs(root.left,targetSum,current,subsets)
            subsets.pop()
        if root.right:
            self.dfs(root.right,targetSum,current,subsets)
            subsets.pop()