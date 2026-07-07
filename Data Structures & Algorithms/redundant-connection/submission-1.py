class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #tree
        #找到那个环 然后随便断开一条就行了
        #拓扑排序 可以把那些
        n=len(edges)
        indegree=[0]*(n+1)
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            indegree[u]+=1
            indegree[v]+=1
            adj[u].append(v)
            adj[v].append(u)
        q=deque()
        for i in range(1,n+1):
            if indegree[i]==1:
                q.append(i)
                indegree[i]-=1
        while q:
            node=q.popleft()
            
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==1:
                    q.append(nei)
        for u,v in reversed(edges):
            if indegree[u]==2 and indegree[v]:
                return [u,v]
        return []