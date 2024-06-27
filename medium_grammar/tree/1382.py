# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # inorder convert tree to a sorted list
        # build balanced tree

        tree_val = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            tree_val.append(root.val)
            root = root.right
        return self.build(tree_val,0,len(tree_val)-1)
        
    def build(self, values:List[int],l:int,r:int)-> TreeNode:
        if r < l: return None
        if l == r: return TreeNode(values[l])
        m = l + (r-l)//2
        root = TreeNode(values[m])
        root.left = self.build(values,l,m-1)
        root.right = self.build(values,m+1,r)
        return root