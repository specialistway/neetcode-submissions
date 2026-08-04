class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        def count1(i):
            ans=0
            while i!=0:
                ans+=i&1
                i=i>>1
            return ans
            
        for i in range(n+1):
            res.append(count1(i))
        return res

        