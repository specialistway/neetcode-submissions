class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #那就是要记2次呀 prev1 prev2
        #就是它下一个可以用，所以可以立马加入，但是前提是prev1!=prev2
        res=""
        maxHeap=[]
        for count,char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count!=0:
                heapq.heappush(maxHeap,(count,char))
        while maxHeap:#没有说必需要用完啊
            count,char=heapq.heappop(maxHeap)
            if len(res)>1 and res[-1]==res[-2]==char:
                #这就说明非法的情况出现了啊
                if not maxHeap:
                    break
                    # return ""
                count2,char2=heapq.heappop(maxHeap)
                res+=char2
                count2+=1
                if count2:
                    heapq.heappush(maxHeap,(count2,char2))
                heapq.heappush(maxHeap,(count,char))

            else:
                res+=char
                count+=1
                if count:
                    heapq.heappush(maxHeap,(count,char))
        return res
                    



        
        