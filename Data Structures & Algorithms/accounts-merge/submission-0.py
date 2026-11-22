class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        emailIdx={}
        emails=[]
        emailToAcc={}

        m=0
        for accId,a in enumerate(accounts):#每一条记录都有一个Id
            for i in range(1,len(a)):
                email=a[i]
                if email in emailIdx:
                    continue
                #它这样一处理的话呢，
                emailIdx[email]=m
                emailToAcc[m]=accId
                emails.append(email)
                m+=1
        adj=[[] for _ in range(m)]
        for a in accounts:
            for i in range(2,len(a)):
                id1=emailIdx[a[i]]
                id2=emailIdx[a[i-1]]
                adj[id1].append(id2)
                adj[id2].append(id1)
        emailGroup=defaultdict(list)
        visited=[False]*m
        def dfs(node,accId):
            visited[node]=True
            emailGroup[accId].append(emails[node])
            #你怎么判断它是不是neibor呢
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei,accId)
        #到底有多少email
        for i in range(m):
            if not visited[i]:
                dfs(i,emailToAcc[i])
        res=[]
        for accId in emailGroup:
            name=accounts[accId][0]
            res.append([name]+sorted(emailGroup[accId]))
        return res




        