class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #标记一下哪些行和列已经是0了就跳过
        n,m=len(matrix),len(matrix[0])
        col=0
        row=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]!=0:
                    continue
                row |=1<<i
                col |=1<<j
        for i in range(n):
            for j in range(m):
                if row&(1<<i) or col&(1<<j):
                    matrix[i][j]=0
        