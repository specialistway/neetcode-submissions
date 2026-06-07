class KthLargest:
    #第k个最大的数就只需要保留前k个数 ，然后每次插入就行了

    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k=nums,k
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        while len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
