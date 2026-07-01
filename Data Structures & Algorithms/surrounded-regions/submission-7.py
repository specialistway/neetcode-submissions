class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #或者每一次flood fill都记下来
        n,m=len(board),len(board[0])
        dx,dy=[0,-1,0,1],[-1,0,1,0]
        def bfs(i_start,j_start):
            visit=[[False]*m for _ in range(n)]
            q=deque()
            q.append((i_start,j_start))
            board[i_start][j_start]='X'
            visit[i_start][j_start]=True
            f=0
            while q:
                x,y=q.popleft()
                for i in range(4):
                    new_x,new_y=x+dx[i],y+dy[i]
                    if new_x<0 or new_x>n-1 or new_y<0 or new_y>m-1 or board[new_x][new_y]=='X':
                        continue
                    if new_x==0 or new_x==n-1 or new_y==0 or new_y==m-1:
                        f=1
                    board[new_x][new_y]='X'
                    q.append((new_x,new_y))
                    visit[new_x][new_y]=True
            if f:
                for i in range(n):
                    for j in range(m):
                        if visit[i][j]:
                            board[i][j]='O'
        for i in range(1,n-1):
            for j in range(1,m-1):
                if board[i][j]=='O':
                    bfs(i,j)
                    


        