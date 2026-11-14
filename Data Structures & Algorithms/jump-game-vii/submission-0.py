class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #其实就是倒着能不能到0
        #dp[i]表示i能不能到达
        n=len(s)
        dp=[False]*n
        dp[0]=True
        for i in range(n):
            if s[i]=='1':
                continue
            for j in range(i-maxJump,i-minJump+1):
                if j<0:
                    continue
                if dp[j]:
                    dp[i]=True
                    break
        return dp[n-1]
        

        