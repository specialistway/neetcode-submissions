class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        path=[]
        res=[]
        #每次dfs都搞定一个长度的，同一个长度的不回头
        def dfs(length,start):
            if len(path)==length:
                res.append(path.copy())
                return
            for i in range(start,n):
                path.append(nums[i])
                dfs(length,i+1)
                path.pop()
        for i in range(n+1):
            dfs(i,0)
        return res



        