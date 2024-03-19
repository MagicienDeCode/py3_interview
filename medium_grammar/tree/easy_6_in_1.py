class Solution226:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

class Solution100:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

import queue
from collections import deque
class Solution104:
    def maxDepthDfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

    def maxDepthQueue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = queue.Queue()
        q.put(root)
        level = 0
        while q:
            size = q.qsize()
            for _ in range(size):
                c = q.get()
                if c.left:
                    q.put(c.left)
                if c.right:
                    q.put(c.right)
            level += 1
        return level

    def maxDepthDeque(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                c = q.popleft()
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            level += 1
        return level

class Solution110:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1

    # -1 means NOT_BALANCED
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)

        if l == -1 or r == -1 or abs(l-r) > 1:
            return -1
        
        return 1 + max(l,r)

class Solution543:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(c: Optional[TreeNode]) -> int:
            if not c:
                return 0
            l = dfs(c.left)
            r = dfs(c.right)
            self.res = max(self.res, l+r)
            return 1 + max(l,r)
        dfs(root)
        return self.res

class Solution572:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        while root or stack:
            while root:
                if root.val == subRoot.val and self.isSameTree(root,subRoot):
                    return True
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)