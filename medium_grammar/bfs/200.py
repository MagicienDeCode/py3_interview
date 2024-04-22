from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dq = deque()
                    dq.append((i,j))
                    grid[i][j] = '0'
                    while dq:
                        x,y = dq.popleft()
                        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                            nx = x + dx
                            ny = y + dy
                            if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]):
                                if grid[nx][ny] == '1':
                                    grid[nx][ny] = '0'
                                    dq.append((nx,ny))
        return res