from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        self.maxv = 26000001
        self.min_costs = [[26000001]*26 for _ in range(26)]
        # BFSPQ (dijkstra)
        self.graph = defaultdict(list)
        for ori,cha,cot in zip(original,changed,cost):
            self.graph[ori].append((cha,cot))
        for i in range(26): self.dijkstra(i)

        res = 0
        for s,t in zip(source,target):
            if s == t: continue
            si = ord(s)-97
            ti = ord(t)-97
            if self.min_costs[si][ti] == self.maxv: return -1
            res += self.min_costs[si][ti]
        return res

    def dijkstra(self, i):
        char_costs = self.min_costs[i]
        pq = [(0,i)]
        while pq:
            cost,index = heapq.heappop(pq)
            if cost >= char_costs[index]: continue
            char_costs[index] = cost
            char = chr(index+97)
            for neigh,neigh_cost in self.graph[char]:
                next_cost = cost + neigh_cost
                next_index = ord(neigh) - 97
                heapq.heappush(pq,(next_cost,next_index))