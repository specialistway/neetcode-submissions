class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n<k or sum(nums)%k!=0:
            return False
        nums.sort(reverse=True)
        bound=sum(nums)//k
        group=[0]*k
        def dfs(id):
            if id==n:
                return True
            for i in range(k):
                if group[i]+nums[id]>bound:
                    continue
                if i and group[i]==group[i-1]:
                    continue
                group[i]+=nums[id]
                if dfs(id+1):
                    return True
                group[i]-=nums[id]
            return False
        return dfs(0)


        