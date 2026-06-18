from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        q=deque()
        time=0
        fresh=0
        dx,dy=[0,-1,0,1],[-1,0,1,0]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        while fresh>0 and q:
            l=len(q)
            for i in range(l):
                cur_x,cur_y=q.popleft()

                for i in range(4):
                    #每次把新鲜的水果感染为腐烂
                    new_x,new_y=cur_x+dx[i],cur_y+dy[i]
                    #如果是空地 或者已经腐烂了呢？？？就不用重复加了
                    if new_x<0 or new_x>=n or new_y<0 or new_y>=m or grid[new_x][new_y]!=1:
                        continue
                    #如果是空地就跳过了
                    grid[new_x][new_y]=2
                    q.append((new_x,new_y))
                    fresh-=1
            time+=1
        return time if fresh==0 else -1

        