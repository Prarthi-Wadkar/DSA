num = 298

def count_digits(num):
    n = num
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    return count

print(count_digits(num))