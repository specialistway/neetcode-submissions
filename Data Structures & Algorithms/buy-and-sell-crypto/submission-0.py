class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowprice=prices[0]
        res=0
        for price in prices:
            lowprice=min(price,lowprice)
            res=max(res,price-lowprice)
        return res
        