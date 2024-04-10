"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        all_nodes = self.getAllNodes(node)
        # olde node to new node
        dic = {}
        for old in all_nodes:
            new = Node(old.val,[])
            dic[old] = new
        
        for old in all_nodes:
            new = dic[old]
            for old_n in old.neighbors:
                new.neighbors.append(dic[old_n])

        return dic[node]

    def getAllNodes(self,node:'Node') -> List['Node']:
        dq = deque()
        visited = set()
        dq.append(node)
        visited.add(node)
        while dq:
            c = dq.popleft()
            for n in c.neighbors:
                if n not in visited:
                    dq.append(n)
                    visited.add(n)
        return list(visited)