class Solution589:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        res.append(root.val)
        for c in root.children:
            res += self.preorder(c)
        return res

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = []
        res = []
        if not root:
            return res
        stack.append(root)
        while stack:
            c = stack.pop()
            res.append(c.val)
            for i in range(len(c.children)-1,-1,-1):
                stack.append(c.children[i])
        return res