class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #前缀和的问题呀，把matrix改造一下
        n=len(matrix)
        m=len(matrix[0])
        for i in range(1,m):
            matrix[0][i]+=matrix[0][i-1]
        for i in range(1,n):
            matrix[i][0]+=matrix[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
    
                matrix[i][j]+=matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]
        self.matrix=matrix


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return (self.matrix[row2][col2]
        -(self.matrix[row2][col1-1] if col1>=1 else 0 )
        -(self.matrix[row1-1][col2] if row1>=1 else 0 )
        +(self.matrix[row1-1][col1-1] if (row1>=1 and col1>=1) else 0))
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)