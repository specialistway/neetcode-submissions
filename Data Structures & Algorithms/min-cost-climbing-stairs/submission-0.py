class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #直接在原数组上修改
        for i in range(len(cost)-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])
