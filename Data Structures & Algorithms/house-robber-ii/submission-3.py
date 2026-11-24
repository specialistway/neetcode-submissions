class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        rob1,rob2=0,0
        for i in range(len(nums)-1):
            tmp=max(nums[i]+rob1,rob2)
            rob1=rob2
            rob2=tmp
        #res1=rob2
        rob3,rob4=0,0
        #n>2
        for i in range(1,len(nums)):
            tmp=max(nums[i]+rob3,rob4)
            rob3=rob4
            rob4=tmp
        return max(rob2,rob4)
