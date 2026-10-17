class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def canShip(cap):#这个容量能不能days内运完
            ships,curCap=1,cap
            for w in weights:
                if curCap-w<0:
                    ships+=1
                    curCap=cap
                curCap-=w
            return ships<=days
        while l<=r:
            mid=l+r>>1
            if canShip(mid):
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res
            

        