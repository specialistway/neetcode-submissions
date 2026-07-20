class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #这个一看就可以剪枝
        #遍历所有的子串
        part=[]
        res=[]
        def dfs(i):
            #只要当前的子串是的话就肯定可以再分开 反正就是要不断地遍历分开的地方
            #什么时候返回呢？？当前的长度等于1的时候 记录一个开始 记录一个结束吗
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.is_valid(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    def is_valid(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
            
            


        