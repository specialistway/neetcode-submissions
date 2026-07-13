class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #要么选要么不选，那这个就简单多了呀 010101的所有 组合
        res=[]
        candidates.sort()
        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if total>target or i >=len(candidates):
                return
            cur.append(candidates[i])
            # total+=candidates[i]
            dfs(i+1,cur,total+candidates[i])
            cur.pop()
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,cur,total)
        
        dfs(0,[],0)
        return res


        