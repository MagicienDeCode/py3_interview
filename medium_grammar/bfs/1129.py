from collections import deque,defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # build directed graph
        graphr = defaultdict(list)
        graphb = defaultdict(list)
        for red in redEdges:
            graphr[red[0]].append(red[1])
        for blue in blueEdges:
            graphb[blue[0]].append(blue[1])
        # visited,deque,res
        res = [-1] * n
        visited = [[False,False] for _ in range(n)]
        dq = deque()
        dq.append([0,0])
        dq.append([0,1])
        level = 0
        # BFS
        while dq:
            size = len(dq)
            for _ in range(size):
                node,color = dq.popleft()
                if res[node] == -1:
                    res[node] = level
                neighbors = graphr[node] if color == 1 else graphb[node]
                for nei in neighbors:
                    if not visited[nei][color^1]:
                        visited[nei][color^1] = True
                        dq.append([nei,color^1])
            level += 1

        return res
