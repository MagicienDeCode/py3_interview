# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque,defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # build undirected graph
        self.graph = defaultdict(list)
        self.buildGraph(root.left, root)
        self.buildGraph(root.right, root)
        # bfs
        dq= deque()
        visited = set()
        dq.append(target.val)
        visited.add(target.val)
        level = 0
        res = []
        while dq:
            if level == k:
                break
            size = len(dq)
            for _ in range(size):
                c = dq.popleft()
                for n in self.graph[c]:
                    if n not in visited:
                        dq.append(n)
                        visited.add(n)
            level += 1
        while dq:
            res.append(dq.pop())
        return res

    def buildGraph(self, node: TreeNode, parent: TreeNode):
        if not node:
            return
        self.graph[node.val].append(parent.val)
        self.graph[parent.val].append(node.val)
        self.buildGraph(node.left, node)
        self.buildGraph(node.right, node)