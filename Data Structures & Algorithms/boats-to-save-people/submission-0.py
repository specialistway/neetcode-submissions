class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #res=people//2+people%2
        #如果单个没有超重 但是和超重了怎么办 排序吧
        #如果超重 那么最重的那个肯定要单加一艘船嘛
        people.sort()
        left=0
        right=len(people)-1
        res=0
        while left<right:
            if people[left]+people[right]>limit:
                res+=1
                right-=1
                continue
            #那就一船走了
            res+=1
            left+=1
            right-=1
        #如果是奇数怎么办呢？？？ 如果最后left==right就需要再加一船
        if left==right:
            res+=1
        return res  

        