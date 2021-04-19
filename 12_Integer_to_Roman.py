class Solution:
    def string_for_this_part_of_string(self, units: int, one_letter: str, five_letter: str, ten_letter: str) -> str:
        s = ""
        if units == 4:
            s = one_letter + five_letter + s
        elif units == 9:
            s = one_letter + ten_letter + s
        else:
            while units >0:
                if units == 5:
                    s = five_letter + s
                    break
                else:
                    s = one_letter + s
                units -= 1
        return s
                
    def intToRoman(self, num: int) -> str:
        units = num % 10
        tens = (num // 10) % 10
        handreds = (num // 100) % 10
        thausends = num // 1000
        s = ""
        s = self.string_for_this_part_of_string(units,"I","V","X") + s
        s = self.string_for_this_part_of_string(tens,"X","L","C") + s
        s = self.string_for_this_part_of_string(handreds,"C","D","M") + s
        while thausends > 0:
            s = "M"+s
            thausends -=1
        return s