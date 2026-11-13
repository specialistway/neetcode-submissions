class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #跟之前我写的
        #卡丹算法是找sum最大的
        #这个是找符合条件最长的
        #暴力就是枚举
        #其实下一个合不合法只和上一个有关
        #也可以用卡丹算法 以某个元素为结尾的最长的东西
        curml=1
        globalml=1#0 2
        flag=0
        for i in range(1,len(arr)):
            if (arr[i]>arr[i-1] and flag==-1) or (arr[i]<arr[i-1] and flag==1):
                curml+=1
                flag=flag*(-1)
            elif arr[i]!=arr[i-1]:
                curml=2
                flag=1 if arr[i]>arr[i-1] else -1
                # 那就是说flag不用改变，
            else:
                #如果相等怎么办呢
                # continue
                curml=1
                flag=0
            globalml=max(globalml,curml)
        return globalml



        