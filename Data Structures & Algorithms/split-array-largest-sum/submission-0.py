class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #对可能的结果范围进行二分吗？？？
        #这个其实要进行2次二分？？？？其实不用吧 最远的地方emmmm
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]#它的这个index其实是从1到n，index其实都无所谓的
        def canSplit(target):
            #i是每次的起点
            i=0#其实还挺巧妙的，i-j之间应该是 pj-p i-1 
            subarrays=0
            while i<n:
                l,r=i+1,n#r最后会停在最远可行解上吗 区间里只有一个数了 mid=r=l
                while l<=r:
                    mid=l+r>>1
                    if prefix[mid]-prefix[i]<=target:
                        l=mid+1
                    else:
                        r=mid-1
                i=r
                subarrays+=1
                if subarrays>k:
                    return False
            return True


        l,r=max(nums),sum(nums)
        res=r
        while l<=r:
            mid=l+(r-l)//2
            if canSplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res



        