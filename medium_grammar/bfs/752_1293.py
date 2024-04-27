from collections import deque
class Solution752:
    def openLock(self, deadends: List[str], target: str) -> int:
        dset = set(deadends)
        graph = {str(i):[str(i+1),str(i-1)] for i in range(1,9)}
        graph['0'] = ['9','1']
        graph['9'] = ['8','0']
        if "0000" in dset:
            return -1
        visited = set()
        dq = deque()
        dq.append("0000")
        level = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                c = dq.popleft()
                if c == target:
                    return level
                for i in range(4):
                    next1 = c[0:i] + graph[c[i]][0] + c[i+1:len(c)]
                    next2 = c[0:i] + graph[c[i]][1] + c[i+1:len(c)]
                    lst = [next1,next2]
                    for n in lst:
                        if n not in visited and n not in dset:
                            dq.append(n)
                            visited.add(n)
            level += 1
        return -1
        
from collections import deque
class Solution1293:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dq = deque()
        visited = [[[False for _ in range(k+1)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        visited[0][0][k] = True
        dq.append((0,0,k))
        level = 0
        while dq:
            for _ in range(len(dq)):
                x,y,k = dq.popleft()
                if x == len(grid)-1 and y == len(grid[0])-1:
                    return level
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]):
                        # obstacle
                        if grid[nx][ny] == 1:
                            if k>0 and not visited[nx][ny][k-1]:
                                visited[nx][ny][k-1] = True
                                dq.append((nx,ny,k-1))
                        else:
                            if not visited[nx][ny][k]:
                                visited[nx][ny][k] = True
                                dq.append((nx,ny,k))
            level += 1

        return -1