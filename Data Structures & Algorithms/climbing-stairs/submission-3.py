class Solution:
    def climbStairs(self, n: int) -> int:
        # dp=[0]*(n+1)
        p1=1
        p2=1
        # dp[2]=1
        for i in range(2,n+1):
            # dp[i]=dp[i-1]+dp[i-2]
            tmp=p1+p2
            p1=p2
            p2=tmp
            # p1=p2
        return p2


        