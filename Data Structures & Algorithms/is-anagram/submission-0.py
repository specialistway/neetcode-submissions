from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dictionary=defaultdict(int)
        for char in s:
            if char in dictionary:
                dictionary[char]+=1
            else:
                dictionary[char]=1
        for char in t:
            if char not in dictionary:
                return False
            else:
                dictionary[char]-=1
        for key,value in dictionary.items():
            if value!=0:
                return False
        return True


        