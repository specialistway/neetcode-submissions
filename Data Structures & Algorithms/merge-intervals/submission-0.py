class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #如果有merge的话就要一直判断
        #prev
        res=[]
        intervals.sort(key=lambda i:i[0])
        prev=intervals[0]
        for i in range(1,len(intervals)):
            if prev[1]<intervals[i][0]:
                res.append(prev)
                prev=intervals[i]
            #不可能prev完全在后面
            else:
                prev=[
                    min(prev[0],intervals[i][0]),
                    max(prev[1],intervals[i][1])
                ]
        res.append(prev)
        return res

        