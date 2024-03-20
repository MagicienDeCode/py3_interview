# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution235:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cv = root.val
        pv = p.val
        qv = q.val
        if pv > cv and qv > cv:
            return self.lowestCommonAncestor(root.right, p, q)
        elif pv < cv and qv < cv:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

from collections import deque
class Solution102:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        dq = deque()
        dq.append(root)
        while dq:
            size = len(dq)
            cur = []
            for _ in range(size):
                c = dq.popleft()
                cur.append(c.val)
                if c.left:
                    dq.append(c.left)
                if c.right:
                    dq.append(c.right)
            res.append(cur)
        return res

from collections import deque
class Solution199:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        dq = deque()
        dq.append(root)
        while dq:
            size = len(dq)
            res.append(dq[-1].val)
            for i in range(size):
                c = dq.popleft()
                if c.left:
                    dq.append(c.left)
                if c.right:
                    dq.append(c.right)
        return res