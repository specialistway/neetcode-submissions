class Solution:
    def reverseBits(self, n: int) -> int:
        k = 2 ** (32 - 1)
        # print(k)
        res = 0
        while n != 0:
            res += k * (n & 1)
            n = n >> 1
            k //= 2
        return res