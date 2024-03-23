# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # store preorder inorder in class instance
        self.p = preorder
        self.i = inorder
        return self.build(0,len(preorder)-1,0,len(preorder)-1)

    # preorder M L R
    # inorder  L M R
    def build(self,ps:int,pe:int,iss:int,ie:int) -> TreeNode:
        if ps > pe or iss > ie:
            return None
        # root value is the first element in preorder list
        root = TreeNode(self.p[ps])
        # find mid position in inorder list
        index = iss
        while self.i[index] != root.val:
            index += 1
        root.left = self.build(ps+1,ps+index-iss,iss,index-1)
        root.right = self.build(ps+index-iss+1,pe,index+1,ie)
        return root