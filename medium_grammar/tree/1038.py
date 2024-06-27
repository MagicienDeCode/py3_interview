# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.rightFirst(root,0)
        return root
        
    def rightFirst(self, root:TreeNode, total: int) -> int:
        if not root: return 0
        right = self.rightFirst(root.right,total)
        before = root.val
        root.val += right + total
        left = self.rightFirst(root.left,root.val)
        return left + before + right
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        origin = root
        total = 0
        while stack or root:
            while root:
                # preorder here
                stack.append(root)
                root = root.right
            root = stack.pop()
            # right mid left
            # inorder here
            value = root.val
            root.val += total
            total += value
            root = root.left
        return origin