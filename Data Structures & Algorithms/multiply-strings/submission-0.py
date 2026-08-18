class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #如何乘起来字符串呢？
        def convertTo(nums):
            k=1
            res=0
            nums=reversed(nums)
            for num in nums:
                res+=k*(ord(num)-ord('0'))
                k*=10
            return res
        ans=convertTo(num1)*convertTo(num2)
        return str(ans)

       
        