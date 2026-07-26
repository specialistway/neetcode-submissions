class Solution:
    def longestPalindrome(self, s: str) -> str:
        #这个还能动态规划吗、
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        l=0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                dp[i][j]=(s[i]==s[j]) and (j-i<=2 or dp[i+1][j-1])
                if dp[i][j]==True:
                    if j-i+1>l:
                        l=j-i+1
                        res=s[i:j+1]
        return res
        