class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s is a subsequence of t
        i=j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)

        