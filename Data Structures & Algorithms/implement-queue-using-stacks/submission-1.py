class MyQueue:
    #怎么保证我pop出来的永远是最早加进去的呢
    #我知道了
    #1负责存 2负责吐 每次吐完了再存回去

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        
    def peek(self) -> int:
        while not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        
        
    def empty(self) -> bool:
        return max(len(self.stack1),len(self.stack2))==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()