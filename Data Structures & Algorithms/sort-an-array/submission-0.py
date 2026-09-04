class Solution:
    def partition(self,nums,left,right)->int:
        mid=(left+right)>>1
        nums[mid],nums[left+1]=nums[left+1],nums[mid]
        if nums[left]>nums[right]:
            nums[left],nums[right]=nums[right],nums[left]
        if nums[left+1]>nums[right]:
            nums[left+1],nums[right]=nums[right],nums[left+1]
        if nums[left]>nums[left+1]:
            nums[left],nums[left+1]=nums[left+1],nums[left]
        pivot=nums[left+1]
        i=left+1
        j=right
        while True:
            while True:
                i+=1
                if nums[i]>=pivot:
                    break
            while True:
                j-=1
                if nums[j]<=pivot:
                    break
            if i>j:
                break
            nums[i],nums[j]=nums[j],nums[i]
        #肯定是把小的换过来
        nums[left+1],nums[j]=nums[j],nums[left+1]
        return j


        
    def quicksort(self,nums,left,right)->None:
        if right<=left+1:
            if right==left+1 and nums[right]<nums[left]:
                nums[left],nums[right]=nums[right],nums[left]
            return
        j=self.partition(nums,left,right)
        self.quicksort(nums,left,j-1)
        self.quicksort(nums,j+1,right)
    def sortArray(self, nums: List[int]) -> List[int]:
        #复习一下快速排序吧
        self.quicksort(nums,0,len(nums)-1)
        return nums

        