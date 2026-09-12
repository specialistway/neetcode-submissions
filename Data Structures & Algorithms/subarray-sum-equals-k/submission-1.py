class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #用一个字典记录每个prefix一共出现了几次 最多O（n）
        curSum=res=0
        prefix={0:1}#空array也是一个subarray
        for num in nums:
            curSum+=num
            res+=prefix.get(curSum-k,0)
            prefix[curSum]=1+prefix.get(curSum,0)
        return res
       
        