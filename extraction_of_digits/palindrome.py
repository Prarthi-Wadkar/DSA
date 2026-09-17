num = 1234
n = num

def checkPalindrome(n):
    result = 0

    while n > 0:
        digit = n % 10
        result = result * 10 + digit
        n = n // 10          

    if result == num:
        return True
    else:
        return False

print(checkPalindrome(n))