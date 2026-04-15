class Solution:
    """
    Runtime: 56 ms, faster than 13.05% of Python3 online submissions for Sqrt(x).
    Memory Usage: 13.8 MB, less than 99.84% of Python3 online submissions for Sqrt(x).
    """
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

    """
    Other Solution
    
    Best memo - use. Good time.
    Simply binary search on ints for best solution. 

    class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        while left <= right:
            guess = left + (right - left) // 2
            sq = guess * guess
            if sq > x:
                right = guess - 1
            elif sq < x:
                left = guess + 1
            else:
                return guess
        
        return right
    """