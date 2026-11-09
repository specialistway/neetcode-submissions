class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #优先队列，先进先出嘛
        #room endtime,nums 最后还要比较一下哪个次数最大？？
        meetings.sort()
        rooms=[0]*n
        meeting_count=[0]*n

        for start,end in meetings:
            min_room=0
            found=False
            for i in range(n):
                if rooms[i]<=start:
                    found=True
                    meeting_count[i]+=1
                    rooms[i]=end
                    break
                if rooms[min_room]>rooms[i]:
                    min_room=i
            if found:
                continue
            meeting_count[min_room]+=1
            rooms[min_room]+=end-start
        return meeting_count.index(max(meeting_count))


  


        