class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        minH=[[grid[0][0],0,0]]
        visit=set()
        visit.add((0,0))
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while minH:
            t,r,c=heapq.heappop(minH)
            if r==N-1 and c==N-1:
                return t
            for dr,dc in directions:
                newR,newC=r+dr,c+dc
                if newR<0 or newR>=N or newC<0 or newC>=N or (newR,newC) in visit:
                    continue
                visit.add((newR,newC))
                heapq.heappush(minH,(max(t,grid[newR][newC]),newR,newC))