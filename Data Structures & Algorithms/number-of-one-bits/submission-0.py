class Solution:
    def hammingWeight(self, n: int) -> int:
        #数数
        res=0
        while n!=0:
            res+=(n & 1)
            n=n>>1
        return res
        