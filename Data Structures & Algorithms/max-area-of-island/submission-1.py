from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #每次flood fill的时候记录一下大小就行了
        n,m=len(grid),len(grid[0])
        res=0
        dx=[0,-1,0,1]
        dy=[-1,0,1,0]
        def bfs(x,y):
            q=deque()
            q.append((x,y))
            grid[x][y]=0
            area=1
            while q:
                cur_x,cur_y=q.popleft()
                for i in range(4):
                    new_x,new_y=dx[i]+cur_x,dy[i]+cur_y
                    if new_x<0 or new_x>=n or new_y<0 or new_y>=m or grid[new_x][new_y]==0:
                        continue
                    grid[new_x][new_y]=0
                    q.append((new_x,new_y))
                    area+=1
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    continue
                # res=max(bfs(i,j),res)
                area=bfs(i,j)
                res=max(area,res)
        return res