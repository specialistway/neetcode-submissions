"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #greedy 的方法
        #we should process the intervals first
        time=[]
        for i in intervals:
            time.append((i.start,1))
            time.append((i.end,-1))
        #应该是根据0来排序的 但是如果0都相同 即一个开始一个结束，那么是不用加的，所以-1优先
        time.sort()
        res=0
        count=0
        for t in time:
            count+=t[1]
            res=max(res,count)
        return res




        