class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        W=set()
        l=0
        for r in range(len(nums)):
            if r-l>k:
                W.remove(nums[l])
                l+=1
            if nums[r] in W:
                return True
            W.add(nums[r])
        return False
    

        