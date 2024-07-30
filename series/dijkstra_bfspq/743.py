from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build directed graph
        graph = defaultdict(list)
        for ti in times:
            graph[ti[0]].append([ti[1],ti[2]])
        # time array, default -1
        times = [-1]*(n+1)
        times[0] = 0
        # min heapq order iterate nodes
        pq = []
        heapq.heappush(pq,[0,k])
        while pq:
            t,d = heapq.heappop(pq)
            if times[d] == -1:
                times[d] = t
            for nd in graph[d]:
                if times[nd[0]] == -1:
                    heapq.heappush(pq,[t+nd[1],nd[0]])
                
        # if time array contains -1, return -1, else return max(time array)
        return -1 if -1 in times else max(times)