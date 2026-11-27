class Solution:
    def numSquares(self, n: int) -> int:
        #dp[i]加到i最少要用几个数字
        num=int(math.sqrt(n))
        dp=[n]*(n+1)
        dp[0]=0
        for i in range(n+1):
            for j in range(1,num+1):
                if i-j**2>=0:
                    dp[i]=min(dp[i-j**2]+1,dp[i])
                else:
                    break
        return dp[n]

        