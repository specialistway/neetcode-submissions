class Solution:
    def reorganizeString(self, s: str) -> str:
        #直接建一个defaultdict
        #哦我知道了，要建立一个最大堆啊，每次都放置能放置的剩余次数最大的那个剩余次数最大堆那个！！！
        count=Counter(s)
        maxHeap=[[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(maxHeap)
        res=""
        prev=None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt,char=heapq.heappop(maxHeap)
            res+=char
            cnt+=1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev=None
            if cnt!=0:
                prev=[cnt,char]
        return res


        