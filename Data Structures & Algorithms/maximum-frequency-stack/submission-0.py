class FreqStack:
    #它这个东西一定是连续的
    def __init__(self):
        #最大堆去实现
        self.cnt={}
        self.stack=[[]]

    def push(self, val: int) -> None:
        valCnt=1+self.cnt.get(val,0)
        self.cnt[val]=valCnt
        if valCnt==len(self.stack):
            self.stack.append([])
        self.stack[valCnt].append(val)
        

    def pop(self) -> int:
        res=self.stack[-1].pop()
        self.cnt[res]-=1
        if not self.stack[-1]:
            self.stack.pop()
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()