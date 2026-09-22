class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        #是先移动还是先判断呢，保留第一个重复的
        #先判断吧
        res=0
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                k+=1
                continue
            #直接往前移动k个就行了
            res+=1
            #说明没有重复
            if k>0:
                nums[i-k]=nums[i]

        return res

