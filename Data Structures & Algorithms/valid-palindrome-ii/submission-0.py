class Solution:
    def validPalindrome(self, s: str) -> bool:
        def judge(i,j,flag):
            if i>=j:
                return True
            if s[i]==s[j]:
                return judge(i+1,j-1,flag)
            elif flag==True:
                return judge(i+1,j,False) or judge(i,j-1,False)
            else:
                return False
        return judge(0,len(s)-1,True)
        