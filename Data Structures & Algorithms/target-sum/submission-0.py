class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1

        for num in nums:
            nextDP=defaultdict(int)
            for total,count in dp.items():
                nextDP[total+num]+=count
                nextDP[total-num]+=count
            dp=nextDP
        return dp[target]
    
       
