class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senates=list(senate)
        cnt=0
        i=0
        while i<len(senates):
            c=senates[i]
            if c=='R':
                if cnt<0:
                    senates.append('D')
                cnt+=1
            else:
                if cnt>0:
                    senates.append('R')
                cnt-=1
            i+=1

        return "Radiant" if cnt>0 else "Dire"
                


     



        