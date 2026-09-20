num = 20
n = num 

#brute force method
def factors(n):
    result = []
    for no in range(1, n+1):
        if n%no == 0:
            result.append(no)
    print(result)
factors(n)

"""
#better option
def factors(n):
    result1 = []
    
    for i in range(1, n//2):
        if n%i == 0:
            result1.append(i)
    result1.append(n)

factors(n)
"""

"""
#optimal solution
def factors(n):
    result = []
    for i in range(1, int(sqrt(n)):
        if n%i == 0:
            result.append(i)
            if n//i != i:
                result.append(num//i)
    result.sort()
    return result
factors(n)
"""