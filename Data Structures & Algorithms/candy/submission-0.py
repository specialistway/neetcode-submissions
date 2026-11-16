class Solution:
    def candy(self, ratings: List[int]) -> int:
        #要是这么理解的话，就是山峰的拿2 剩下的拿1呗
        #有个bug就是如果一样的话 有可能你比左右的人都拿得少1
        i=1
        n=len(ratings)
        res=n
        while i<n:
            if i<n and ratings[i]==ratings[i-1]:
                i+=1
                continue
            inc=0
            while i<n and ratings[i]>ratings[i-1]:
                # i+=1
                inc+=1
                res+=inc
                i+=1
            dec=0
            while i<n and ratings[i]<ratings[i-1]:
                dec+=1
                res+=dec
                i+=1
            res-=min(dec,inc)
        return res





    






        