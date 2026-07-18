class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m=len(board),len(board[0])
        visited=[[False for _ in range(m)] for _ in range(n)]
        def dfs(x,y,idx):
            if idx==len(word):#idx是从0开始 所以这个时候已经+1了
                return True
            if x<0 or x>=n or y<0 or y>=m or visited[x][y] or word[idx]!=board[x][y]:
                return False
            visited[x][y]=True
            res=(dfs(x,y-1,idx+1) or dfs(x-1,y,idx+1) or dfs(x,y+1,idx+1) or dfs(x+1,y,idx+1))
            visited[x][y]=False
            return res
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False
        