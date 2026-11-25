class Solution:
    def longestPalindrome(self, s: str) -> str:
        #双指针
        #dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
        n=len(s)
        l=0
        dp=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    if j-i+1>l:
                        l=j-i+1
                        res=s[i:j+1]
        return res


        