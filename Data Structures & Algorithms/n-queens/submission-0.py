class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=0
        negDiag=0
        posDiag=0

        res,ans=[],[["."]*n for _ in range(n)]
        def dfs(i):
            nonlocal col,posDiag,negDiag
            if i>=n:
                res.append([''.join(row) for row in ans])
                return
            for j in range(n):
                #如果说等于0 的话才可以，是的 由于其他位都是0啊 如果说不等于0的话呢那就不行所以没问题啊
                if (col & 1<<j) or (posDiag & 1<<(i+j)) or (negDiag& 1<<(i-j+n)):
                    continue
                col |=1<<j
                posDiag |= 1<<(i+j)
                negDiag|=1<<(i-j+n)
                ans[i][j]='Q'
                dfs(i+1)
                ans[i][j]='.'
                col &=~(1<<j)
                posDiag&=~(1<<(i+j))
                negDiag&=~(1<<(i-j+n))
        dfs(0)
        return res
      
