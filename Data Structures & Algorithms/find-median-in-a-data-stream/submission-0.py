class MedianFinder:
#最简单的办法就是每次都排一次序
    def __init__(self):
        self.lst=[]

    def addNum(self, num: int) -> None:
        self.lst.append(num)
        self.lst.sort()

    def findMedian(self) -> float:
        n=len(self.lst)
        if n%2==0:
            return (self.lst[n//2-1]+self.lst[n//2])/2.0
        else:
            return self.lst[n//2]

        