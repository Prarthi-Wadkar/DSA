num = [1,2,3,4,5,6,1,1,2,2,2,2,4,6]

n = num

"""
def check_frequency(n):
    frequency = {}
    for i in range(1, len(n)):
        if n[i] in frequency:
            frequency[n[i]] += 1

        else:
            frequency[n[i]] = 1

    print(frequency)

print(check_frequency(n))

"""

#using .get()
def frequency(n):
    freq = {}
    length = len(n)
    for i in range(0,length):
        freq[n[i]] = freq.get(n[i],0) + 1
    print(freq)

print(frequency(n))
