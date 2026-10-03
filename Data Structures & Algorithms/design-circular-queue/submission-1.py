class MyCircularQueue:

    def __init__(self, k: int):
        self.q=[-1]*k
        self.left=-1
        self.right=0
        self.k=k
        

    def enQueue(self, value: int) -> bool:
        if ((self.right-self.left+self.k)%self.k==1 or self.right-self.left==1) and self.q[(self.left+1)%self.k]!=-1:
            return False
        self.q[self.right]=value
        self.right=(self.right+1)%self.k
        return True
        

    def deQueue(self) -> bool:
        if self.q[(self.left+1)%self.k]==-1:
            return False
        self.q[(self.left+1)%self.k]=-1
        self.left=(self.left+1)%self.k
        return True
        
    
    def Front(self) -> int:
        return self.q[(self.left+1)%self.k]
        

    def Rear(self) -> int:
        return self.q[(self.right-1+self.k)%self.k]
        
    def isEmpty(self) -> bool:
        return self.q[(self.left+1)%self.k]==-1

    def isFull(self) -> bool:
        return ((self.right-self.left+self.k)%self.k==1 or self.right-self.left==1) and self.q[(self.left+1)%self.k]!=-1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()