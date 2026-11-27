class Solution:
    def integerBreak(self, n: int) -> int:
        #dp[i] 加到i的最大乘积
        #拆了之后乘积最大
        #尽量往square方面拆？？ 别有1
        if n==2:
            return 1
        dp=[0]*(n+1)
        dp[1]=1
        # dp[2]=2#0+2
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i]=max(dp[i],dp[j]*(i-j),j*(i-j))
        return dp[n]


            
            


        