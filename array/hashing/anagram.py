s = "anagram"
t = "angaram"

def anagram(s,t):
    if len(s) != len(t):
        return False
    frequency_s = {}
    frequency_t = {}

    for character in s:
        if character in frequency_s:
            frequency_s[character] = frequency_s[character] + 1
        else:
            frequency_s[character] = 1

        
    for characters in t:
        if characters in frequency_t:
            frequency_t[characters] = frequency_t[characters] + 1
        else:
            frequency_t[characters] = 1

        
    if frequency_s == frequency_t:
        return True
    else:
        return False
    
    
print(anagram(s,t))
