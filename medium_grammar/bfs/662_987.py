# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution662:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0
        dq = deque()
        dq.append([root,1])
        while dq:
            size = len(dq)
            maxv = float('-inf')
            minv = float('inf')
            for _ in range(size):
                r,v = dq.popleft()
                maxv = max(maxv,v)
                minv = min(minv,v)
                if r.left:
                    dq.append([r.left, v << 1])
                if r.right:
                    dq.append([r.right, v * 2 + 1])
            res = max(res,maxv - minv +1)

        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class Solution:
    def verticalTraversal978(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        dq = deque()
        dq.append([root,0])
        dic = defaultdict(list)
        while dq:
            l_dic = defaultdict(list) 
            size = len(dq)
            for _ in range(size):
                r,v = dq.popleft()
                l_dic[v].append(r.val)
                if r.left:
                    dq.append([r.left, v - 1])
                if r.right:
                    dq.append([r.right, v + 1])
            for k,v in l_dic.items():
                dic[k].extend(sorted(v))
        sorted_dic = sorted(dic.items(), key=lambda x:x[0])
        for k,v in sorted_dic:
            res.append(v)
        return res