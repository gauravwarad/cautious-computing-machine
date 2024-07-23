class Solution:
    def maximum69Number (self, num: int) -> int:

        i = 0
        num = str(num)
        num = list(num)
        while i < len(num):
            if num[i] == '6':
                num[i] = '9'
                break
            i += 1
        return int("".join(num))


print(Solution().maximum69Number(9669))