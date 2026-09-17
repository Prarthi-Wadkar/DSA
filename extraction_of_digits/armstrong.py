#return true if armstrong
num = 153
n = num

def armstrong(n):
    digits = len(str(n))
    total = 0

    while n > 0:
        last_digit = n% 10 
        total = total + (last_digit **digits)
        n = n//10        

    return total

print(armstrong(n))