class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n=len(matchsticks)
        if n<4 or sum(matchsticks)%4 !=0:
            return False
        #其实需要分成4组 然后每组的和都是edge
        #不需要跳过重复的吧，那么先从大的开始分吧
        matchsticks.sort(reverse=True)
        group=[0]*4
        edge=sum(matchsticks)//4
        def dfs(stickID):
            if stickID==n:
                return True
            # res=False

            #代表现在分配第几个stick
            for i in range(4):
                if group[i]>=edge or group[i]+matchsticks[stickID]>edge:
                    continue
                if i>0 and group[i]==group[i-1]:
                    continue
                group[i]+=matchsticks[stickID]
                if dfs(stickID+1):
                    return True
                group[i]-=matchsticks[stickID]
                #已经试过一次了，之后是空的，，，，
                # if group[i]==0:
                #     break
            return False
        return dfs(0)





        