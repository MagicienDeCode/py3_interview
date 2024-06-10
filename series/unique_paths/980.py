
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # count how many 0 squares, total_zero
        # from starting square, count zero square, if count == total_zero and x,y is ending square, result += 1
        self.total_zero = 0
        self.grid = grid
        self.res = 0
        x = -1
        y = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.total_zero +=1
                if grid[i][j] == 1:
                    x = i
                    y = j
        self.dfs(x,y,0)
        return self.res

    def dfs(self,x:int,y:int,count:int):
        if self.grid[x][y] == 2:
            if count == self.total_zero:
                self.res +=1
        else:
            value = self.grid[x][y]
            next_count = count + 1 if value == 0 else count
            self.grid[x][y] = -1
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and ny >= 0 and nx < len(self.grid) and ny < len(self.grid[0]):
                    if self.grid[nx][ny] != -1:
                        self.dfs(nx,ny,next_count)
            self.grid[x][y] = value