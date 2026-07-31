class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 只需要判断要不要进位
        cur = len(digits) - 1
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            while digits[cur] == 9:
                digits[cur] = 0
                cur -= 1
            if cur == -1:
                digits.insert(0, 1)
            else:
                digits[cur] += 1

        return digits