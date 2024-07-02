from collections import defaultdict,deque
import copy
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 1. Calculate in-degrees of all vertices & build graph.
        graph = defaultdict(list)
        indegrees = [0 for _ in range(n)]
        for fr,to in edges:
            graph[fr].append(to)
            indegrees[to]+=1
        # 2. Create a queue to store all vertices with in-degree 0.
        dq = deque()
        for d in [i for i in range(n) if indegrees[i] == 0]: dq.append(d)
        # 3. While the queue is not empty, extract a vertex from the queue.
        topological_order = []
        while dq:
            # 4. Append the extracted vertex to the topological order.
            node = dq.popleft()
            topological_order.append(node)
            # 5. For each adjacent vertex, decrease its in-degree by 1.
            for child in graph[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0: dq.append(child)
                # 6. If in-degree of an adjacent vertex becomes 0, add it to the queue.

        res = [set() for _ in range(n)]
        for to in topological_order:
            for fr in graph[to]:
                res[fr].add(to)
                res[fr].update(res[to])

        return [sorted(list(i)) for i in res]

                
"""
from collections import defaultdict,deque
import copy
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 1. build graph from to
        self.graph = defaultdict(list)
        for fr,to in edges:
            self.graph[fr].append(to)
        # 2. create visited array & initiate 0.
        self.topological_order = []
        self.visited = [0] * n
        self.hasCycle = False
        # 3. iterate each node, if not visited, call dfs function.
        for i in range(n):
            if self.visited[i] == 0: self.dfs(i)
        # !! reverse list
        self.topological_order.reverse()
        res = [set() for _ in range(n)]
        for to in self.topological_order:
            for fr in self.graph[to]:
                res[fr].add(to)
                res[fr].update(res[to])

        return [sorted(list(i)) for i in res]

    def dfs(self,i):
        # 4. in dfs function, if has cycle(== -1) or already visited(== 1), return.
        if self.hasCycle or self.visited[i] == -1:
            self.hasCycle = True
            return
        if self.visited[i] == 1: return
        # 5. mark the current node -1.
        self.visited[i] = -1
        # 6. for each adjacent node, call dfs function.
        for neighbor in self.graph[i]:
            self.dfs(neighbor)
        # 7. mark the current node 1 and add current node into result.
        self.visited[i] = 1
        self.topological_order.append(i)
"""