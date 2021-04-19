class Solution:
    positive_limit = 2**31 -1  """ 2147483647 """
    negative_limit = -1 * (2**31) """ -2147483648 """

    def reverse(self, x: int) -> int:
        unit = 1
        if x < 0:
            unit = -1
        x = unit *x
        y = 0
        while x != 0:
            if y == positive_limit // 10:
                if x % 10 > 7:
                    return 0
            y = y*10 + x % 10
            x = x // 10 