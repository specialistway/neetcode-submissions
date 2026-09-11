class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #摩尔投票啊！！ 那最多两个数字
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
            if len(freq)<=2:#如果包含2个条目 就要减了 如果没有的话就不用减了
                continue
            new_freq=defaultdict(int)
            for x,c in freq.items():
                if c>1:
                    new_freq[x]=c-1
            freq=new_freq
        res=[]
        for x in freq:
            if nums.count(x)>len(nums)//3:
                res.append(x)
        return res