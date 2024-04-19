from collections import deque
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = set()
        dq = deque()
        dq.append(id)
        visited.add(id)
        ll = 0
        freq = {}
        while dq:
            if ll == level:
                while dq:
                    n = dq.popleft()
                    videos = watchedVideos[n]
                    for v in videos:
                        freq[v] = freq.get(v,0) + 1
                break
            size = len(dq)
            for _ in range(size):
                c = dq.popleft()
                for f in friends[c]:
                    if f not in visited:
                        visited.add(f)
                        dq.append(f)
            ll += 1
        sorted_freq = sorted(freq.items(), key = lambda x: (x[1],x[0]))

        return [x for x,y in sorted_freq]
        