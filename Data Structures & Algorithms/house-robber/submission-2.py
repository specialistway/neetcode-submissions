class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*n#dp表示到当前这一家的最大钱，包含两种情况：1 抢当前这一家 2 不抢当前这一家 dp[i-2]就表示一定不会抢i-1这一家
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        if n==2:
            return dp[1]
        #对但是有可能没有抢啊
        #这个真的不是二维的dp吗
        for i in range(2,n):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        return dp[n-1]

        