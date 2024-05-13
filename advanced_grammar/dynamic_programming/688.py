from collections import deque
class Solution:
    """
    M X X
    X X N
    X N X
    M init position,
    N valid move
    6
    -> 6 2
    -> 6 2
    ( 2 + 2 ) / ( 8 * 8 )

    # Memory Limit Exceeded
    if k == 0:
        return 1
    dq = deque()
    dq.append((row,column))
    level = 0
    valid = 0
    while dq:
        if level == k: break
        for _ in range(len(dq)):
            x,y = dq.popleft()
            for dx,dy in [(2,-1),(2,1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]:
                nx = x + dx
                ny = y + dy
                if n>nx>=0 and n>ny>=0:
                    dq.append((nx,ny))                
        level += 1

    valid = len(dq)
    total = 8 ** k
    return valid / total 

    """
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        self.dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(n)]
        self.dfs(row,column,k,n)
        total = 8 ** k
        return self.dp[row][column][k] / total 

    def dfs(self,r:int,c:int,k:int,n:int)->int:
        if k == 0:
            return 1
        if self.dp[r][c][k] != -1:
            return self.dp[r][c][k]
        res = 0
        for dx,dy in [(2,-1),(2,1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]:
            nx = r + dx
            ny = c + dy
            if n>nx>=0 and n>ny>=0:
                res += self.dfs(nx,ny,k-1,n)
        self.dp[r][c][k] = res
        return res