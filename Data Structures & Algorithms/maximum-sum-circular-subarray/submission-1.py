class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #我感觉这个和滑动窗口
        #dp??
        #反正如果是正数的话就一定要扩展
        #可以试试滑动窗口
        #其实就是2遍
        #dp也可以做
        #就是它不能全不选
        globalMax,globalMin=-1e9,1e9
        curMax,curMin=-1e9,1e9#以num为结尾的最大和
        total=0
        for num in nums:
            curMax=max(num,curMax+num)
            curMin=min(num,curMin+num)
            total+=num
            globalMax=max(globalMax,curMax)
            globalMin=min(globalMin,curMin)
        return max(globalMax,total-globalMin) if globalMax>0 else globalMax

        