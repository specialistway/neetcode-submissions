class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #至少得用一个set吧？？我怎么知道它之前出现了没有呢？？或者排序一下
        #用bit表示出现过了没有
        #你怎么判断一个数字出现过了呢
        res=0
        for num in nums:
            res^=num
        return res
       


        