num = 298

def count_digits(num):
    n = num
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    return count

print(count_digits(num))


#another method
"""
from math import * 
def countDigits(num):
    return int(log10(num) + 1)
print(countDigits(num))
"""
"""
#one more method
num = str(num)
print(len(num)) """