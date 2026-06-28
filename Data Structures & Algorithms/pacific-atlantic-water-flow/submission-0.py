class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        n,m=len(heights),len(heights[0])
        pic=[[False]*m for _ in range(n)]
        atl=[[False]*m for _ in range(n)]
        dx,dy=[0,-1,0,1],[-1,0,1,0]
        def bfs(ocean,source):
            q=deque(source)
            while q:
                x,y=q.popleft()
                ocean[x][y]=True
                for i in range(4):
                    new_x,new_y=x+dx[i],y+dy[i]
                    if new_x<0 or new_x>=n or new_y<0 or new_y>=m or ocean[new_x][new_y]:
                        continue
                    if heights[new_x][new_y]>=heights[x][y]:
                        q.append((new_x,new_y))

        P=[]
        A=[]
        for i in range(m):
            P.append((0,i))
            A.append((n-1,i))
        for j in range(n):
            P.append(((j,0)))
            A.append((j,m-1))
        bfs(pic,P)
        bfs(atl,A)
        for i in range(n):
            for j in range(m):
                if pic[i][j] and atl[i][j]:
                    res.append([i,j])
        return res
