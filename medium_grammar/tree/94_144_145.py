# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution94:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # inorder here
            res.append(root.val)
            root = root.right
        return res

class Solution144:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                # preorder here
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            # inorder here
            root = root.right
        return res

class Solution145:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversalStack(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        results = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                results.insert(0, root.val)  # Inserting at the beginning for reverse order
                root = root.right
            
            root = stack.pop().left  # Go to the left child after processing the right subtree
        
        return results