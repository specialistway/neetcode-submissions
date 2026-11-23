class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        res=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    res+=4
                    if i and grid[i-1][j]:
                        res-=2
                    if j and grid[i][j-1]:
                        res-=2
        return res

        