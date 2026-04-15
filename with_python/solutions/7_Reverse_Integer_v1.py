class Solution:
    def reverse(self, x: int) -> int:
        unit = 1
        if x < 0:
            unit = -1
        x = unit *x
        string_x = str(x)
        y = unit * int(string_x[::-1])
        if y > -1* 2** 31 and y < 2**31 -1:
            return y
        else:
            return 0