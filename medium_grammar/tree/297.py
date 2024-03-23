# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.preorder(root,res)
        return ''.join(res[:len(res)-1])

    def preorder(self,root,res):
        if not root:
            res.append("null")
            res.append(',')
        else:
            res.append(str(root.val))
            res.append(',')
            self.preorder(root.left,res)
            self.preorder(root.right,res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        dq = deque(data.split(','))
        return self.build(dq)
    
    def build(self, dq):
        if not dq:
            return None
        c = dq.popleft()
        if c == "null":
            return None
        root = TreeNode(int(c))
        root.left = self.build(dq)
        root.right = self.build(dq)
        return root

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))