class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m=len(s1),len(s2)
        if n+m !=len(s3):
            return False

        dp=[False]*(m+1)
        dp[m]=True
        #就是说刚开始的时候上一行和当前行是一样的？？
        for i in range(n,-1,-1):
            nextDP=[False]*(m+1)
            if i==n:
                nextDP[m]=True
            for j in range(m,-1,-1):
                if i<n and s1[i]==s3[i+j] and dp[j]:
                    nextDP[j]=True
                if j<m and s2[j]==s3[i+j] and nextDP[j+1]:
                    nextDP[j]=True
            dp=nextDP
        return dp[0]