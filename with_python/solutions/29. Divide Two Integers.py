class Solution:
    def divide_helper (self, dividend: int, divisor: int) -> int:
        quotient = 0
        while dividend >= divisor:
            quotient += 1
            dividend = dividend - divisor
        return quotient
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0:
            sign = sign * (-1)
            dividend = -1 * dividend
        if divisor < 0:
            sign = sign * (-1)
            divisor = -1 * divisor
        return sign * self.divide_helper(dividend,divisor)