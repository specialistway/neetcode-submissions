class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree=[0]*(n+1)
        for pair in trust:
            src,target=pair[0],pair[1]
            degree[src]-=1
            degree[target]+=1
        for i,people in enumerate(degree):
            if people==n-1:
                return i
        return -1


        