class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #这个肯定可以用bfs去做
        if "0000" in deadends:
            return -1
        q=deque()
        q.append("0000")
        steps=0
        visit=set(deadends)
        visit.add("0000")
        while q:
            l=len(q)
            steps+=1
            for _ in range(l):
                lock=q.popleft()
                for i in range(4):
                    for j in [1,-1]:
                        digit=str((int(lock[i])+j+10)%10)
                        nextlock=lock[:i]+digit+lock[i+1:]
                        if nextlock in visit:
                            continue
                        if nextlock==target:
                            return steps
                        q.append(nextlock)
                        visit.add(nextlock)
        return -1


        