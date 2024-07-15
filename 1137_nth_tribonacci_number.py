class Solution:
    def tribonacci(self, n: int) -> int:
        
        arr = [0, 1, 1]
        # arr[0] = 0
        # arr[1] = 1
        # arr[2] = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        for i in range(3, n + 1):
            arr.append(arr[i-1] + arr[i-2] + arr[i-3])
        print(arr)
        return (arr[i])


    def tribonacci2(self, n):
        # without array?
        a = 0
        b = 1
        c = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        for _ in range(3, n+1):
            d = a + b + c
            a = b
            b = c
            c = d
        
        return d

n = 25
print(Solution().tribonacci2(n))