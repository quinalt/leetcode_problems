# basic problem - return a reversed string 

def rev_string(s):
    for i, char in enumerate(list(reversed(s))):
        s[i] = char
