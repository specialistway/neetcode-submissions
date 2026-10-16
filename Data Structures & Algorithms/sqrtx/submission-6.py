class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        res=0
        while l<=r:
            mid=l+r>>1
            if mid**2==x:
                return mid
            elif mid**2<x:
                l=mid+1
                res=mid
            else:
                r=mid-1
        return res

        