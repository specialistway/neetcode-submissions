class Solution:
    def isHappy(self, n: int) -> bool:
        #如果有重复的那就不是 
        #什么样子的数字不能得到1呢？？
        #其实只有 1 10 100 1000 100000才能得到吧
        #直接模拟吗
        #如果是1的话那么slow 和FAST也都会等于1
        slow,fast=n,self.sumOfSquare(n)
        while slow!=fast:
            slow=self.sumOfSquare(slow)
            fast=self.sumOfSquare(fast)
            fast=self.sumOfSquare(fast)
        return slow==1
    def sumOfSquare(self,n:int)->int:
        output=0
        while n:
            digits=n%10
            output+=digits**2
            n=n//10
        return output

        