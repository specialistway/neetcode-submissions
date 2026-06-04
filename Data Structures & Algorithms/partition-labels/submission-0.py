class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #每一个字母只出现在一个字串里面
        #尽可能的多
        #那就是说 只要有相同的字母 这个就是一个子串了
        lastIndex={}
        for i,c in enumerate(s):
            lastIndex[c]=i
        end=0
        size=0
        res=[]
        for i,c in enumerate(s):
            
            size+=1
            end=max(end,lastIndex[c])
            if i==end:
                res.append(size)
                size=0
        return res