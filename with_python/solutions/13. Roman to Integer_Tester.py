
from Integer_to_Roman import Solution as int_to_roman_sol
from Roman_to_Integer import Solution as roman_to_int_sol

int_to_roman = int_to_roman_sol(None)
roman_to_int = roman_to_int_sol(None)

D = {i: int_to_roman.intToRoman(i) for i in range(4000)}
for key,val in D.items():
    if roman_to_int.romanToInt(val) != key:
        print(key)
        break
print('got here')