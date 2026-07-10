class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #是因为这个题确实很难啊！！！
        #它说的是序列的长度
        if endWord not in wordList or beginWord==endWord:
            return 0
        
        n,m=len(wordList),len(wordList[0])
        adj=[[] for i in range(n+1)]
        def is_nei(s1,s2):
            cnt=0
            for i in range(m):
                if s1[i]!=s2[i]:
                    cnt+=1
            if cnt==1:
                return True
            return False
        for i in range(n):
            if is_nei(beginWord,wordList[i]):
                adj[0].append(i+1)
                adj[i+1].append(0)
        for i in range(n):
            for j in range(i+1,n):
                if is_nei(wordList[i],wordList[j]):
                    adj[i+1].append(j+1)
                    adj[j+1].append(i+1)
        q=deque()
        visit=set()
        q.append(0)
        visit.add(0)
        #嗯就是你需要记录一下最短的路径 这个怎么记录比较好呢？？把每一层都记录下来吗？？
        res=0
        #奥对 就是每次处理一层的
        while q:
            res+=1
            for i in range(len(q)):
                node=q.popleft()
                if node and wordList[node-1]==endWord:
                    return res
                for nei in adj[node]:
                    if nei in visit:
                        continue
                    visit.add(nei)
                    q.append(nei)
        return 0


        