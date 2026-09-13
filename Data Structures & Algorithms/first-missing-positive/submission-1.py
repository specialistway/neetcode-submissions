class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 超出index的情况也提前处理 了 每次都while到正确的位置上
        n=len(nums)
        i=0
        while i<n:
            if nums[i]>n or nums[i]<=0:
                i+=1
                continue
            index=nums[i]-1
            #1->nums[0]
            #nums[i]->nums[nums[i]-1]
            if nums[i]!=nums[index]:
                nums[i],nums[index]=nums[index],nums[i]
            else:
                #numsi==nums[index] 就是说此位置就是正确的位置 或者已经重复了并且放到正确的位置上了，就不用再交换了
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
