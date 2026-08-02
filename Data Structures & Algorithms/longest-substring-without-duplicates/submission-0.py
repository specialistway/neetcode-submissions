class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        hashSet=set()
        res=0
        #向右扩张，如果不行就向左收缩
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            hashSet.add(s[r])
            res=max(r-l+1,res)
        return res
        