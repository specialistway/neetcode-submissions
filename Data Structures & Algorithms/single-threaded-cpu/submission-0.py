class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        order=sorted(range(n),key=lambda i:tasks[i][0])
        minHeap,res=[],[]
        i=time=0
        while minHeap or i<n:
            while i<n and tasks[order[i]][0]<=time:
                idx=order[i]
                heapq.heappush(minHeap,(tasks[idx][1],idx))
                i+=1
            if not minHeap:
                time=tasks[order[i]][0]
            else:
                next_task=heapq.heappop(minHeap)
                time+=next_task[0]
                res.append(next_task[1])
        return res


        