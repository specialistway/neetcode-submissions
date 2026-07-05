class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #你就记录下来队列的顺序就可以了
        adj=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        #从0指向1
        for tail,head in prerequisites:
            adj[head].append(tail)
            indegree[tail]+=1
        q=deque()
        res=[]
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                # res.append(i)

        
        while q:
            node=q.popleft()
            res.append(node)
            
            #应该是加入队列的时候删掉？
            #删掉的体现就是入度减一
            for next_node in adj[node]:
                indegree[next_node]-=1
                if indegree[next_node]==0:
                    q.append(next_node)
        
        return res if len(res)==numCourses else []
                


        