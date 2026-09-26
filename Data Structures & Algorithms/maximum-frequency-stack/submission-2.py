class FreqStack:

    def __init__(self):
  
        self.cnt=defaultdict(int)
        self.freq=defaultdict(list)

    def push(self, val: int) -> None:
        self.cnt[val]+=1
        self.freq[self.cnt[val]].append(val)


        

    def pop(self) -> int:
        res= max(i for i in self.freq)
        ans = self.freq[res].pop()
        self.cnt[ans]-=1
        if len(self.freq[res]) < 1:
            del self.freq[res]
        return ans
        