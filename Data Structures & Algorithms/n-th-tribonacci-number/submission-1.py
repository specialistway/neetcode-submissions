class Solution:
    def tribonacci(self, n: int) -> int:
        #哦，它等于前面3个数的和啊
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        p1,p2,p3=0,1,1
        tmp=0
        for _ in range(3,n+1):
            tmp=p1+p2+p3
            p1,p2,p3=p2,p3,tmp
        return tmp


        