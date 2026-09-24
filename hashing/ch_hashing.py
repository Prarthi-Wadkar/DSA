#character hsahing

a = ["a","z","y","x","y","y","z","a","a","a","a"]
b = ["d","a","y","x"]

frequency = {}

for i in a:
    if i in frequency:
        frequency[i] = frequency[i] +1
    else:
        frequency[i] = 1

for i in b:
    print(frequency.get(i,0))