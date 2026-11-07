class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #那肯定要先排序吧 按照第一个排序
        L,R=float("inf"),float("-inf")
        for _,start,end in trips:
            L=min(L,start)
            R=max(R,end)
        N=R-L+1
        points=[0]*int(N+1)
        for passengers,start,end in trips:
            points[start-L]+=passengers
            points[end-L]-=passengers
        curPass=0
        for p in points:
            curPass+=p
            if curPass>capacity:
                return False
        return True


        
        