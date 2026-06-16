from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid),len(grid[0])
        res=0
        dx=[0,-1,0,1]# left up right down
        dy=[-1,0,1,0]
        def bfs(x,y):
            # if grid[x][y]=='0':
            #     return
            q=deque()
            q.append((x,y))
            while q:
                cur_x,cur_y=q.popleft()
                for i in range(4):
                    new_x,new_y=dx[i]+cur_x,dy[i]+cur_y
                    if new_x<0 or new_x>=n or new_y<0 or new_y>=m or grid[new_x][new_y]=='0' :
                        continue
                    grid[new_x][new_y]='0'
                    q.append((new_x,new_y))
            
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='0':
                    continue
                bfs(i,j)
                res+=1
        return res

        