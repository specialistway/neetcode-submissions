class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #递归可以做 
        res=[[]]
        for num in nums:
            res+=[subset+[num] for subset in res]
        return res

        