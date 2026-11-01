class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        array=[]
        for i in range(len(nums)):
            l=len(array)
            for j in range(l):
                array.append(array[j]^nums[i])
            array.append(nums[i])
        return sum(array)


        