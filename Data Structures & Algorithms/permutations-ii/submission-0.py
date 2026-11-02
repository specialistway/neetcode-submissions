class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #用一个set 再把set转换回列表
        n=len(nums)
        res=[]
        perm=[]
        visit=[False]*n
        
        def dfs():
            if len(perm)==n:
                    res.append(perm.copy())
                    return
            #其实你可以先写，写着写着就会发现有啥变量缺了，
            for i in range(n):
                if visit[i]:
                    continue
                if i and nums[i]==nums[i-1] and not visit[i-1]:
                    continue
                visit[i]=True
                perm.append(nums[i])
                dfs()
                perm.pop()
                visit[i]=False
        nums.sort()
        dfs()
        return res


