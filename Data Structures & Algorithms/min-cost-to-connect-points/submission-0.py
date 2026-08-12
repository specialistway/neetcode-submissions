class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        node=0
        edges=0
        dist=[1e9]*n
        visit=[False]*n
        res=0
        while edges<n-1:
            visit[node]=True
            nextNode=-1
            for i in range(n):
                if visit[i]:
                    continue
                #每次跟新一波dist
                curDist=abs(points[i][0]-points[node][0])+abs(points[i][1]-points[node][1])
                dist[i]=min(dist[i],curDist)
                if nextNode==-1 or dist[i]<dist[nextNode]:
                    nextNode=i
            res+=dist[nextNode]
            node=nextNode
            edges+=1
        return res

        #其实就是连通性问题 构建一个联通图就行了
        #如何花最小代价构建一个联通图
        #弄一个连通图的集合
        #每次计算所有距离 到那个连通图集合的最小距离
        #用编号表示每个点
    

        