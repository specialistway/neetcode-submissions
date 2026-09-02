class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        jihe=set()
        for num in nums:
            if num in jihe:
                return True
            else:
                jihe.add(num)
        return False