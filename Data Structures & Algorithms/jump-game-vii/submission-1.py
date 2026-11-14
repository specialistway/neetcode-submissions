class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #其实就是倒着能不能到0
        #dp[i]表示i能不能到达
        n=len(s)
        if s[n-1]=='1':
            return False
        dp=[False]*n
        dp[0]=True
        cnt=0
        for i in range(1,n):
            if i>=minJump and dp[i-minJump]:
                cnt+=1
            if i>maxJump and dp[i-maxJump-1]:
                cnt-=1
            if cnt>0 and s[i]=='0':
                dp[i]=True
        return dp[n-1]

        

        