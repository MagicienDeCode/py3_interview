from collections import defaultdict
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        self.n = n
        self.threshold = distanceThreshold
        self.graph = defaultdict(list)
        self.shortest = [[100000]*n for _ in range(n)]
        for i in range(n): self.shortest[i][i] = 0
        for s,e,w in edges:
            self.graph[s].append((e,w))
            self.graph[e].append((s,w))
        for i in range(n):
            self.dijkstra(i)
        return self.get_res()
        
    def dijkstra(self,i):
        pq = [(0,i)]
        distance = self.shortest[i]
        while pq:
            dis,city = heapq.heappop(pq)
            if dis > self.threshold: continue
            for neighbor,weight in self.graph[city]:
                next_dis = dis + weight
                if distance[neighbor] > next_dis and next_dis <= self.threshold: 
                    distance[neighbor] = next_dis
                    heapq.heappush(pq,(distance[neighbor],neighbor))

    def get_res(self):
        res = -1
        count = self.n
        for i in range(self.n):
            total = 0
            for j in range(self.n):
                if i == j: continue
                if self.shortest[i][j] <= self.threshold: total += 1
            if total <= count:
                count = total
                res = i
        return res
        