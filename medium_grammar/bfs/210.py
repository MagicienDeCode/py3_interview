from collections import deque,defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build directed graph and its indegrees
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegrees[pre[0]] += 1
        # bfs try to find order of courses
        dq = deque()
        for i,v in enumerate(indegrees):
            if v == 0:
                dq.append(i)
        res = []
        while dq:
            c = dq.popleft()
            res.append(c)
            for n in graph[c]:
                indegrees[n] -=1
                if indegrees[n] == 0:
                    dq.append(n)
        return res if len(res) == numCourses else []