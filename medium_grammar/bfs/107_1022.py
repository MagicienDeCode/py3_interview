# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution107:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        dq = deque()
        dq.append(root)
        while dq:
            size = len(dq)
            level = []
            for _ in range(size):
                c = dq.popleft()
                level.append(c.val)
                if c.left:
                    dq.append(c.left)
                if c.right:
                    dq.append(c.right)

            res.insert(0,level)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution1022:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0
        dq = deque()
        dq.append([root,0])
        while dq:
            c,v = dq.popleft()
            vv = v + c.val
            if not c.left and not c.right:
                res += vv
            if c.left:
                dq.append([c.left,vv << 1])
            if c.right:
                dq.append([c.right,vv << 1])

        return res
        