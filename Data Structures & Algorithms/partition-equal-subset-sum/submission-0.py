class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #这没有递归子结构
        #就是选呗
        #从0-target
        # 能不能凑出来
        # dp[i]=dp[i-num] for num in nums
        # sorted(nums)
        #对于一个数 要么选 要么不选
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        dp=[False]*(target+1)#dp这里是需要+1的
        dp[0]=True
        for num in nums:
            for j in range(target,num-1,-1):
                dp[j]=dp[j] or dp[j-num]
        return dp[target]

      

        



        