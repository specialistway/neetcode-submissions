class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #能不能到达和到达的代价
        adj=defaultdict(list)
        for i,eq in enumerate(equations):
            a,b=eq
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))
        def bfs(src,target):
            if src not in adj or target not in adj:
                return -1
            q=deque()
            #q里面存的是 node和到达该node的value吧，但是这样子的话每次都要计算一遍很麻烦啊
            visit=set()
            q.append((src,1))
            visit.add(src)

            while q:
                node,w=q.popleft()
                if node==target:
                    return w
                for nei,wei in adj[node]:
                    if nei not in visit:
                        q.append((nei,w*wei))
                        visit.add(nei)
            return -1
                
        return [bfs(q[0],q[1]) for q in queries]
        