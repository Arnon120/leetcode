class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return self.myPow(1/x,-n)
        else:
            return self.myPow(x*x,n//2) * self.myPow(x,n%2)


inputs = [
    [2.0,10],
    [2.1,3],
    [2.0,-2]
]
for input in inputs:
    x = input[0]
    n = input[1]
    print(Solution().myPow(x,n))

print((-3)//2)
print((-3)%2)