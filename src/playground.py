import sys
from pycipher import Caesar

sys.path.append('utils')
import sort

print(sort.order_fct([1, 3, 7, 4, 2, 9]))


ciphered = Caesar(key=1).encipher('defend the east wall of the castle')
# 'EFGFOEUIFFBTUXBMMPGUIFDBTUMF'
print(ciphered)

deciphered = Caesar(key=1).decipher('EFGFOEUIFFBTUXBMMPGUIFDBTUMF')
# 'DEFENDTHEEASTWALLOFTHECASTLE'
print(deciphered)