# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution98:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode],min_v:int,max_v:int) -> bool:
            if not root:
                return True
            if min_v is not None and root.val <= min_v:
                return False
            if max_v is not None and root.val >= max_v:
                return False
            return dfs(root.left,min_v,root.val) and dfs(root.right,root.val,max_v)
        return dfs(root,None,None)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1448:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root: TreeNode,max_v:int):
            if not root:
                return
            if root.val >= max_v:
                self.res += 1
                max_v = root.val
            dfs(root.left,max_v)
            dfs(root.right,max_v)
        dfs(root,-10001)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution230:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left_c = self.count(root.left) + 1
        if left_c == k:
            return root.val
        elif left_c > k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - left_c)

    def count(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
        
