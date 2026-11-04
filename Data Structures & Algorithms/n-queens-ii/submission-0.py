class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        
        # col: 列状态
        # diag1: 正对角线 (row + col 恒定)
        # diag2: 反对角线 (row - col 恒定)
        def dfs(r: int, col: int, diag1: int, diag2: int):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                # 检查列、正对角线、反对角线是否已被占用
                # 注意反对角线 r - c 可能为负数，加上 n 防止位移报错
                if (col & (1 << c)) or (diag1 & (1 << (r + c))) or (diag2 & (1 << (r - c + n))):
                    continue
                
                # 向下递归时，通过按位或 (|) 加上当前放置皇后的位置限制
                dfs(r + 1, 
                    col | (1 << c), 
                    diag1 | (1 << (r + c)), 
                    diag2 | (1 << (r - c + n)))

        dfs(0, 0, 0, 0)
        return res

   

                


        