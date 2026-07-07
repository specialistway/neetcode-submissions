class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #哦哦有多少个连通图 那就直接bfs??
        res=0
        visit=set()
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(start):
            visit.add(start)
            q=deque()
            q.append(start)
            while q:
                node=q.popleft()
                for nei in adj[node]:
                    if nei in visit:
                        continue
                    q.append(nei)
                    visit.add(nei)



        for i in range(n):
            if i not in visit:
                bfs(i)
                res+=1
        return res
        