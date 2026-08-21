class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #要么从上面 要么从左边
        dp=[[0]*n for _ in range(m)]
        for i in range(n):
            dp[0][i]=1
        for i in range(1,m):
            dp[i][0]=1
        #f[i][j]=f[i-1]+f[j-1]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]