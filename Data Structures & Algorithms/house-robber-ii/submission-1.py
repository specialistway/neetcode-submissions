class Solution:
    def rob(self, nums: List[int]) -> int:
        #那不还是一个道理吗 但是呢
        #就是最后一家和第一家要保证不能挨上
        #不能同时选
        #如果说就一个东西的话 切掉的话
        #dp[i]=max(dp[i-1],dp[i-2]+num)
        return max(nums[0],self.helper(nums[1:]),
        self.helper(nums[:-1]))
    def helper(self,nums):
        rob1,rob2=0,0
        for num in nums:
            temp=max(rob1+num,rob2)
            rob1=rob2
            rob2=temp
        return rob2
        