class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change=[0]*2# 0 for 5$;1for 10$
        for bill in bills:
            if bill-5:
                if bill-5==5:#如果是10
                    change[0]-=1
                    change[1]+=1
                    if change[0]<0:
                        return False
                else:#如果是20
                    #先尝试1张10
                    if change[1]>=1 and change[0]>=1:
                        change[1]-=1
                        change[0]-=1
                    elif change[0]>=3:
                        change[0]-=3
                    else:
                        return False
            else:
                change[0]+=1
        return True


        