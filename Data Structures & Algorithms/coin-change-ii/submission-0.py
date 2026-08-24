class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        f=[0]*(amount+1)
        f[0]=1
        for coin in coins:
            for j in range(1,amount+1):
                if j>=coin:
                    f[j]+=f[j-coin]
        return f[amount]

