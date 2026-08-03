class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #至少得用一个set吧？？我怎么知道它之前出现了没有呢？？或者排序一下
        nums.sort()
        i=0
        while i<len(nums):
            if i+1<len(nums) and nums[i]==nums[i+1]:
                i+=2
            else:
                return nums[i]


        