class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))
            res+='#'
            res+=s
        return res


    def decode(self, s: str) -> List[str]:
        res=[]
        start=0
        while start<len(s):
            j=start
            while s[j]!='#':
                j+=1
            length=int(s[start:j])#因为j的位置是#
            start=j+1
            j=start+length
            res.append(s[start:j])
            start=j
        return res
