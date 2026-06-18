class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=2**31-1
        #最短路问题用广搜啊 第一个到达的就是最近的
        n,m=len(grid),len(grid[0])
        dx=[0,-1,0,1]
        dy=[-1,0,1,0]
        def bfs(x,y):
            q=deque()
            #那就第一个格子不算嘛，如果最后还是0的话
            visit=[[0]*m for _ in range(n)]
            q.append((x,y,0))
            visit[x][y]=1
            while q:
                cur_x,cur_y,dis=q.popleft()
                #应该是弹出的时候计算步数 但是每一层有多少呢？？
                
                for i in range(4):
                    new_x,new_y=cur_x+dx[i],cur_y+dy[i]
                    if new_x<0 or new_x>=n or new_y<0 or new_y>=m or visit[new_x][new_y]==1 or grid[new_x][new_y]==-1 :
                        continue
                    if grid[new_x][new_y]==0:
                        return dis+1
                    q.append((new_x,new_y,dis+1))
                    visit[new_x][new_y]=1
            return INF
                        

        for i in range(n):
            for j in range(m):
                if grid[i][j]==INF:
                    dis=bfs(i,j)
                    grid[i][j]=dis
        