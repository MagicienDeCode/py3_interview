class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.row = [[False for _ in range(9)] for _ in range(9)]
        self.col = [[False for _ in range(9)] for _ in range(9)]
        self.box = [[False for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    box_i = (i//3)*3 + (j//3)
                    v = int(board[i][j]) - 1
                    self.row[i][v] = True
                    self.col[j][v] = True
                    self.box[box_i][v] = True
        self.dfs(0,0)

    def dfs(self, r:int, c:int) -> bool:
        if r == 9:
            return True
        if c == 9:
            return self.dfs(r+1,0)
        if self.board[r][c] != '.':
            return self.dfs(r,c+1)
        for i in range(ord('1'),ord('9')+1):
            char = chr(i)
            if self.isValidSudoku(r,c,char):
                v = int(char) - 1
                box_i = (r//3)*3 + (c//3)
                self.row[r][v] = True
                self.col[c][v] = True
                self.box[box_i][v] = True
                self.board[r][c] = char
                if self.dfs(r,c+1):
                    return True
                self.row[r][v] = False
                self.col[c][v] = False
                self.box[box_i][v] = False
                self.board[r][c] = '.'
        return False


    def isValidSudoku(self,r:int,c:int,char:str):
        v = int(char) - 1
        box_i = (r//3)*3 + (c//3)
        return not self.row[r][v] and not self.col[c][v] and not self.box[box_i][v]
        