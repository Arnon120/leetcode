class Solution:
    def mySqrt(self, x: int) -> int:
        y = x //2
        while y > 0:
            if y ** 2 > x:
                y = y // 2
            elif y ** 2 == x:
                return y
            else:
                break
        while (y+1)**2 <= x:
            z = 2
            while (y + y // z) ** 2 > x:
                z *= 2
            y += max(y // z, 1)
        return y

for i in range(0,10):
    y = Solution().mySqrt(i)
    print(y)