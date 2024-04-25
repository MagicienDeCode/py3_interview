from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # given the current state and click position, return next state
        # if click is 'M', change it to 'X'
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        dq = deque()
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        dq.append((click[0],click[1]))
        visited[click[0]][click[1]] = True
        # if click position is neighbor of Mine, set number
        # else set 'B', put all neighbors into the queue
        while dq:
            x,y = dq.popleft()
            count = 0
            temp = []
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board[0]):
                    if not visited[nx][ny]:
                        temp.append((nx,ny))
                        if board[nx][ny] == 'M':
                            count += 1
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for t in temp:
                    dq.append(t)
                    visited[t[0]][t[1]] = True
        
        return board

        