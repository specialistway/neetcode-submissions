class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #k=n//2
        #0 1 2 3 
        #0+3 =1+2=3
        #0 1 2 3 4
        #0+4=1+3=2+2=4
        k=len(s)-1
        for i in range(k//2+1):#右开
            index=k-i
            s[i],s[index]=s[index],s[i]
        

        