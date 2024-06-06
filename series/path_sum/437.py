# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        return self.dfs(root,targetSum,0) + self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum)

    def dfs(self,root:Optional[TreeNode],targetSum:int, current:int) -> int:
        if not root: return 0
        return  (1 if root.val + current == targetSum else 0) + self.dfs(root.left,targetSum,current+root.val) + self.dfs(root.right,targetSum,current+root.val)