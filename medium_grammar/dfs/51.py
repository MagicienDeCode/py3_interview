class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.col_set = set()
        self.d1_set = set()
        self.d2_set = set()
        self.grid = [['.' for _ in range(n)] for _ in range(n)]
        self.res = []
        self.dfs(0)
        return self.res
        
    def dfs(self,row:int):
        if row == self.n:
            self.res.append(["".join(r) for r in self.grid])
        else:
            for i in range(self.n):
                d1 = row + i
                d2 = row - i
                if i not in self.col_set and d1 not in self.d1_set and d2 not in self.d2_set:
                    self.grid[row][i] = 'Q'
                    self.col_set.add(i)
                    self.d1_set.add(d1)
                    self.d2_set.add(d2)
                    self.dfs(row+1)
                    self.grid[row][i] = '.'
                    self.col_set.remove(i)
                    self.d1_set.remove(d1)
                    self.d2_set.remove(d2)