class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=100001
        S=0
        l=0
        for r in range(len(nums)):
            S+=nums[r]
            while l<=r and S>=target:
                res=min(res,r-l+1)
                S-=nums[l]
                l+=1               
        return res if res!=100001 else 0




        