class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #背包问题
        #每个amount 可以从amount -c转移过来
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i]=min(dp[i],dp[i-c]+1)
        return dp[amount] if dp[amount]!=amount+1 else -1


        