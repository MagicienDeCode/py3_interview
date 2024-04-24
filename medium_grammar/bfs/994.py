from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        count = 0
        level = -1
        dq = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    dq.append([i,j])
        if fresh == 0:
            return 0
        while dq:
            size = len(dq)
            for _ in range(size):
                x,y = dq.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]):
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 7
                            count += 1
                            dq.append([nx,ny])

            level += 1
        
        return level if fresh == count else -1
        