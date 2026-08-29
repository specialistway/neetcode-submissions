class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #dp[i,j]表示p的从i到j能匹配s从x到y
        #这道题想清楚真的很难
        #你可以听他讲的逻辑
        dp=[[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[len(s)][len(p)]=True
        for i in range(len(s),-1,-1):
            for j in range(len(p)-1,-1,-1):
                match=i<len(s) and (s[i]==p[j] or p[j]==".")#必须搭配一个用
                if (j+1)<len(p) and p[j+1]=='*':
                    #不用*
                    dp[i][j]=dp[i][j+2]
                    #必须在匹配的情况下才能使用*
                    if match:
                        dp[i][j]=dp[i+1][j] or dp[i][j]
                elif match:
                    dp[i][j]=dp[i+1][j+1]
        return dp[0][0]

