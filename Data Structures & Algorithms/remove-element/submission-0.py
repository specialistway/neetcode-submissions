class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #我觉得一趟就够了循环往前搬
        j=0
        k=0
        for i in range(len(nums)):
            #j记录一下需要往前移动几个呗？？
            #先移动呢还是先判断呢？？
            if nums[i]==val:
                j+=1
                continue
            #后移动
            k+=1
            if j==0:
                continue
            nums[i-j]=nums[i]
        return k
            
            
