# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root,targetSum,0)

    def dfs(self,root:Optional[TreeNode],targetSum:int, current:int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return root.val + current == targetSum
        return self.dfs(root.left,targetSum,current+root.val) or self.dfs(root.right,targetSum,current+root.val)