class Solution:
    def totalNQueens(self, n: int) -> int:
        res=0
        col,diag1,diag2=0,0,0
        def dfs(r):
            nonlocal res,col,diag1,diag2
            if r==n:
                res+=1
                return
            for c in range(n):
                if (col &(1<<c)) or (diag1 &(1<<(r+c))) or (diag2 &(1<<(r-c+n))):
                    continue
                col ^=(1<<c)
                diag1^=(1<<(r+c))
                diag2^=(1<<(r-c+n))
                dfs(r+1)
                col ^=(1<<c)
                diag1^=(1<<(r+c))
                diag2^=(1<<(r-c+n))
        dfs(0)
        return res

                
    

   

                


        