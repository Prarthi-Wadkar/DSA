n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

#brute force method
"""
def frequency(n,m):
    for num in m:
        count = 0
        for x in n:
            if x == num:
                count += 1
        print(count)

frequency(n,m)
"""

#optimal solution
freq = {}

for i in n:
    if i in freq:
        freq[i] = +1
    else:
        freq[i] = 1

for i in m:
    print(freq.get(i, 0))