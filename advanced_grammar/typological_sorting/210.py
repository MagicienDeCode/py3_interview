from collections import deque,defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Calculate in-degrees of all vertices & build graph
        indegrees = [0]*numCourses
        graph = defaultdict(list)
        for aft,pre in prerequisites:
            graph[pre].append(aft)
            indegrees[aft] += 1
        # 2. Create a queue to store all vertices with in-degree 0.
        dq = deque()
        for i in [i for i in range(numCourses) if indegrees[i] == 0]: dq.append(i)
        # 3. While the queue is not empty, extract a vertex from the queue.
        res = []
        while dq:
            # 4. Append the extracted vertex to the topological order.
            course = dq.popleft()
            res.append(course)
            # 5. For each adjacent vertex, decrease its in-degree by 1.
            for neighbor in graph[course]:
                indegrees[neighbor] -=1
                if indegrees[neighbor] == 0: dq.append(neighbor)
            # 6. If in-degree of an adjacent vertex becomes 0, add it to the queue.

        return res if len(res) == numCourses else []
        # 7. If all vertices are processed, the topological sort is complete.
        # 8. If the graph has a cycle, it won’t be possible to get a valid topological order.

"""
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        # 1. build graph in reverse order to from.
        for aft,pre in prerequisites:
            self.graph[aft].append(pre)
        # 2. create visited array & initiate 0.
        self.visited = [0] * numCourses
        self.res = []
        self.hasCycle = False
        # 3. iterate each node, if not visited, call dfs function.
        for i in range(numCourses):
            if self.hasCycle: return []
            if self.visited[i] == 0: self.dfs(i)

        return self.res if len(self.res) == numCourses else []

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
        self.res.append(i)
"""